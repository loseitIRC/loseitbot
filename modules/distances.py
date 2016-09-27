from sopel import module

KM_PER_MILE = 1.60934

@module.commands("km")
@module.example("km 26.2")
def miles_to_km(bot, trigger):
    """ Convert miles to km """

    try:
        miles = float(trigger.group(2))
    except ValueError:
        bot.reply("Could not understand input.  Please input the distance in km, e.g. !km 26.2")
        return False

    if miles is not None:
        bot.reply("%.1f miles is equal to %.1f km" % (miles, miles * KM_PER_MILE))


@module.commands("mi")
@module.example("mi 5")
def km_to_miles(bot, trigger):
    """ Convert km to miles """

    # memes
    if trigger.group(2).lower().strip() == "sharona":
        bot.reply("https://www.youtube.com/watch?v=g1T71PGd-J0")
        return False

    try:
        km = float(trigger.group(2))
    except ValueError:
        bot.reply("Could not understand input.  Please input the distance in mi, e.g. !mi 5")
        return False

    if km is not None:
        bot.reply("%.1f km is equal to %.1f miles" % (km, km / KM_PER_MILE))

