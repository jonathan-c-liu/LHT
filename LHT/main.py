# Open file of games and format into dictionary
games = open(r"2019 Home Schedule")
dict_games = dict()
day = games.readline()

while day:
    key = day[0:2]+day[3:5]
    dict_games[key] = (day[9:11]+day[12:14])
    day = games.readline()

games.close()

# Testing if it's gameday
gameDay = False
if date == dict_games:
    gameDay = True

# Acting on whether or not it's gameday
if gameDay == False:
    print("No change to Schedule")
else:
    print("Optimized Schedule From ")
    print (startTime + offset) + " to " + (offset+range)
    display(bus_times)
