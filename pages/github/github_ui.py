# pages/github/github_ui.py
from textual.containers import Vertical
from textual.widgets import Placeholder


class GithubUI(Vertical):
    def compose(self):
        yield Placeholder("Github UI")
