from sopel import module
import random

LBS_PER_KG = 2.2

equiv_weights = [
    (1, "Guinea Pig")
    ,(2, "rack of baby back ribs")
    ,(3, "average human brain")
    ,(4, "ostrich egg")
    ,(5, "Chihuahua")
    ,(6, "human skin")
    ,(8, "human head")
    ,(11, "average housecat")
    ,(12, "Bald Eagle")
    ,(15, "10 dozen large eggs")
    ,(16, "sperm whale brain")
    ,(20, "automobile tire")
    ,(25, "average 2 year old")
    ,(33, "cinder block")
    ,(36, "mid-size microwave")
    ,(40, "average human leg")
    ,(44, "elephant's heart")
    ,(50, "small bale of hay")
    ,(55, "5000 BTU air conditioner")
    ,(60, "elephants penis")
    ,(70, "Irish Setter")
    ,(77, "gold brick")
    ,(80, "World's Largest Ball of Tape")
    ,(100, "2 month old horse")
    ,(118, "complete Encyclopedia Britannica")
    ,(130, "newborn giraffe")
    ,(144, "average adult woman")
    ,(150, "complete Oxford English Dictionary")
    ,(187, "average adult male")
    ,(235, "Arnold Schwarzenegger")
    ,(300, "average football linebacker")
    ,(400, "Welsh pony")
]

@module.commands("equiv\D(\d+\.?\d*)\s*(lb[s]?|kg[s]?)\s*")
@module.example("equiv 200 lb")
def equiv_weight(bot, trigger):
    """ Give an equivalent of the input weight """
    origweight, weightunit = trigger.groups()[1:3]

    if weightunit.startswith("lb"):
        weight = float(origweight)
    elif weightunit.startswith("kg"):
        weight = float(origweight) * LBS_PER_KG

    
    equiv, name = random.choice(equiv_weights)
    while weight / equiv < 1:
        equiv, name = random.choice(equiv_weights)

    if weight/equiv > 1:
        name += "s"

    bot.reply("%.1f %s is equivalent to %.1f %s" % (float(origweight), weightunit, weight/equiv, name))
