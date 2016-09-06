from __future__ import absolute_import
from sopel import module
import os
import sqlite3

# Nutr_No constants
CALORIE = 208
PROTEIN = 203
FAT = 204
CARB = 205
SUGAR = 269
FIBER = 291

@module.commands("cal", "calories")
@module.example("!calories cheddar cheese")
def caloriesCmd(bot, trigger):
    """ 
    Retrieve the amount of calories per 100g of a food from USDA's NDB SR28
    """
    replyFmt = '"%s" has %i kcal per 100 g'
    lookup = lookupFoodAndReply(bot, trigger, replyFmt, nutrient=CALORIE)


@module.commands("fat")
@module.example("!fat cheddar cheese")
def fatCmd(bot, trigger):
    """ 
    Retrieve the amount of fat per 100g of a food from USDA's NDB SR28
    """
    replyFmt = '"%s" has %.1f g fat per 100 g'
    lookup = lookupFoodAndReply(bot, trigger, replyFmt, nutrient=FAT)


@module.commands("carb[s]?")
@module.example("!carb cheddar cheese")
def carbCmd(bot, trigger):
    """ 
    Attempts to retrieve the amount of carb per 100g of a food from USDA's NDB SR28
    """
    replyFmt = '"%s" has %.1f g carb per 100 g'
    lookup = lookupFoodAndReply(bot, trigger, replyFmt, nutrient=CARB)


def lookupFoodAndReply(bot, trigger, replyFmt, nutrient=CALORIE):
    foodName = trigger.group(2)
    if not foodName:
        return False

    # First, let's just try to find the user's whole request
    res = foodQuery(["%s%%" % foodName], nutrient=nutrient)

    if not res:
        # Then, let's try their query with a wildcard in front, too
        res = foodQuery(["%%%s%%" % foodName], nutrient=nutrient)

    if not res:
        # look for anything that matches all terms
        foodNames = ["%%%s%%" % fn for fn in foodName.split(' ')]
        res = foodQuery(foodNames, nutrient=nutrient)

    if res is not False:
        bot.reply(replyFmt % res)
    else:
        bot.reply("No results.")


def foodQuery(foodNames, nutrient=CALORIE):
    conn = sqlite3.connect(os.path.dirname(__file__) + '/nutrients.db')
    c = conn.cursor()
    cmd = ''.join([
    '''
    SELECT Long_Desc, Nutr_Val 
    FROM food_des 
    JOIN nut_data 
        ON food_des.NDB_No = nut_data.NDB_No 
    WHERE
    '''
    ,' AND '.join(['Long_Desc LIKE ?'] * len(foodNames))
    ,''' AND Nutr_No = '%i' ''' % nutrient
    ,'ORDER BY length(Long_Desc)' # let's be naive and pick the shortest result
    ,'LIMIT 1;'
    ])

    c.execute(cmd, tuple(foodNames))

    foods = c.fetchall()
    if len(foods) is 0:
        return False
    else:
        return (foods[0][0], foods[0][1])
