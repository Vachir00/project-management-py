import curses
from pages.routes import show_routes


def main(stdscr):
    curses.curs_set(0)  # Oculta el cursor
    stdscr.clear()

    # Mostrar la pantalla inicial
    show_routes(stdscr)

    stdscr.refresh()
    stdscr.getch()


curses.wrapper(main)
