import json

f= open('211119_154638_R.json', 'r', encoding='utf-16-le')

data = json.load(f)

print(data['sessionResult']['leaderBoardLines'])

print('\n\n\n\n\n')

entrylist = {'entries' : [],
            'forceEntryList' : 1}


print(len(data['sessionResult']['leaderBoardLines']))

i = 0

# Change this to change the type of reverse grid (top 8/12 reverse grid etc).
# 0 to disable
# use a large number (> number of cars) to enable full reverse grid
reverse_grid_no = 0

cars = data['sessionResult']['leaderBoardLines']
grid_size = len(cars)

for car in cars:
    print(data['sessionResult']['leaderBoardLines'][i]['car']['drivers'][0]['lastName'])

    grid_position = i + 1

    reverse_grid_no = 0

    if grid_position <= reverse_grid_no:
        grid_position = reverse_grid_no - i
    
    if (data['sessionResult']['leaderBoardLines'][i]['car']['cupCategory'] == 0):
        entrylist['entries'].append(
            {
                'drivers' : [{
                    'firstName' : data['sessionResult']['leaderBoardLines'][i]['car']['drivers'][0]['firstName'],
                    'lastName' : data['sessionResult']['leaderBoardLines'][i]['car']['drivers'][0]['lastName'],
                    'shortName' : data['sessionResult']['leaderBoardLines'][i]['car']['drivers'][0]['shortName'],
                    'playerID' : data['sessionResult']['leaderBoardLines'][i]['car']['drivers'][0]['playerId'],
                    'driverCategory' : 3}
                ],
                'raceNumber' : data['sessionResult']['leaderBoardLines'][i]['car']['raceNumber'],
                "forcedCarModel": data['sessionResult']['leaderBoardLines'][i]['car']['carModel'],
                "defaultGridPosition" : grid_position,
                "overrideDriverInfo": 1,
                "isServerAdmin": 0
            }
        )
    else:
        entrylist['entries'].append(
            {
                'drivers' : [{
                    'firstName' : data['sessionResult']['leaderBoardLines'][i]['car']['drivers'][0]['firstName'],
                    'lastName' : data['sessionResult']['leaderBoardLines'][i]['car']['drivers'][0]['lastName'],
                    'shortName' : data['sessionResult']['leaderBoardLines'][i]['car']['drivers'][0]['shortName'],
                    'playerID' : data['sessionResult']['leaderBoardLines'][i]['car']['drivers'][0]['playerId'],
                    'driverCategory' : data['sessionResult']['leaderBoardLines'][i]['car']['cupCategory'] - 2}
                ],
                'raceNumber' : data['sessionResult']['leaderBoardLines'][i]['car']['raceNumber'],
                "forcedCarModel": data['sessionResult']['leaderBoardLines'][i]['car']['carModel'],
                "defaultGridPosition" : grid_position,
                "overrideDriverInfo": 1,
                "isServerAdmin": 0
            }
        )

    i = i + 1

o_file = open('entrylist_race2.json','w', encoding='utf-16-le')

o_file.write(json.dumps(entrylist, indent=4, sort_keys=True))

f.close()