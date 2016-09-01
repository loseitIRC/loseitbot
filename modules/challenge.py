from sopel import module

@module.commands('challenge')
@module.example('.challenge')
def challenge(bot, trigger):
    if trigger.group(2) and trigger.admin:
        try:
            with open(bot.config.homedir + '/challenge.txt', 'w') as f:
                f.write(trigger.group(2))
                bot.say("New message saved.")
        except:
            bot.say("Something went wrong.")
    elif not trigger.group(2):
        try:
            with open(bot.config.homedir + '/challenge.txt') as f:
               bot.say(f.readline())
        except:
            bot.say("Can't find challenge.txt")
