import json

f = open('signuplatest.json', 'r')

data = json.load(f)

entrylist = {'entries': [],
             'forceEntryList': 1}

i = 0

racenumbers = []
shortnames = []

for driver in data:
    drivername = driver['UserName']
    shortname = driver['UserName'][:3].upper()
    racenumber = driver['drivernumber']

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
                'playerID': 'S' + driver['Steam'],
                'driverCategory': 0
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