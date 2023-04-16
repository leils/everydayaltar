# Works with textbox but missing some basic functionality 
import curses
from curses.textpad import Textbox, rectangle

# rectOuterY = 5
# rectOuterX = 30

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


def dothing(stdscr):
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")
    curses.set_escdelay(1)

    editwin = curses.newwin(10,30, 2,1)
    rectangle(stdscr, 1,0, 1+10+1, 1+30+1)
    stdscr.refresh()

    box = Textbox(editwin, insert_mode=True)
    box.edit(validate)

    # # Let the user edit until Ctrl-G is struck.
    # box.edit()

    # Get resulting contents
    message = box.gather()
    stdscr.clear()
    return message

def main(window):
    # curses.wrapper(dothing)
    input_text = dothing(window)
    window.refresh()
    window.addstr(0, 0, f"You entered: {input_text}")
    window.getch()

if __name__ == "__main__":
    curses.wrapper(main)