import time, sys, random, json, textwrap
import os
import utils
import serial
import adafruit_thermal_printer

uart=serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.68)
printer = ThermalPrinter(uart)

f = open('source.json')
raw_data = json.load(f)
questions = raw_data['questions']
starters = raw_data['starters']

responses = []

intro_message = """Welcome to the altar.
    You are your ancestors, your descendants.
    You shape not moving forward or backwards but in all directions. 
    When you make an offering to this altar, you offer yourself a moment of reflection. 
    Press enter when you are ready. 
    """

generation_message = """ Thank you for offering those thoughts. 
Sift what you will from what has been given. 
"""

# Include the intro message in the word bank. 
responses.append(intro_message)

built_questions = []

chosen_questions = random.sample(questions, 3)
chosen_starters = random.sample(starters, 3)

# expects an array of strings
def generation_loop(responses):
    sift_text = utils.random_generator(respones)
    utils.print_slow(sift_text)
    print("\n*****----------------------*****")
    print("*****----------------------*****")

    utils.print_slow("\n\nResift? y/n")
    response = input().strip().lower()[:1]
    if response == 'y': 
        generation_loop(responses)
    else: 
        printer.print(sift_text)
        print("Goodbye.")


#* ----Main Body of the Program--------------------------------------------------- */

os.system('clear')
utils.print_slow(intro_message)
input()
utils.print_slow("Please, share a few things.\n")
utils.print_slow(chosen_starters[0] + chosen_questions[0] + '\n')
print("----------------------")
responses.append(input())
printer.print(responses[0])
printer.feed(3)
print("----------------------")
utils.print_slow("Thank you. \n")
utils.print_slow(chosen_starters[1] + chosen_questions[1] + '\n')
print("----------------------")
responses.append(input())
printer.print(responses[1])
printer.feed(3)
print("----------------------")
utils.print_slow("Thank you. \n")
utils.print_slow(chosen_starters[2] + chosen_questions[2] + '\n')
print("----------------------")
responses.append(input())
printer.print(responses[2])
printer.feed(3)
print("----------------------")
time.sleep(1.2)
utils.print_slow(generation_message)

print("*****----------------------*****")
print("*****----------------------*****")

generation_loop(responses)
