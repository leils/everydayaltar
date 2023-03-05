import time, sys, random, json, textwrap
import os
import utils
import serial
import adafruit_thermal_printer
import str_util

dirname = os.path.dirname(__file__)
source_filename = os.path.join(dirname, 'source.json')
datastore = os.path.join(dirname, "data.json")

### PRINTER SETUP 
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.68)
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
printer = ThermalPrinter(uart)
printer.up_down_mode = True

### FILE SETUP 
f = open(source_filename)
raw_data = json.load(f)
questions = raw_data['questions']

### MESSAGING VARIABLES
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

    printer.print(prompt)
    printer.print(response)
    printer.feed(2)


    utils.write_to_file(new_data, datastore)
    print("\n")
    utils.print_slow("Going to sleep. Hope to see you soon.")

    time.sleep(5)

