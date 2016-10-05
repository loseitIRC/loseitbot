from sopel import module
import subprocess

@module.commands("factor")
@module.example("!factor 42, !factor 6.0221409e23")
def factor(bot, trigger):
    try:
        # cast to float first to support scientific notation
        num = int(float(trigger.group(2)))
    except:
        bot.reply("Invalid input.")
        return False
    if num > 1e100 or num <= 1:
        return False

    response = "%s = " % num
    output = subprocess.check_output(['factor', str(num)]).decode("utf-8").replace("\n", "").split(": ")
    if len(output) < 2:
        return False
    output = output[1].split(' ')
    output = [int(n) for n in output]
    factors = []
    factorsused = []
    for f in output:
        if f not in factorsused:
            if output.count(f) != 1:
                fstring = "%i^%i" % (f, output.count(f))
            else:
                fstring = "%i" % f
            factors.append(fstring) 
            factorsused.append(f)

    response += ' * '.join(factors)
    bot.reply(response)
