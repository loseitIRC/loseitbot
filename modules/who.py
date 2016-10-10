from sopel import module
import random
import re

@module.commands('who', 'whose')
def who(bot, trigger):
    """ Choose from users in this channel """
    # Ideally this should use bot.channels[trigger.sender].users, but it
    # seems that list is not actually properly kept up to date...
    if re.match(r'loves snoopjedi', trigger.group(2).lower()):
        bot.reply("No one loves SnoopJeDi")
    else:
        whoIsHere = list(bot.privileges[trigger.sender].keys())
        who = random.choice(whoIsHere)
        bot.reply(str(who))
