from sopel import module

import requests

@module.commands("spew")
@module.example("spew")
def spew(bot, trigger):
    """ Spew random text using a markov chain (by calling upon loseit-markov.ml) """
    url = 'http://loseit-markov.ml'
    response = requests.get(url, timeout=5)
    if response.ok:
      bot.reply(response.text)
    else:
      bot.reply("Had trouble reading from %s, please try again or let tycoon177 know about this issue" % url)
