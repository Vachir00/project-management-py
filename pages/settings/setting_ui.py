# pages/settings/setting_ui.py
from textual.containers import Vertical
from textual.widgets import Placeholder
from textual import events


class SettingUI(Vertical):
    DEFAULT_CSS = """
    SettingUI {
        background: $boost;
        color: $text;
    }
    """

    def compose(self):
        yield Placeholder("Setting UI")
