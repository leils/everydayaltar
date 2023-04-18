# Test to get curses and printout to work back and forth
import curses, os, textwrap
from curses.textpad import Textbox, rectangle
import sys, json, os, random, time
from pathlib import Path

#-------- shared utils access hack
path = str(Path(Path(__file__).parent.absolute()).parent.absolute().parent.absolute())
sys.path.insert(0, path)

from shared import utils

def main(): 
    question = "Write about one of your hobbies. Why do you do it? Who do you do it with?"
    os.system('clear')
    print('hello, this is waiting for enter')
    input()
    inputString = curses.wrapper(utils.inputBox, question)

    os.system('clear')
    print(inputString)

    formatted = " ".join(x.strip() for x in inputString.split("\n"))
    print(formatted)
    input()
    

if __name__ == "__main__":
    main()
 

