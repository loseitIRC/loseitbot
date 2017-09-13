from sopel import module
from sopel.config.types import StaticSection, ValidatedAttribute, ListAttribute
import os

class DefconSection(StaticSection):
    channels = ListAttribute('channels')
    state = ValidatedAttribute('state', int, default=0)

def configure(config):
    config.define_section('defcon', DefconSection)

def setup(bot):
    bot.config.define_section('defcon', DefconSection)
    try:
        fn = os.path.join(bot.config.core.homedir, 'defcon_nowarn_users.cfg')
        with open(fn, 'r') as f:
            bot.config.defcon.nowarn_users = set(f.read())
            import q; q.q(bot.config.defcon.nowarn_users)
    except FileNotFoundError:
        bot.config.defcon.nowarn_users = set()

@module.require_admin
@module.commands('defcon')
@module.priority('high')
def defcon(bot, trigger):
    """ 
    Set Defcon on or off.
    Defcon On = cmode +M - registered only, tell newcomers
    Defcon Off = cmode -M - all talk
    """
    if trigger.group(2):
        state = trigger.group(2)
        try:
            bot.config.defcon.state = int(state)
        except ValueError:
            bot.reply("Value must be a valid base10 integer. E.g. !defcon 1")
            return False
    bot.reply("Current Defcon: {}".format(bot.config.defcon.state))

def get_nowarn_users(bot):
    """ Get list of lowercase usernames to never warn about defcon """
    return {u.lower() for u in bot.config.defcon.nowarn_users}

def add_nowarn_user(bot, user):
    nowarn_users = bot.config.defcon.nowarn_users
    nowarn_users.add(user)
    fn = os.path.join(bot.config.core.homedir, 'defcon_nowarn_users.cfg')
    with open(fn, 'w') as f:
        f.write(repr(nowarn_users))
        

@module.event('JOIN')
@module.rule('.*')
def welcome(bot, trigger):
  """ Welcome users joining while channel is in defcon """
  defcon = bot.config.defcon.state
  nowarn_users = get_nowarn_users(bot)
  defconchans = bot.config.defcon.channels
  chan = trigger.sender
  user = str(trigger.nick).lower()
  if defcon and str(chan) in defconchans and user not in nowarn_users:
      bot.notice("Welcome to {channel}! "
                "Please register your nickname (or identify yourself with "
                "services) to speak. Type /msg NickServ HELP for details. "
                "Reply with !nowarn if you'd prefer not to see this message."
                .format(channel=chan), 
                trigger.nick)

@module.require_privmsg
@module.commands("nowarn")
def disablewarning(bot, trigger):
    nowarn_users = get_nowarn_users(bot)
    user = str(trigger.nick).lower()
    if user not in nowarn_users:
        add_nowarn_user(bot, user)
        bot.reply("Okay, I won't warn you about moderated channels on join.")
