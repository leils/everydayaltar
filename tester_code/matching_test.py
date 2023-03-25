import random, json
import os, sys
from pathlib import Path

#-------- shared utils access hack
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from shared import utils

### FILE SETUP 
sharedPath = path + '/shared'
source_filename = os.path.join(sharedPath, 'source.json')
data_filename = os.path.join(sharedPath, "data.json")

questions = json.load(open(source_filename))['questions']
responses = json.load(open(data_filename))

while(1): 
    print('-------------------------------')
    input('press enter to retrieve')
    q = random.choice(questions)
    print(q)
    print('responses:')
    if q in responses: 
        print(responses[q])
    else: 
        print("not found")

