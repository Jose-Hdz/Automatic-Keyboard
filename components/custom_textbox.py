""" Custom styled TextBox using the base Tkinter textbox """

import tkinter as tk

from modules.style import THEME

class CustomTextBox(tk.Text):
    """ Receive the initial arguments and call the build function """
    def __init__(
            self,
            master: any,
            font: tuple,
            place_coords: tuple,
            place_size: tuple,
            foreground: str = THEME["black"],
            *args,
            **kwargs,
    ):
        super().__init__(
            master=master,
            fg=foreground,
            font=font,
            *args,
            **kwargs
        )
        self.place_coords = place_coords
        self.place_size = place_size
        self.on_creation()

    def on_creation(self):
        """ Position the textbox with the received configuration """
        self.place(
            x=self.place_coords[0],
            y=self.place_coords[1],
            width=self.place_size[0],
            height=self.place_size[1]
        )
