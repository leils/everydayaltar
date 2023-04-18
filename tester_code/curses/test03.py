# Test to get curses and printout to work back and forth
import curses, traceback, time
from curses.textpad import Textbox
def validate(ch):

    # exit input with the escape key
    escape = 27
    if ch == escape:
        ch = curses.ascii.BEL # Control-G
    
    # delete the character to the left of the cursor
    elif ch in (curses.KEY_BACKSPACE, curses.ascii.DEL):
        ch = curses.KEY_BACKSPACE
    
    # exit input to resize windows
    elif ch == curses.KEY_RESIZE:
        ch = curses.ascii.BEL # Control-G

    return ch

def getInput(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "write a message please")

    editwin = curses.newwin(10,30, 2,1)
    # editwin.box()

    editBox = Textbox(editwin, insert_mode=True)
    editBox.edit(validate)
    message = editBox.gather().strip()
    stdscr.clear()
    return message


def main(): 
    print('hello, this is waiting for something')
    input()
    inputString = curses.wrapper(getInput)
    print(inputString)
    input()
    

if __name__ == "__main__":
    main()
 

