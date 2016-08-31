from sopel import module
import random

@module.commands('who')
def echo(bot, trigger):
    who = random.choice(list(bot.channels[trigger.sender].users.values()))
    bot.reply(who.nick)
