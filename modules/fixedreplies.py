from sopel import module

commands = {
    '200' : 'What 200 calories look like: www.wisegeek.com/what-does-200-calories-look-like.htm'
    ,'2000' : 'What 2000 calories look like: http://www.nytimes.com/interactive/2014/12/22/upshot/what-2000-calories-looks-like.html'
    ,'docs' : 'https://loseitirc.github.io/loseitdocs/'
    ,'ed' : ' http://www.cdc.gov/nccdphp/dnpa/nutrition/pdf/r2p_energy_density.pdf'
    ,'faq' : 'https://loseitirc.github.io/loseitdocs/faq.html'
    ,'flowchart' : 'The calorie counting flowchart: http://i.imgur.com/Nn04Cfs.png'
    ,'harsh' : 'http://4chanfit.wikia.com/wiki/Harsh\'s_Worksheet_(WIP)'
    ,'metabolism' : 'https://www.reddit.com/r/fatlogic/comments/2i6oa3/can_you_actually_break_your_metabolism/ckzboth'
    ,'mfp' : 'https://www.myfitnesspal.com'
    ,'source' : 'https://github.com/loseitIRC/loseitbot'
    ,'ss': 'http://liamrosen.com/fitness.html'
    ,'subfaq' : 'https://www.reddit.com/r/loseit/wiki/faq'
    ,'tdee': 'https://loseitirc.github.io/tdeecalc/'
    ,'usda' : 'https://ndb.nal.usda.gov/ndb/search/list'
    ,'visualbmi' : 'http://visualbmi.com/'
    ,'water' : 'http://web.archive.org/web/20131114201153/http://www.scientificamerican.com/article.cfm?id=eight-glasses-water-per-day'
    ,'whatwillilooklike' : 'http://visualbmi.com/'
}

patterns = {
    '^!\s*$': '¡'
    ,'.*>\s*implying.*': '>implying implication'
    ,'.*\Walot': 'http://i.imgur.com/C4Oao7G.png'
    ,'.*\Wmagic': 'https://i.imgur.com/YsbKHg1.gif'
    ,'NSV\?': 'NSV means non-scale victory.  See https://www.reddit.com/r/loseit/wiki/faq'
    ,'NSV mean\?': 'NSV means non-scale victory.  See https://www.reddit.com/r/loseit/wiki/faq'
    ,'GW\?': 'GW means goal weight.  See https://www.reddit.com/r/loseit/wiki/faq'
    ,'GW mean\?': 'GW means goal weight.  See https://www.reddit.com/r/loseit/wiki/faq'
    ,'.*smoke weed.*': 'erryday.'
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


@module.rule(".*$nickname.*")
def stoicAction(bot, trigger):
    if 'intent' in trigger.tags.keys() and trigger.tags['intent'] == 'ACTION':
        bot.action("stares at " + str(trigger.nick))
        

@module.rule(".*bad bot(\W|$)")
def whydontyouloveme(bot, trigger):
    bot.say(":[")


@module.rule(".*good bot(\W|$)")
def senpaiNoticedMe(bot, trigger):
    bot.say(":]")
