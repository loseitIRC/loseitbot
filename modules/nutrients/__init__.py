from __future__ import absolute_import
from fuzzywuzzy import process, fuzz
from sopel import module

import os
import sqlite3
import requests

# Nutr_No constants
CALORIE = 208
PROTEIN = 203
FAT = 204
CARB = 205
SUGAR = 269
FIBER = 291

with open('usdaapikey', 'r') as f:
    APIKEY = f.read().strip()

class NDBSearch():
    def __init__(self):
        self.exclude_foodgroups = {'Baby Foods'}

    def process_response(self, r):
        if r.ok:
            return r.json()
        else:
            return False 

    def search(self, name):
        payload = {'format': 'json',
                  'ds': 'Standard Reference',
                  'q': name,
                  'sort': 'r',
                  'max': 50,
                  'api_key': APIKEY}
        url = 'https://api.nal.usda.gov/ndb/search/'
        r = requests.get(url, params=payload)
        return self.process_response(r)
    
    def get_calories(self, ndbno):
        payload = {'format': 'json', 
                   'api_key': APIKEY,
                   'nutrients': CALORIE,
                   'ndbno': ndbno}
        url = 'http://api.nal.usda.gov/ndb/nutrients/'
        r = requests.get(url, params=payload)
        data = self.process_response(r)
        if data:
            return [int(n['gm']) for n in data['report']['foods'][0]['nutrients'] if int(n['nutrient_id']) == CALORIE][0]
        
NDBSearch = NDBSearch()

@module.rate(10)
@module.commands("cal", "calories")
@module.example("!calories cheddar cheese")
def calories_command(bot, trigger):
    query = trigger.group(2)
    results = NDBSearch.search(query)
    if 'list' in results.keys():
      filtered_results = [food['name'] for food in results['list']['item'] if food['group'] not in NDBSearch.exclude_foodgroups]
      weighted = process.extract(query, filtered_results, scorer=fuzz.token_sort_ratio)
      topFood = [food for food in results['list']['item'] if food['name'] == weighted[0][0]][0]
      foodname = topfood['name']
      ndbno = topfood['ndbno']
      calories = NDBSearch.get_calories(ndbno)
      if calories is not None:
          bot.reply('"{foodname}" has {calories:.0f} kcal per 100 g. See more results at https://ndb.nal.usda.gov/ndb/search/list?qlookup={query}'.format(foodname=foodname, calories=calories, query=requests.utils.quote(query)))
          return
    bot.reply("No result")

