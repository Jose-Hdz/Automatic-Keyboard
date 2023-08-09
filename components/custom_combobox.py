""" Custom styled combobox using the base Tkinter combobox """

import tkinter as tk
from tkinter import ttk

from modules.texts import FONT

class CustomComboBox(ttk.Combobox):
    """ Receive the initial arguments and call the build function """
    def __init__(
        self,
        master: any,
        values: list,
        textvariable: tk.StringVar,
        place_coords: tuple,
        place_size: tuple,
        state: any = tk.NORMAL,
        font: tuple = (FONT, 8),
        readonly: bool = True,
        *args,
        **kwargs
    ):
        super().__init__(
            master=master,
            values=values,
            textvariable=textvariable,
            font=font,
            state=state,
            *args,
            **kwargs
        )
        self.place_coords = place_coords
        self.place_size = place_size
        self.readonly = readonly
        self.on_creation()

    def on_creation(self):
        """ Position the combobox with the received configuration """
        self.place(
            x=self.place_coords[0],
            y=self.place_coords[1],
            width=self.place_size[0],
            height=self.place_size[1]
        )

        if self.readonly:
            self["state"] = "readonly"
