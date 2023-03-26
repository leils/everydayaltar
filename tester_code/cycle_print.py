import serial
import adafruit_thermal_printer

import sys
from pathlib import Path

#-------- shared utils access hack
printerLineLen = 32

#-------- shared utils access hack
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from shared import utils

ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.68)

#there's definitely a better way of doing this
uart1 = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3000)
uart2 = serial.Serial("/dev/ttyUSB1", baudrate=9600, timeout=3000)
uart3 = serial.Serial("/dev/ttyUSB2", baudrate=9600, timeout=3000)

printer1 = ThermalPrinter(uart1)
printer2 = ThermalPrinter(uart2)
printer3 = ThermalPrinter(uart3)

printers = [printer1, printer2, printer3]

#printer setup
for p in printers: 
    p.feed(2)
    p.up_down_mode = True

def printInCycle(lines, printers):
    if len(lines) != len(printers): 
        print("Number of line sets (", len(lines), ") must equal number of printers (", len(printers),")")
        return

    maxLineLen = max(map(len, lines))

    for i in range(maxLineLen):
        for p in range(len(printers)):
            printer = printers[p]
            lineSet = lines[p]
            if i < len(lineSet):
                printer.print(lineSet[i])

s1 = "I recently rediscovered my own imagination when trying to fall asleep. Why think about the chores of tomorrow when I can pretend that pigeons are huge and I can grab onto their wings and hitch a ride? Or I can hold my breath indefinitely underwater and swim with Pokemon-lookin dratini?"
s2 = "I usually call my mother with bad news, or my friend Joe. When I want to tell them the worries I have, I know theyll listen with care and call me on my bullshit whenever I need them to. And they'll take a moment to mourn with me"
s3 = "I am really great at working between the hours of 9pm and 2am. There's something about that time that really works with my brain. Maybe it's because I never used to sleep at good hours, I used to only sleep for 4 so 5 hours each night. Even when I could sleep more, I'd take that extra time to read or surf the web instead. "

lineGroup = [
    utils.textWrapped(s1, printerLineLen).splitlines(),
    utils.textWrapped(s2, printerLineLen).splitlines(),
    utils.textWrapped(s3, printerLineLen).splitlines()
]

printInCycle(lineGroup, printers)