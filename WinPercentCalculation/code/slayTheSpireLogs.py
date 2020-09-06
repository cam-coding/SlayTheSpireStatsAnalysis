import json
import os

def openJson(directory, character):
    data_list = []
    wins = 0
    total = 0
    fileName = "C:\\Users\\Cam\\Desktop\\SlayTheSpireTinkering\\output\\" + character + ".csv"

    with open(fileName, 'w+') as output:
        for file in os.listdir(directory):
            json_path = os.path.join(directory, file)
            with open(json_path) as f:
                json_data = json.load(f)
                data_list.append(json_data)
                if json_data['ascension_level'] == 15:
                    if (json_data['victory']) or (json_data['floor_reached'] > 51):
                        wins = wins + 1
                    total = total + 1
                    percent = wins/(total)
                    output.write(str(round(percent, 2)) + ',')

defect = 'C:\\Users\\Cam\\Desktop\\SlayTheSpireTinkering\\runs\\DEFECT', "defect"
ironclad = 'C:\\Users\\Cam\\Desktop\\SlayTheSpireTinkering\\runs\\IRONCLAD', "ironclad"
silent = 'C:\\Users\\Cam\\Desktop\\SlayTheSpireTinkering\\runs\\THE_SILENT', "silent"
watcher = 'C:\\Users\\Cam\\Desktop\\SlayTheSpireTinkering\\runs\\WATCHER', "watcher"

characters = [defect, ironclad, silent, watcher]

for character in characters:
    openJson(character[0], character[1])
print("done1")