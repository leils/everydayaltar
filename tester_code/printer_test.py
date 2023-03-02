import serial
import adafruit_thermal_printer

ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.68)
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)

printer = ThermalPrinter(uart)

printer.test_page()
printer.feed(2)
printer.bold = True

while(1):
    printer.print(input())
    printer.feed(2)

