from sopel import module
import random

responses = [
    "yes",
    "no"
]

@module.commands("8")
@module.example(".8 is this the real life?")
def howmany(bot, trigger):
    """ Ask the bot a yes or no question """
    bot.reply(random.choice(responses))
