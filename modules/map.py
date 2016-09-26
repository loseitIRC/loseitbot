import sopel
from sopel import module
import json
from geopy.geocoders import GoogleV3

geocoder = GoogleV3()
mapurl = "http://jamesgerity.com/loseit/map"

@module.commands('map')
def loseitmap(bot, trigger):
    """ Give link to user map, or set user location """
    if trigger.group(2) is None:
        bot.reply("#loseit user map: %s" % mapurl)
    else:
        who = trigger.nick
        with open('/var/www/html/loseit/map/users.json', 'r+') as f:
            where = trigger.group(2)
            userdb = json.load(f)
            locs = geocoder.geocode(where, exactly_one=False)
            print(locs)
            if len(locs) > 1:
                bot.reply("Ambiguous location, please be more specific")
            else:
                userdb[who] = [locs[0].latitude, locs[0].longitude]
                bot.reply("Location set to %s" % locs[0].address)
            f.seek(0)
            f.write(json.dumps(userdb))
            f.truncate()

