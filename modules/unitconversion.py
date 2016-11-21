from sopel import module

LBS_PER_KG = 2.2
M_PER_INCH = 2.54e-2
INCH_PER_FEET = 12

@module.commands("kg\s*(\d+)(\s*lbs?)?")
@module.example("kg 200lb")
def kgtolb(bot, trigger):
    """ Convert lbs to kg """
    weight = trigger.group(2)

    lbs = float(weight) 
    kg = lbs / LBS_PER_KG

    bot.reply("%.1f lbs is %.1f kg" % (lbs, kg))


@module.commands("lbs?\s*(\d+)(\s*kgs?)?")
@module.example("lb 200 kg")
def lbtokg(bot, trigger):
    """ Convert kg to lbs """
    weight = trigger.group(2)

    kg = float(weight) 
    lbs = kg * LBS_PER_KG

    bot.reply("%.1f kg is %.1f lbs" % (kg, lbs))
