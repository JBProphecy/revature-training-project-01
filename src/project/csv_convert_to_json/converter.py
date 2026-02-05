import csv, json

with open('revature-training-project-01/data/v1/raw/Forest_Fires_Data.csv', mode='r', encoding='utf-8') as csv_file:
    data = list(csv.DictReader(csv_file))

with open('revature-training-project-01/data/v1/raw/Forest_Fires_Data.json', mode='w') as json_file:
    json.dump(data, json_file, indent = 4)