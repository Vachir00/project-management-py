import curses
from pages.docker.docker_manager import list_containers, list_images, list_volumes


def docker_ui(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    options = [
        "Contenedores",
        "Imágenes",
        "Volúmenes"
    ]
    functions = [
        show_containers,
        show_images,
        show_volumes
    ]

    current_option = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        for idx, option in enumerate(options):
            x = w // 2 - len(option) // 2
            y = h // 2 - len(options) // 2 + idx * 2
            if idx == current_option:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, f"[ {option} ]")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(y, x, f"  {option}  ")
                stdscr.attroff(curses.color_pair(2))

        key = stdscr.getch()

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


def show_containers(stdscr):
    containers = list_containers()
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, container in enumerate(containers):
        stdscr.addstr(idx, 0, f"{container.name} ({container.status})")
    stdscr.refresh()
    stdscr.getch()  # Esperar a que el usuario presione una tecla


def show_images(stdscr):
    images = list_images()
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, image in enumerate(images):
        stdscr.addstr(idx, 0, f"{image.tags}")
    stdscr.refresh()
    stdscr.getch()


def show_volumes(stdscr):
    volumes = list_volumes()
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, volume in enumerate(volumes):
        stdscr.addstr(idx, 0, f"{volume.name}")
    stdscr.refresh()
    stdscr.getch()
