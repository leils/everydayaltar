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


### MESSAGING VARIABLES
intro_message = """Take a breath. 
    When you're ready, press enter.
    """

outro_message = """Thank you for sharing."""

def print_matched_responses(q):
    global responses
    
    utils.print_slow('Finding matched responses ...\n')
    print('-------------------------------')
    if q in responses: 
        chosen_responses = []
        if len(responses[q]) > 2:
            chosen_responses = random.sample(responses[q], 2)
        else: 
            chosen_responses = responses[q]
        
        for r in chosen_responses:
            utils.print_slow(r)
            print('\n\n')
            print('-------------------------------\n')
    else: 
        utils.print_slow("no other responses found. check again later, maybe someone else will stop by.\n")


while(1): 
    os.system('clear')
    input('press enter to wake up')
    os.system('clear')
    print('-------------------------------')

    utils.print_slow(intro_message)
    input()
    utils.print_slow("Please, share a few things.\n")

    q = random.choice(questions)
    utils.print_slow(q + "\n")

    print("----------------------")
    response = input()
    print("----------------------")
    utils.print_slow(outro_message)
    print("\n")

    print_matched_responses(q)
    utils.write_to_file(response, data_filename, q)

    print("\n")

