# pages/routes.py
from pages.docker.docker_ui import DockerUI
from pages.github.github_ui import GithubUI
from pages.settings.setting_ui import SettingUI

routes = {
    "docker": DockerUI,
    "github": GithubUI,
    "settings": SettingUI,
}
