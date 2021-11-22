import curses

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello World!")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)