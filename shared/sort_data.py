import json

oldFile = open("../portal04_solo_printed/data.json")
old_raw_data = json.load(oldFile)
newFile = open("data.json", 'r+')

sorted = {}

for set in old_raw_data['data']:
    p = set['prompt']
    r = set['response']
    if p in sorted:
        sorted[p].append(r)
    else: 
        sorted[p] = [r]


json.dump(sorted, newFile, indent = 4)