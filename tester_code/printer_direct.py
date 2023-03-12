import serial
import adafruit_thermal_printer
import str_util

ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.68)
# uart = serial.Serial("/dev/serial1", baudrate=19200, timeout=3000)
uart = serial.Serial("/dev/ttyUSB0", baudrate=19200, timeout=3000)

printer = ThermalPrinter(uart)

# printer.test_page()
printer.feed(2)
#printer.bold = True
# printer.inverse = True
printer.up_down_mode = True
while(1):
    i = input()
    s = str_util.textWrapped(i, 32)
    printer.print(s)
    printer.feed(2)

