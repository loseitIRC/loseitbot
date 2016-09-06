from sopel import module
import random

@module.commands('who', 'whose')
def who(bot, trigger):
    """ Choose from users in this channel """
    # Ideally this should use bot.channels[trigger.sender].users, but it
    # seems that list is not actually properly kept up to date...
    whoIsHere = list(bot.privileges[trigger.sender].keys())
    who = random.choice(whoIsHere)
    bot.reply(str(who))
