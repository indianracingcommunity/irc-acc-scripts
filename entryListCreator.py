import json

f = open('signuplatest.json', 'r')
# API Endpoint - https://indianracingcommunity.co.in/api/signups/{season_id}
# Requires Authorization Header
# Returns [{id, drivername, discord_id, racenumber, steam_id, attendance, car}, {...} ...]

data = json.load(f)

entrylist = {'entries': [],
             'forceEntryList': 1}

i = 0

racenumbers = []
shortnames = []

# TODO: Check if id is null, if so skip and print Username<@discord_id> back to Discord -> Missing from website
# TODO: Check if driver is in classes.json, else print Username<@discord_id> back to Discord -> Missing a classes
for driver in data:
    drivername = driver['drivername']
    shortname = driver['drivername'][:3].upper()
    racenumber = driver['racenumber']

    if racenumber in racenumbers:
        print(drivername + ' has a clash of race number ' + racenumber)

    if shortname in shortnames:
        print(shortname + ' is already taken')

    racenumbers.append(racenumber)
    shortnames.append(shortname)

    entrylist['entries'].append(
        {
            'drivers': [{
                'firstName': "",
                'lastName': drivername,
                'shortName': shortname,
                'playerID': 'S' + driver['steam_id'],
                'driverCategory': 0
            }
            ],
            'raceNumber': int(racenumber),
            "forcedCarModel": int(driver['car']),
            "defaultGridPosition": -1,
            "overrideDriverInfo": 1,
            "isServerAdmin": 0
        }
    )

    i = i + 1

o_file = open('entrylist_temp.json', 'w', encoding='utf-16-le')

o_file.write(json.dumps(entrylist, indent=4, sort_keys=True))

f.close()