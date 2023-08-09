"""
Module that controls the colors of
the program depending on the selected theme.
"""

from modules.config import global_config_program

THEME = {}

BLACK = "#30302e"
WHITE = "#ffffff"
BLUE = "#c9c9ff"
PURPLE = "#f1cbff"
PINK = "#ffbdbd"

def get_theme(default_theme: str) -> dict:
    """ Select the selected theme in the initial configuration """
    theme = {
        "dark": {
            "white": WHITE,
            "black": BLACK,
            "primary": BLACK,
            "secundary": WHITE,
            "tertiary": PURPLE
        },
        "blue": {
            "white": WHITE,
            "black": BLACK,
            "primary": BLUE,
            "secundary": WHITE,
            "tertiary": PURPLE,
        },
        "pink": {
            "white": WHITE,
            "black": BLACK,
            "primary": PINK,
            "secundary": WHITE,
            "tertiary": PURPLE
        }
    }

    return theme.get(default_theme)

THEME = get_theme(global_config_program["theme"])
TOTAL_THEMES = ["dark", "blue", "pink"]
