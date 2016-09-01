from sopel import module

keywords = {
    'tdee': 'https://loseitirc.github.io/tdeecalc/',
    'ss': 'http://liamrosen.com/fitness.html',
    'docs' : 'https://github.com/loseitIRC/loseitdocs',
    'source' : 'https://github.com/loseitIRC/loseitbot'
}

@module.commands(*keywords.keys())
@module.example('.' + ', .'.join(keywords.keys()))
def linkreply(bot, trigger):
    bot.reply(keywords[trigger.group(1)])

@module.rule(".*bad bot\W?")
def whydontyouloveme(bot, trigger):
    bot.say(":[")
