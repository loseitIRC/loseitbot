from sopel import module

LBS_PER_KG = 2.2
M_PER_INCH = 2.54e-2
INCH_PER_FEET = 12

@module.commands("bmi\D(\d+\.?\d*)\s*(lb[s]?|kg[s]?)\s*(\d+'[\d.]*\"?|\d+\.?\d*\s*(c?m))\s*")
@module.example("bmi 200lb 5'11")
def bmi(bot, trigger):
    """ Calculate user's bmi, supports lb,kg,m,cm,ft'in" """
    weight, weightunit, height, heightunit = trigger.groups()[1:5]

    print(trigger.groups())
    print(weight)
    print(float(weight))
    if weightunit.startswith("lb"):
        weight = float(weight) / LBS_PER_KG
    elif weightunit.startswith("kg"):
        weight = float(weight)

    print("%s kg" % weight)

    if heightunit is None and height.find("'") > -1:
        ft, inches = [float(qty.replace("\"","")) for qty in height.split("'")[0:2]]
        height = (ft*INCH_PER_FEET + inches) * M_PER_INCH
    elif heightunit.startswith("cm"):
        height = float(height[:-2])/100
    elif heightunit.startswith("m"):
        height = float(height[:-1])
    
    print("%s m" % height)

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

