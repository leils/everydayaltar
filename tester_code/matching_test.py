import time, random, json
import os, sys
from pathlib import Path

#-------- shared utils access hack
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from shared import utils

### FILE SETUP 
sharedPath = path + '/shared'
source_filename = os.path.join(sharedPath, 'source.json')
datastore = os.path.join(sharedPath, "data.json")

f = open(source_filename)
raw_data = json.load(f)
questions = raw_data['questions']