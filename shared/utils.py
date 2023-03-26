import time, sys, random, json
import textwrap

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
def textWrapped(text, maxColumn):         #maxColumn can be fetched from Adafruit_Thermal.py (it is 32)
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
