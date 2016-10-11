from sopel import module
import random
import re

responses = [
    "yes",
    "no"
]

@module.commands("8")
@module.example("!8 is this the real life?")
def howmany(bot, trigger):
    """ Ask the bot a yes or no question """
    if trigger.group(2) and trigger.group(2).lower().startswith("are you sure"):
        bot.reply("Did I stutter?")
    elif trigger.group(2) and re.match(r'loves?[\s]+snoopjedi', trigger.group(2).lower()):
        bot.reply("No one loves SnoopJeDi")
    else:
        bot.reply(random.choice(responses))
