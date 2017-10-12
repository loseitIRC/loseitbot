from sopel import module
import re

LBS_PER_KG = 2.2
M_PER_INCH = 2.54e-2
INCH_PER_FEET = 12


def extractHeight(cmd):
    return re.search("(\d+'[\d.]*\"?|\d+\.?\d*\s*(c?m))", cmd, re.IGNORECASE)

def extractWeight(cmd):
    return re.search("(\d+\.?\d*)\s*(lb[s]?|kg[s]?)", cmd, re.IGNORECASE)

@module.commands("bmi")
@module.example("bmi 200lb 5'11")
def bmi(bot, trigger):
    """ Calculate user's BMI, supports lb,kg,m,cm,ft'in" """
    if not trigger.group(2):
        return bot.say("E.g.: !bmi 200lb 5'11\"")

    cmd = ' '.join(x for x in trigger.groups()[1:] if x is not None)

    weightgrps = extractWeight(cmd)
    if weightgrps is None or len(weightgrps.groups()) < 2:
        return bot.say("Must specify both a weight and a unit (lb, kg). E.g. !bmi 5'11\" 200 lbs")
    weight, weightunit = weightgrps.groups()

    heightgrps = extractHeight(cmd)
    if heightgrps is None or len(heightgrps.groups()) < 2:
        return bot.say("Must specify both a height and a unit (m, cm, ft'in\"). E.g. !bmi 5'11\" 200 lbs")
    height, heightunit = heightgrps.groups()

    if weightunit.startswith("lb"):
        weight = float(weight) / LBS_PER_KG
    elif weightunit.startswith("kg"):
        weight = float(weight)

    if heightunit is None and height.find("'") > -1:
        ft, inches = [float(qty.replace("\"","")) if qty is not '' else 0 for qty in height.split("'")[0:2]]
        height = (ft*INCH_PER_FEET + inches) * M_PER_INCH
    elif heightunit.startswith("cm"):
        height = float(height[:-2])/100
    elif heightunit.startswith("m"):
        height = float(height[:-1])
    
    bmi = weight/(height**2)

    if bmi < 18.5:
        bmiclass = ", underweight"
    elif bmi > 18.5 and bmi <= 24.9:
        bmiclass = ", normal"
    elif bmi > 24.9 and bmi <= 29.9:
        bmiclass = ", overweight"
    elif bmi > 29.9 and bmi <= 34.9:
        bmiclass = ", obese, class I"
    elif bmi > 34.9 and bmi <= 39.9:
        bmiclass = ", obese, class II"
    elif bmi > 39.9 and bmi <= 49.9:
        bmiclass = ", obese, class III"
    elif bmi > 49.9 and bmi <= 59.9:
        bmiclass = ", obese, class IV"
    elif bmi > 59.9:
        bmiclass = ", obese, class V"
    else:
        bmiclass = ""

    bot.reply("%.1f%s" % (bmi, bmiclass))

