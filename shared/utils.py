import time, sys, random, json
import textwrap

defaultMaxColumn = 32

def setupPrinters():
    import serial
    import adafruit_thermal_printer

    ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.68)

    #there's definitely a better way of doing this
    uart1 = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3000)
    uart2 = serial.Serial("/dev/ttyUSB1", baudrate=9600, timeout=3000)
    uart3 = serial.Serial("/dev/ttyUSB2", baudrate=9600, timeout=3000)

    printer1 = ThermalPrinter(uart1)
    printer2 = ThermalPrinter(uart2)
    printer3 = ThermalPrinter(uart3)

    printers = [printer1, printer2, printer3]

    for p in printers: 
        p.feed(2)
        p.up_down_mode = True

    return printers

def print_pause():
    return random.random() * .1

def print_dots(n):
    for x in range(n):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(.3)
    print('\n')

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(print_pause())
        time.sleep(.02)
    time.sleep(0.2)

def write_to_file(new_data, filename, dataname="data"): 
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data 
        if dataname in file_data: 
            file_data[dataname].append(new_data)
        else: 
            file_data[dataname] = [new_data]
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

# taken from https://forums.adafruit.com/viewtopic.php?f=19&t=56504
def textWrapped(text, maxColumn = 32):         #maxColumn can be fetched from Adafruit_Thermal.py (it is 32)
	textWrapped = textwrap.wrap(text, width=maxColumn)
	for i in range(len(textWrapped)):
		textWrapped[i]+='\n'

	textWrappedReversed = textWrapped[::-1] # reverse the lines in order to print bottom-to-top
	stringForPrinter = ''.join(list(textWrappedReversed))
	return stringForPrinter

# param lines; array of arrays of strings 
# param printers; array of printer objects
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
    
    for p in printers: 
        p.feed(2)

#param lines; pre-formatted array of strings
#printers; array of printer objects
def printToAll(lines, printers):
    for l in lines: 
        for p in printers: 
            p.print(l)
    for p in printers: 
        p.feed(2)

def formatArrayForMultiPrint(arrayOfStrings):
    wrappedStrings = list(map(textWrapped, arrayOfStrings))
    splitStrings = list(map(lambda s: s.splitlines(), wrappedStrings))
    return splitStrings

def printInvertedToAll(lines, printers):
    for p in printers: 
        p.inverse = True
    
    printToAll(lines, printers)

    for p in printers: 
        p.inverse = False