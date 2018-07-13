from sopel import module

LBS_PER_KG = 2.2
M_PER_INCH = 2.54e-2
INCH_PER_FEET = 12


@module.commands('cm\s+(\d+)\'(\d+"?)?')
@module.example("cm 5'11\"")
def feet_to_cm(bot, trigger):
    """ Convert imperial height to metric """
    feet = int(trigger.group(2))
    if len(trigger.groups()) > 2:
        inches = int(trigger.group(3).rstrip('"'))
    else:
        inches = 0

    cm = int(((inches + feet * INCH_PER_FEET) * M_PER_INCH) * 100)

    bot.reply("{:d}\'{:d}\" is {:d} cm".format(feet, inches, cm))
  

@module.commands("kgs?\s+(\d+(.\d+)?)(\s*lbs?)?")
@module.example("kg 200lb")
def kgtolb(bot, trigger):
    """ Convert lbs to kg """
    weight = trigger.group(2)

    lbs = float(weight) 
    kg = lbs / LBS_PER_KG

    bot.reply("%.1f lbs is %.1f kg" % (lbs, kg))


@module.commands("lbs?\s+(\d+(.\d+)?)(\s*kgs?)?")
@module.example("lb 200 kg")
def lbtokg(bot, trigger):
    """ Convert kg to lbs """
    weight = trigger.group(2)

    kg = float(weight) 
    lbs = kg * LBS_PER_KG

    bot.reply("%.1f kg is %.1f lbs" % (kg, lbs))
