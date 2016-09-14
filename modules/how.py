from sopel import module
import random

@module.commands("how(\s?many|\s?much)?")
@module.example("!how much spam")
def howmany(bot, trigger):
    """ Ask how many/how much of something """
    thing = trigger.group(3)
    if thing is not None:
        thing = ' ' + thing.split(" ")[0]
        if thing[-1].isalpha() and thing[-1] is not 's':
            thing += 's'
    else:
        thing = ''
    bot.reply("%i%s" % (int(random.random()*1000),thing))
