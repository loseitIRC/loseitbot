import sopel
from sopel import module
import json
from geopy.geocoders import GoogleV3

geocoder = GoogleV3()
mapurl = "http://jamesgerity.com/loseit/map"

@module.commands('map')
@module.example('!map Springfield, IL')
def loseitmap(bot, trigger):
    """ Give link to user map, or set user location """
    if trigger.group(2) is None:
        bot.reply("#loseit user map (use !map Anywhere, CA to add yourself): %s" % mapurl)
    else:
        host = trigger.host
        nick = trigger.nick
        with open('/var/www/html/loseit/map/users.json', 'r+') as f:
            where = trigger.group(2)
            userdb = json.load(f)
            locs = geocoder.geocode(where, exactly_one=False)
            print(locs)
            if locs is None:
                bot.reply("Can't find that location.")
                return False
            if len(locs) > 1:
                bot.reply("Ambiguous location, please be more specific")
                return False
            else:
                userdb[host] = {"username" : nick, 
                                "loc" : [locs[0].latitude, locs[0].longitude]}
                bot.reply("Location set to %s" % locs[0].address)
            f.seek(0)
            f.write(json.dumps(userdb, indent=2))
            f.truncate()

