import json

f = open('signups.json', 'r')
clsFile = open('classes.json', 'r')
# API Endpoint - https://indianracingcommunity.co.in/api/signups/{season_id}
# Requires Authorization Header
# Returns [{id, drivername, discord_id, racenumber, steam_id, attendance, car}, {...} ...]

data = json.load(f)
classData = json.load(clsFile)

entrylist = {'entries': [],
             'forceEntryList': 1}

i = 0

racenumbers = []
racenumberstemp = []
shortnames = []

# TODO: Check if id is null, if so skip and print Username<@discord_id> back to Discord -> Missing from website
# TODO: Check if driver is in classes.json, else print Username<@discord_id> back to Discord -> Missing a classes
driverInPro = classData['pro']['drivers']
driverInSilver = classData['silver']['drivers']
driverInAm = classData['am']['drivers']

for driver in data:
    drivername = driver['UserName']
    shortname = driver['UserName'][:3].upper()
    racenumber = driver['drivernumber']
    userid = int(driver['user_id'])

    if racenumber in racenumbers:
        for x in range(1,1000):
            if x not in racenumberstemp:
                racenumberstemp.append(x)
                racenumber = x
                break

    if shortname in shortnames:
        print(shortname + ' is already taken')

    if userid in driverInPro:
        driverCat = 1
    elif userid in driverInSilver:
        driverCat = 3
    elif userid in driverInAm:
        driverCat = 2
    else:
        driverCat = 2
        print(drivername + ' not assigned a class, defaulted to AM')

    racenumbers.append(racenumber)
    shortnames.append(shortname)

    entrylist['entries'].append(
        {
            'drivers': [{
                'firstName': "",
                'lastName': drivername,
                'shortName': shortname,
                'playerID': 'S' + driver['Steam'],
                'driverCategory': int(driverCat)
            }
            ],
            'raceNumber': int(racenumber),
            "forcedCarModel": int(driver['Car Value 1']),
            "defaultGridPosition": -1,
            "overrideDriverInfo": 1,
            "isServerAdmin": 0
        }
    )

    i = i + 1

o_file = open('entrylist_temp.json', 'w', encoding='utf-16-le')

o_file.write(json.dumps(entrylist, indent=4, sort_keys=True))

f.close()