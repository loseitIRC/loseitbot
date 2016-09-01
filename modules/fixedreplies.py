from sopel import module

commands = {
    'tdee': 'https://loseitirc.github.io/tdeecalc/'
    ,'ss': 'http://liamrosen.com/fitness.html'
    ,'docs' : 'https://github.com/loseitIRC/loseitdocs'
    ,'source' : 'https://github.com/loseitIRC/loseitbot'
    ,'faq' : 'https://www.reddit.com/r/loseit/wiki/faq'
    ,'usda' : 'http://www.nal.usda.gov/fnic/foodcomp/search/index.html'
}

patterns = {
    'NSV\?': 'NSV means non-scale victory.  See https://www.reddit.com/r/loseit/wiki/faq'
    ,'GW\?': 'GW means goal weight.  See https://www.reddit.com/r/loseit/wiki/faq'
}

@module.commands(*commands.keys())
@module.example('.' + ', .'.join(commands.keys()))
def linkreply(bot, trigger):
    bot.reply(commands[trigger.group(1)])


def spontaneousReply(bot, trigger):
    bot.say(patterns[trigger.match.re.pattern])

# This decorates spontaneousReply for every pattern available
for pattern in patterns.keys():
    module.rule(pattern)(spontaneousReply)

@module.rule(".*bad bot\W?")
def whydontyouloveme(bot, trigger):
    bot.say(":[")
