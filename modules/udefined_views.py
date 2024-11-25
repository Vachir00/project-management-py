import curses

def main_menu(stdscr, message, options, functions):
    # Inicializar colores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)  # Colores para la opción seleccionada
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Colores por defecto
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Colores para el mensaje de bienvenida

    current_option = 0

    while True:

        stdscr.clear()
        h, w = stdscr.getmaxyx()

        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(1, w // 2 - len(message) // 2, message)
        stdscr.attroff(curses.color_pair(3))

        for idx, option in enumerate(options):
            x = w // 2 - len(option) // 2
            y = h // 2 - len(options) // 2 + idx * 2  # Espacio entre opciones
            if idx == current_option:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, f"[ {option} ]")  # Enmarcar opción seleccionada
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(y, x, f"  {option}  ")  # Espacio adicional para mantener el tamaño
                stdscr.attroff(curses.color_pair(2))

        # Capturar tecla presionada
        key = stdscr.getch()

        # Navegación con teclas
        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(options) - 1:
            current_option += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            functions[current_option](stdscr)
            stdscr.clear()
        elif key == 27:  # Tecla ESC para salir
            break

        stdscr.refresh()