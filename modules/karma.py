import sopel
from sopel import module
import random

def setup(bot):
    if not bot.memory.contains('karma'):
        bot.memory['karma'] = sopel.tools.SopelMemory()

@module.commands('karma')
def getKarma(bot, trigger):
    """ Show karma for a given username """
    who = trigger.group(2).strip()
    whokey = who.lower()
    if whokey not in bot.memory['karma']:
        bot.memory['karma'][whokey] = 0
    else:
        pass
    bot.reply("%s has %i karma" % (who, bot.memory['karma'][whokey]))


@module.rule('(\w+)[:,]?\s*(\+\+|--)')
@module.require_chanmsg()
@module.rate(60)
def addKarma(bot, trigger):
    who = trigger.group(1).strip()
    whokey = who.lower()
    whoshere = [str(s).lower() for s in bot.privileges[trigger.sender]]

    if trigger.group(2) == "++":
        karma_adj = 1
    elif trigger.group(2) == "--":
        karma_adj = -1
    else:
        karma_adj = 0
    

    if who == str(trigger.user) or who not in whoshere:
        return False

    if whokey not in bot.memory['karma']:
        bot.memory['karma'][whokey] = 0 + karma_adj
    else:
        bot.memory['karma'][whokey] += karma_adj

