import curses, traceback
import curses.textpad

def main(stdscr): 
    global screen
    screen = stdscr.subwin(23, 79, 2, 2)
    screen.box()
    print('HELLO')

    screen.addstr(1, 1, "hello")
    screen.getch()

if __name__ == "__main__":
    try:
        # Initialize curses
        stdscr=curses.initscr()
        # Turn off echoing of keys, and enter cbreak mode,
        # where no buffering is performed on keyboard input
        curses.noecho()
        curses.cbreak()

        # do things here
        main(stdscr)

        stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()  
    except:
        stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        traceback.print_exc()           # Print the exception

