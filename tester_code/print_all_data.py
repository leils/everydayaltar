import serial, os, json
import adafruit_thermal_printer
import str_util
from pathlib import Path

ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.68)
# uart = serial.Serial("/dev/serial1", baudrate=19200, timeout=3000)
uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3000)

dirname = os.path.dirname(__file__)
p = Path(dirname)
parentPath = str(p.parent)
source_filename = os.path.join(parentPath, 'shared/source.json')
datastore = os.path.join(parentPath, "shared/data.json")

f = open(datastore)
raw_data = json.load(f)

printer = ThermalPrinter(uart)

printer.feed(2)
printer.up_down_mode = True

for q, a in raw_data.items():
    printer.print(str_util.textWrapped(q, 32))
    printer.feed(2)
    for answer in a: 
        printer.print(str_util.textWrapped(answer, 32))

