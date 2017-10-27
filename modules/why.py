from sopel import module

@module.commands("why")
@module.example("!why do you hate me?")
def why(bot, trigger):
    """ why something """
    bot.reply("because reasons")
