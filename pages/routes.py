import curses
from pages.docker.docker_ui import docker_ui
from pages.github.github_ui import github_ui
from pages.home import home_ui
from pages.settings.setting_ui import settings_ui


def show_routes(stdscr):
    # Inicializar colores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)  # Colores para la opción seleccionada
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Colores por defecto
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Colores para el mensaje de bienvenida

    options = [
        "Docker",
        "GitHub",
        "Settings"
    ]
    functions = [
        docker_ui,
        github_ui,
        settings_ui
    ]

    current_option = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        # Mensaje de bienvenida
        welcome_msg = "Bienvenido a la aplicación de gestión de proyectos"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(1, w // 2 - len(welcome_msg) // 2, welcome_msg)
        stdscr.attroff(curses.color_pair(3))

        # Dibujar opciones con bordes
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
