""" Custom styled button using the base Tkinter buttons """

import tkinter as tk

from modules.style import THEME

class CustomButton(tk.Button):
    """ Receive the initial arguments and call the build function """
    def __init__(
            self,
            master: any,
            font: tuple,
            command: any,
            place_coords: tuple,
            place_size: tuple,
            background: str = THEME["white"],
            foreground: str = THEME["black"],
            bindcolor: str = THEME["tertiary"],
            button_state: any = tk.NORMAL,
            image: any = None,
            text: str = None,
        ):
        super().__init__(master=master, image=image, text=text)
        self.background = background
        self.foreground = foreground
        self.bindcolor = bindcolor
        self.font = font
        self.command = command
        self.button_state = button_state
        self.place_coords = place_coords
        self.place_size = place_size
        self.on_creation()

    def on_creation(self):
        """ Creating the custom button and functions to create the hover effect """
        def on_enter(event):
            self["background"] = self.bindcolor
        def on_leave(event):
            self["background"] = self.background

        self.config(
            border=0,
            bg=self.background,
            fg=self.foreground,
            font=self.font,
            command=self.command,
            state=self.button_state
        )

        self.bind("<Enter>", on_enter)
        self.bind("<Leave>", on_leave)

        self.place(
            x=self.place_coords[0],
            y=self.place_coords[1],
            width=self.place_size[0],
            height=self.place_size[1]
        )

    def disable(self) -> None:
        """ A function to disable the button at call time """
        self["state"] = "disabled"

    def enable(self) -> None:
        """ A function to enable the button at call time """
        self["state"] = "normal"
