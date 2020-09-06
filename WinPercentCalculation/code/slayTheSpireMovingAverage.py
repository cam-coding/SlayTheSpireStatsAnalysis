import json
import os

def movingAverage(length, runs):
    total = 0
    for run in runs:
        total = total + run
    return total/length

def openJson(directory, character):
    data_list = []
    length = 20
    movingAvg = [None] * length
    fileName = "C:\\Users\\Cam\\Desktop\\SlayTheSpireTinkering\\output\\" + character + "MovingAverage" + str(length) + ".csv"

    with open(fileName, 'w+') as output:
        i = 0
        write = False
        for file in os.listdir(directory):
            json_path = os.path.join(directory, file)
            with open(json_path) as f:
                json_data = json.load(f)
                data_list.append(json_data)
                if json_data['ascension_level'] == 15:
                    if (json_data['victory']) or (json_data['floor_reached'] > 51):
                        movingAvg[i] = 1
                    else:
                        movingAvg[i] = 0
                    
                    if (write):
                        #output.write(str(round(percent, 2)) + ',')
                        output.write(str(round(movingAverage(length, movingAvg), 2)) + ',')
                    i += 1
                    if (i == length):
                        write = True
                        i = 0

defect = 'C:\\Users\\Cam\\Desktop\\SlayTheSpireTinkering\\runs\\DEFECT', "defect"
ironclad = 'C:\\Users\\Cam\\Desktop\\SlayTheSpireTinkering\\runs\\IRONCLAD', "ironclad"
silent = 'C:\\Users\\Cam\\Desktop\\SlayTheSpireTinkering\\runs\\THE_SILENT', "silent"
watcher = 'C:\\Users\\Cam\\Desktop\\SlayTheSpireTinkering\\runs\\WATCHER', "watcher"

characters = [defect, ironclad, silent, watcher]

for character in characters:
    openJson(character[0], character[1])
print("done1")