import sopel
from sopel import module
import random

@module.commands("or", "elif", "elseif")
@module.example("!or A or B or C")
def orfunc(bot, trigger):
    """ Choose from a list of things """
    things = trigger.group(2)
    if things is not None and type(things) is str:
        choice = random.choice(things.split(" or ")).rstrip("?")
        bot.reply("%s" % choice)
