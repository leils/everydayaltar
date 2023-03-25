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
datastore = os.path.join(sharedPath, "data_test.json")

f = open(source_filename)
raw_data = json.load(f)
questions = raw_data['questions']


### MESSAGING VARIABLES
intro_message = """Take a breath. 
    When you're ready, press enter.
    """

outro_message = """Thank you for sharing."""


#* ----Main Body of the Program--------------------------------------------------- */

while(1):
    os.system('clear')
    input("Press enter to wake me up ...")
    prompt = random.choice(questions)

    utils.print_slow(intro_message)
    input()
    utils.print_slow("Please, share a few things.\n")
    utils.print_slow(prompt + '\n')
    print("----------------------")
    response = input()
    print("----------------------")
    utils.print_slow(outro_message)

    new_data = {
        "prompt": prompt,
        "response": response
    }

    utils.write_to_file(response, datastore, prompt)
    print("\n")
    utils.print_slow("Going to sleep. Hope to see you soon.")

    time.sleep(5)

