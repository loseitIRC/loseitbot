from sopel import module

KM_PER_MILE = 1.60934

@module.commands("km")
@module.example("km 26.2")
def miles_to_km(bot, trigger):
    """ Convert miles to km """

    miles = float(trigger.group(2))
    if miles is not None:
        bot.reply("%.1f miles is equal to %.1f km" % (miles, miles * KM_PER_MILE))


@module.commands("mi")
@module.example("mi 5")
def km_to_miles(bot, trigger):
    """ Convert km to miles """

    km = float(trigger.group(2))
    if km is not None:
        bot.reply("%.1f km is equal to %.1f miles" % (km, km / KM_PER_MILE))

