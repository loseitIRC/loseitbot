from __future__ import absolute_import
from sopel import module
import os
import sqlite3

@module.require_owner()
@module.commands("cal", "calories")
@module.example("!calories cheese, cheddar")
def caloriesCmd(bot, trigger):
    """ 
    Attempts to retrieve the amount of calories per 100g of a food from USDA's NDB SR28
    """
    foodName = trigger.group(2)
    replyFmt = '"%s" has %i kcal per 100 g'
    if foodName is None:
        return False
    res = lookupFood(foodName + "%")

    if res:
        bot.reply(replyFmt % (res[1], res[-1]))
        print(replyFmt % (res[1], res[-1]))
    else:
        # if we were given two things to search for, try "secondWord%firstWord%" 
        foodName = "%".join(foodName.split(' ')[1::-1])
        res = lookupFood(foodName + "%")
        if res:
            bot.reply(replyFmt % (res[1], res[-1]))
            print(replyFmt % (res[1], res[-1]))
        else:
            bot.reply('No results')

def lookupFood(foodName):
    conn = sqlite3.connect(os.path.dirname(__file__) + '/nutrients.db')
    c = conn.cursor()
    cmd = '''
    SELECT food_des.NDB_No, Long_Desc, Shrt_Desc, ComName, Nutr_Val 
    FROM food_des 
    JOIN nut_data 
        ON food_des.NDB_No = nut_data.NDB_No 
    WHERE Long_Desc LIKE ? 
        AND Nutr_No = '208' 
    LIMIT 1;
    '''

#     c.execute(cmd)
    c.execute(cmd, (foodName,))

    foods = c.fetchall()
    if len(foods) is 0:
        return False
    else:
        return foods[0]
