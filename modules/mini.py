from sopel import module
import datetime

scores = {}
numScores = 3

@module.commands("mini(\s*\d{0,2}:\d{2})?")
@module.example("!mini or !mini 1:30")
def mini(bot, trigger):
  if trigger.group(2): # Will only be triggered when there is a time present
    today = datetime.date.today().strftime('%Y%m%d')
    time = trigger.group(2).strip()
    if time.startswith(":"):
      time = "0%s" % time
    todaysScores = scores.get(today, None)
    if todaysScores is None:
      scores.clear()
      scores[today] = {}
      todaysScores = scores.get(today, None)
    sender = trigger.nick
    if todaysScores.get(sender, None) is None:
      todaysScores[sender] = time
      bot.reply('Your time has been added!')
    else:
      bot.reply('You have already submitted your time today! Come back tomorrow')
  else:
    bot.reply('https://www.nytimes.com/crosswords/game/mini')

@module.commands('minileaderboard')
@module.example('!minileaderboard')
def minileaderboard(bot, trigger):
  today = datetime.date.today().strftime('%Y%m%d')
  todaysScores = scores.get(today, None)
  sender = trigger.nick
  if todaysScores is None:
    bot.reply('There are no scores recorded for the day. Be the first one to complete the mini!')
    return
  sortedScores = sorted(todaysScores.items(), key=lambda kv: (kv[1],kv[0]))
  topN = [x for x in sortedScores[:numScores]]
  response = ', '.join(["%s finished in %s" % (x[0], x[1]) for x in topN])
  selfScore = todaysScores.get(sender, None)
  if selfScore is not None and (sender, selfScore) not in [x for x in topN]:
    response = "%s, and you finished in %s." % response, selfScore
  response += " (Top %d times shown)" % numScores
  bot.reply(response)

