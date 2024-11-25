from modules.udefined_views import main_menu
from pages.docker.docker_manager import list_containers, list_images, list_volumes


def docker_ui(stdscr):

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

    main_menu(stdscr, "test123", options, functions)


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
