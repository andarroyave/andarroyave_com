import reflex as rx
from rxconfig import config
import datetime


SECTIONS = {
    "home": "Hello Home",
    "about": "Hello About",
    "contact": "Hello Contact",
    "tema1": "Hello Tema 1",
    "tema2": "Hello Tema 2",
    "tema3": "Hello Tema 3",
    "tema4": "Hello Tema 4",
}

class Content(rx.Base):
    text: str

class Article(rx.Base):
    title: str
    content: Content
    date: datetime.datetime
    keywords: list[str]

class State(rx.State):
    '''state'''
    content: str = "Hello, world!"
    contents: dict  = SECTIONS

    @rx.event
    def set_content(self, section: str) -> None:
        self.content = self.contents[section]


def nav_link(text: str, url: str, section: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url, on_click=State.set_content(section),
    )

# Define the header component with a logo and navbar
def header() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="../assets/favicon.icon",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "andarroyave.com", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    nav_link("Home", "/#", "home"), 
                    nav_link("About", "/#", "about"),
                    nav_link("Contact", "/#", "contact"),
                    rx.color_mode.button(),
                    justify="end",
                    spacing="5",
                ),
                
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "andarroyave.com", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item(nav_link("Home", "/#", "home")),
                        rx.menu.item(nav_link("About", "/#", "about")),
                        rx.menu.item(nav_link("Contact", "/#", "contact")),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        #bg=rx.color("accent", 3),
        padding="1em",
        width="100%",
    )

def sidebar_items() -> rx.Component:
    return rx.vstack(
        nav_link("Tema 1", "/#", "tema1"),
        nav_link("Tema 2", "/#", "tema2"),
        nav_link("Tema 3", "/#", "tema3"),
        nav_link("Tema 4", "/#", "tema4"),
        spacing="1",
        width="100%",
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                sidebar_items(),
                spacing="5",
                # position="fixed",
                # left="0px",
                # top="0px",
                # z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                #bg=rx.color("accent", 3),
                align="start",
                # height="100%",
                height="650px",
                width="16em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    placeholder="Search...",
                    type="search",
                    size="2",
                    justify="end",
                    padding_x="1em",
                ),
                align_items="center",
                padding_x="1em",
            ),
        ),
    )


# Define the main content component with dynamic content
def main_content() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(State.content, font_size="xl"),
            rx.image(src="../assets/favicon.ico", alt="Placeholder image"),
            padding="2rem",
        ),
        width="80%",
    )

def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "© 2025 andarroyave.com",
                size="3",
                white_space="nowrap",
                weight="medium",
            ),
            rx.logo(),
            align_items="center",
            justify="center",
            width="100%",
        ),
        align_items="between",
        width="100%",
    )

# Define the main page layout
def index():
    return rx.vstack(
        
        header(),
        rx.hstack(
            sidebar(),
            main_content(),
            width="100%",
            height="calc(100vh - 4rem)",  # Full height minus header height
        ),
        footer(),
        
        spacing="0",
        
    )


# Create the app and add the index page
app = rx.App()
app.add_page(index, route="/")
