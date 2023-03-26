import random, json
import os, sys
from pathlib import Path
import serial
import adafruit_thermal_printer

#-------- shared utils access hack
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from shared import utils

### ------------------------- FILE SETUP 
sharedPath = path + '/shared'
source_filename = os.path.join(sharedPath, 'source.json')
data_filename = os.path.join(sharedPath, "data.json")

questions = json.load(open(source_filename))['questions']
responses = json.load(open(data_filename))


### ------------------------- MESSAGING VARIABLES
intro_message = """Take a breath. 
    When you're ready, press enter.
    """
outro_message = """Thank you for sharing."""

### ------------------------- PRINTER SETUP
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.68)

#there's definitely a better way of doing this
uart1 = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3000)
uart2 = serial.Serial("/dev/ttyUSB1", baudrate=9600, timeout=3000)
uart3 = serial.Serial("/dev/ttyUSB2", baudrate=9600, timeout=3000)

printer1 = ThermalPrinter(uart1)
printer2 = ThermalPrinter(uart2)
printer3 = ThermalPrinter(uart3)

### ------------------------- RESPONSE HANDLING
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


### ------------------------- MAIN PROGRAM
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

