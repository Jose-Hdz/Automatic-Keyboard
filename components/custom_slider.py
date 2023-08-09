""" Custom styled Slider using the base Tkinter scales """

from tkinter import ttk
import tkinter as tk

from modules.style import THEME
from modules.texts import FONT

class CustomSlider(ttk.Scale):
    """ Receive the initial arguments and call the build function """
    def __init__(
            self,
            master: any,
            from_: int,
            to: int,
            place_coords: tuple,
            place_size: tuple,
            orient: any = tk.HORIZONTAL,
            background: str = THEME["primary"],
            value: any = 0,
            *args,
            **kwargs,
    ):
        super().__init__(
            master=master,
            from_=from_,
            to=to,
            orient=orient,
            value=value,
            *args,
            **kwargs
        )
        self.background = background
        self.place_coords = place_coords
        self.place_size = place_size
        self.on_creation()

    def on_creation(self):
        """ Set the style and position the slider with the received configuration """
        ttk.Style().configure("TScale",background=self.background)

        self.place(
            x=self.place_coords[0],
            y=self.place_coords[1],
            width=self.place_size[0],
            height=self.place_size[1]
        )
