# pages/home.py
from textual.app import App, ComposeResult
from textual.widgets import Placeholder, Header, Footer
from textual.containers import Vertical, Center
from pages.routes import routes


class HomeView(Center):
    def compose(self) -> ComposeResult:
        for route_name in routes:
            yield Placeholder(route_name)


class HomeApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield HomeView()


if __name__ == "__main__":
    HomeApp().run()
