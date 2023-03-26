import serial
import adafruit_thermal_printer

import sys
from pathlib import Path

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

def print_all(s):
    global printers

    formattedString = utils.textWrapped(s, 32)
    lines = formattedString.splitlines()
    for l in lines: 
        for p in printers: 
            p.print(l)


while(1):
    i = input()
    print_all(i)

