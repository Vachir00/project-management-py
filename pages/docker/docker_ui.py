# pages/docker/docker_ui.py
from textual.containers import Vertical
from textual.widgets import Placeholder


class DockerUI(Vertical):
    def compose(self):
        yield Placeholder("Docker UI")
