from sopel import module

@module.require_chanmsg
@module.commands('defcon')
@module.priority('high')
def defcon(bot, trigger):
    """ Set Defcon on or off.
    Defcon On = cmode +M - registered only, tell newcomers
    Defcon Off = cmode -M - all talk
    """
    if bot.privileges[trigger.sender][bot.nick] < module.HALFOP:
        return bot.reply("I'm not a channel operator!")
    if not trigger.admin:
      bot.reply("You're not my IRC Supervisor!")
    else:
      if trigger.group(2):
        state = bool(trigger.group(2))
        modeset = "+M" if state else "-M"
        bot.config.defcon.state = state
        bot.write(("MODE", trigger.sender, modeset))
        bot.reply("Defcon Set: {}".format(trigger.group(2)))
      else
        bot.reply("Must specify defcon boolean")

@module.event("JOIN")
def welcome(bot, trigger):
  """ Welcome users joining while channel is in defcon """
  if bot.config.defcon.state:
    bot.reply("This channel is currently under moderation. \
Please register your nickname (or identify yourself with services) to speak. \
See `/msg NickServ HELP` for details", notice=True)
  else:
    pass
