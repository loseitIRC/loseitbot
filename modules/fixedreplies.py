from sopel import module

commands = {
    '200' : 'What 200 calories look like: www.wisegeek.com/what-does-200-calories-look-like.htm'
    ,'2000' : 'What 2000 calories look like: http://www.nytimes.com/interactive/2014/12/22/upshot/what-2000-calories-looks-like.html'
    ,'docs' : 'https://loseitirc.github.io/loseitdocs/'
    ,'ed' : ' http://www.cdc.gov/nccdphp/dnpa/nutrition/pdf/r2p_energy_density.pdf'
    ,'faq' : 'https://loseitirc.github.io/loseitdocs/faq.html'
    ,'flair' : 'Instructions for /r/loseit flair: https://www.reddit.com/r/loseit/wiki/faq#wiki_how_do_i_update_my_flair.3F'
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
    'NSV\?': 'NSV means non-scale victory.  See https://www.reddit.com/r/loseit/wiki/faq'
    ,'NSV mean\?': 'NSV means non-scale victory.  See https://www.reddit.com/r/loseit/wiki/faq'
    ,'GW\?': 'GW means goal weight.  See https://www.reddit.com/r/loseit/wiki/faq'
    ,'GW mean\?': 'GW means goal weight.  See https://www.reddit.com/r/loseit/wiki/faq'
}


@module.commands(*commands.keys())
@module.example('.' + ', .'.join(commands.keys()))
def linkreply(bot, trigger):
    bot.reply(commands[trigger.group(1).lower()])

def spontaneousReply(bot, trigger):
    bot.say(patterns[trigger.match.re.pattern])

# This decorates spontaneousReply for every pattern available
for pattern in patterns.keys():
    module.rule(pattern)(spontaneousReply)
