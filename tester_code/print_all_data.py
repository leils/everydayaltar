import sys, json, os, random, time
from pathlib import Path

#-------- shared utils access hack
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from shared import utils
printers = utils.setupPrinters()

#-------- JSON file loads for questions & responses
sharedPath = path + '/shared'
source_filename = os.path.join(sharedPath, 'source.json')
data_filename = os.path.join(sharedPath, "data.json")

responses = json.load(open(data_filename))

toPrint = []

for question in responses.keys():
    resp = responses[question]
    for r in resp: 
        toPrint.append([question, r])
        # utils.printToAll(utils.textWrapped(r).splitlines(), printers)
        # utils.printToAll(utils.textWrapped(question).splitlines(), printers)

i = input("Randomize y/n")
if i == "y":
    random.shuffle(toPrint)

for pair in toPrint: 
    utils.printToAll(utils.textWrapped(pair[1]).splitlines(), printers)
    utils.printToAll(utils.textWrapped(pair[0]).splitlines(), printers)