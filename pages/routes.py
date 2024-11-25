from modules.udefined_views import main_menu
from pages.docker.docker_ui import docker_ui
from pages.github.github_ui import github_ui
from pages.home import home_ui
from pages.settings.setting_ui import settings_ui


def show_routes(stdscr):
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

    main_menu(stdscr, "test123", options, functions)
