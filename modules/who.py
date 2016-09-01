from sopel import module
import random

@module.commands('who')
def who(bot, trigger):
    # Ideally this should use bot.channels[trigger.sender].users, but it
    # seems that list is not actually properly kept up to date...
    whoIsHere = list(bot.privileges[trigger.sender].keys())
    who = random.choice(whoIsHere)
    bot.reply(str(who))
