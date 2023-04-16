# Works well but needs some amount of tweaking. 
# taken from: https://stackoverflow.com/questions/47481955/python-curses-detecting-the-backspace-key
# user aidanmelen

import curses
import curses.textpad 

def get_input(window):
    curses.curs_set(1)
    curses.set_escdelay(1)
    window.addstr(0, 0, "Enter some text:")
    input_box = curses.textpad.Textbox(curses.newwin(1, 40, 1, 0), insert_mode=True)
    
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
    
    input_box.edit(validate)
    curses.curs_set(0)
    curses.set_escdelay(1000)
    return input_box.gather().strip()


def main(window):
    curses.noecho()
    curses.cbreak()
    window.keypad(True)
    curses.curs_set(0)

    input_text = get_input(window)

    window.addstr(2, 0, f"You entered: {input_text}")
    window.refresh()
    window.getch()

if __name__ == "__main__":
    curses.wrapper(main)