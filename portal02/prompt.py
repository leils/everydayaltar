import time, sys, random, json, textwrap
import os
import utils

f = open('/home/pi/portal01/source.json')
raw_data = json.load(f)
questions = raw_data['questions']
starters = raw_data['starters']

intro_message = """Take a breath. 
    When you're ready, press enter.
    """

outro_message = """Thank you for sharing."""

chosen_question = random.choice(questions)
chosen_starter = random.choice(starters)

prompt = chosen_starter + chosen_question



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

    utils.write_to_file(new_data)
    print("\n")
    utils.print_slow("Going to sleep. Hope to see you soon.")

    time.sleep(5)

