import time, sys, random, json

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
