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
    if not trigger.group(2):
        bot.reply(random.choice(responses))
        return
    else:
        text = trigger.group(2).lower()
    
    if text.startswith("are you sure"):
        bot.reply("Did I stutter?")
    if text.startswith("boobs?"):
        bot.reply("https://m.popkey.co/665a53/8q7oO_s-200x150.gif")
    elif re.match(r'loves?[\s]+snoopjedi', text):
        bot.reply("No one loves SnoopJeDi")
    elif re.match(r'butts?\??', text):
        bot.reply("Butts are great ( ͡° ͜ʖ ͡°) yay butts")
    elif trigger.group(2) and re.search(r'good\?+\s*$', trigger.group(2).lower()):
        bot.reply("Dunno what's good, but Zensei smells like Fresca")
    else:
        bot.reply(random.choice(responses))
