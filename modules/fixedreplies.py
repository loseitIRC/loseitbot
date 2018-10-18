from sopel import module

commands = {
    '100' : 'What 100 calories looks like: https://imgur.com/a/y8Hnb'
    ,'200' : 'What 200 calories looks like: www.wisegeek.com/what-does-200-calories-look-like.htm'
    ,'2000' : 'What 2000 calories look like: http://www.nytimes.com/interactive/2014/12/22/upshot/what-2000-calories-looks-like.html'
    ,'cooking' : 'Recipes and other curated cooking suggestions: https://goo.gl/lF64F3'
    ,'crossword' : 'https://www.nytimes.com/crosswords/game/mini'
    ,'docs' : 'https://loseitirc.github.io/loseitdocs/'
    ,'ed' : ' http://www.cdc.gov/nccdphp/dnpa/nutrition/pdf/r2p_energy_density.pdf'
    ,'exchange' : 'Join our holiday gift exchange! Sign-ups open through Nov 30, ship by Dec 18, available here: https://goo.gl/forms/wPacZsiLi55p3oEF2'
    ,'faq' : 'https://loseitirc.github.io/loseitdocs/faq.html'
    ,'flair' : 'Instructions for /r/loseit flair: https://www.reddit.com/r/loseit/wiki/faq#wiki_how_do_i_update_my_flair.3F'
    ,'flowchart' : 'The calorie counting flowchart: http://i.imgur.com/Nn04Cfs.png'
    ,'hackdiet' : 'The Hacker\'s Diet ebook: https://www.fourmilab.ch/hackdiet/e4/'
    ,'harsh' : 'http://4chanfit.wikia.com/wiki/Harsh\'s_Worksheet_(WIP)'
    ,'keywest' : '#loseit will be going to Key West in Jan 2018: https://goo.gl/PMIHX4'
    ,'metabolism' : 'https://www.reddit.com/r/fatlogic/comments/2i6oa3/can_you_actually_break_your_metabolism/ckzboth'
    ,'mfp' : 'https://www.myfitnesspal.com'
    ,'nwcr' : 'http://www.nwcr.ws/'
    ,'protein' : 'Consumption of 0.6-1.0 g/lb protein (along with lifting) minimizes muscle loss: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2858200/'
    ,'recipes' : 'Recipes and other curated cooking suggestions: https://goo.gl/lF64F3'
    ,'source' : 'https://github.com/loseitIRC/loseitbot'
    ,'ss': 'http://liamrosen.com/fitness.html'
    ,'subfaq' : 'https://www.reddit.com/r/loseit/wiki/faq'
    ,'trendweight' : 'https://trendweight.com/demo/ (see also https://www.fourmilab.ch/hackdiet/e4/pencilpaper.html)'
    ,'tdee': 'https://loseitirc.github.io/tdeecalc/'
    ,'usda' : 'https://ndb.nal.usda.gov/ndb/search/list'
    ,'visualbmi' : 'https://loseitirc.github.io/visualbmi/'
    ,'water' : 'http://web.archive.org/web/20131114201153/http://www.scientificamerican.com/article.cfm?id=eight-glasses-water-per-day'
    ,'whatwillilooklike' : 'http://visualbmi.com/'
}

patterns = {
    'NSV\?': 'NSV means non-scale victory.  See https://www.reddit.com/r/loseit/wiki/faq'
    ,'.*NSV mean\?': 'NSV means non-scale victory.  See https://www.reddit.com/r/loseit/wiki/faq'
    ,'GW\?': 'GW means goal weight.  See https://www.reddit.com/r/loseit/wiki/faq'
    ,'.*GW mean\?': 'GW means goal weight.  See https://www.reddit.com/r/loseit/wiki/faq'
}


#@module.commands(*commands.keys())
#@module.example('.' + ', .'.join(commands.keys()))
#def linkreply(bot, trigger):
#    bot.reply(commands[trigger.group(1).lower()])

def spontaneous_reply(bot, trigger):
    bot.say(patterns[trigger.match.re.pattern])

for pattern in patterns.keys():
    module.rule(pattern)(spontaneous_reply)

def link_reply(bot, trigger):
    bot.reply(commands[trigger.group(1).lower()])

for command in commands.keys():
    module.commands(command)(link_reply)
