from sopel import module
import random

@module.commands("or")
def howmany(bot, trigger):
    things = trigger.group(2)
    if things is not None and type(things) is str:
        choice = random.choice(things.split(" or "))
        bot.reply("%s" % choice)