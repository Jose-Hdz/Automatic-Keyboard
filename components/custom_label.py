""" Custom styled label using the base Tkinter labels """

import tkinter as tk

from modules.style import THEME
from modules.texts import FONT

class CustomLabel(tk.Label):
    """ Receive the initial arguments and call the build function """
    def __init__(
            self,
            master: any,
            place_coords: tuple,
            place_size: tuple,
            font: tuple = (FONT, 14),
            background: THEME = THEME["primary"],
            foreground: THEME = THEME["secundary"],
            *args,
            **kwargs
    ) -> None:
        super().__init__(
            master=master,
            bg=background,
            fg=foreground,
            font=font,
            *args,
            **kwargs
        )
        self.place_coords = place_coords
        self.place_size = place_size
        self.on_creation()

    def on_creation(self) -> None:
        """ Position the label with the received configuration """
        self.place(
            x=self.place_coords[0],
            y=self.place_coords[1],
            width=self.place_size[0],
            height=self.place_size[1]
        )
