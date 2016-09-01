from sopel import module
import random

TRIGGER_PROBABILITY = 0.3

@module.rule('trigger')
def triggerwarning(bot, trigger):
    if random.random() < TRIGGER_PROBABILITY:
        bot.say("TRIGGER WARNING")
