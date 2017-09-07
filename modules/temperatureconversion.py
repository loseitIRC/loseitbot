from sopel import module

@module.commands("fa", "fahrenheit")
@module.example("fa 100")
def celsius_to_fahrenheit(bot, trigger):
    """ Convert Celsius to Fahrenheit """

    try:
        celsius = float(trigger.group(2))
    except ValueError:
        bot.reply("Could not understand input.  Please input the temperature in Celsius, e.g. !fa 100")
        return False

    if celsius is not None:
        bot.reply("%.1f degrees Celsius is equal to %.1f degrees Fahrenheit" % (celsius, (celsius * 1.8 + 32)))


@module.commands("ce", "celsius")
@module.example("ce 212")
def fahrenheit_to_celsius(bot, trigger):
    """ Convert Fahrenheit to Celsius """

    try:
        fahrenheit = float(trigger.group(2))
    except ValueError:
        bot.reply("Could not understand input.  Please input the temperature in Fahrenheit, e.g. !ce 100")
        return False

    if fahrenheit is not None:
        bot.reply("%.1f degrees Fahrenheit is equal to %.1f degrees Celsius" % (fahrenheit, (fahrenheit - 32) / 1.8))
