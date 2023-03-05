import time, sys, random, json, textwrap
import os
import utils

dirname = os.path.dirname(__file__)
source_filename = os.path.join(dirname, 'source.json')
datastore = os.path.join(dirname, "data.json")

f = open(source_filename)
raw_data = json.load(f)
questions = raw_data['questions']

intro_message = """Take a breath. 
    When you're ready, press enter.
    """

outro_message = """Thank you for sharing."""

prompt = random.choice(questions)

#* ----Main Body of the Program--------------------------------------------------- */

while(1):
    os.system('clear')
    input()

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

    utils.write_to_file(new_data, datastore)
    print("\n")
    utils.print_slow("Going to sleep. Hope to see you soon.")

    time.sleep(5)

