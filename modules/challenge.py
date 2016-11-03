from sopel import module

@module.commands('challenge')
@module.example('!challenge or (admin only) !challenge new text')
def challenge(bot, trigger):
    """ Get information about the current #loseit challenge """
    if trigger.group(2) and trigger.admin:
        try:
            with open(bot.config.homedir + '/challenge.txt', 'w') as f:
                f.write(trigger.group(2))
                bot.say("New message saved.")
        except:
            bot.say("Something went wrong.")
    elif not trigger.group(2):
        if trigger.sender[0] is "#" and not trigger.sender.startswith("#loseit"):
            return False

        try:
            with open(bot.config.homedir + '/challenge.txt') as f:
               bot.say(f.readline())
        except:
            bot.say("Can't find challenge.txt")
