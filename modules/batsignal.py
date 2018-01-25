from sopel import module

MINUTE = 60

channellist = ['#loseit', '#loseit-mods']
recipients =  ['SnoopJeDi', 'chaoticgeek', 'Nasty_Woman', 'wiggly', 'Bob_McBob', 
               'LikeABox', 'TKT', 'Veritay']

@module.rate(channel=5*MINUTE)
@module.commands('ops')
def alert_ops(bot, trigger):
    """ Alert operators that someone in the channel has requested their presence """
    if not trigger.sender in channellist:
        return False
    
    for op in recipients:
        bot.say('User {nick} has requested an operator in {channel}, saying: "{msg}"'.format(
            channel=trigger.sender,
            nick=trigger.nick,
            msg=trigger.match.string),
            op
        )
    
    bot.notice("The channel operators have been notified of your request.", trigger.nick)
