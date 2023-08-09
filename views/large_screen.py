""" large text screen """

import tkinter as tk

from modules.style import THEME
from modules.texts import TEXT, FONT

from components.custom_button import CustomButton
from components.custom_textbox import CustomTextBox
from components.custom_label import CustomLabel

from data import global_var
from data.global_var import DIR_ICONS

class LargeScreen(tk.Toplevel):
    """
    Create the large screen, configure it, and call the on_creation function.
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.screen_size = (500, 400)
        self.start_screen_position = (self.master.winfo_x(), self.master.winfo_y())

        self.resizable(0, 0)
        self.geometry(
            f"{self.screen_size[0]}x{self.screen_size[1]}+{self.start_screen_position[0]}+{self.start_screen_position[1]}"
        )
        self.background_frame = BackgroundFrame(self)
        self.background_frame.pack()
        self.protocol("WM_DELETE_WINDOW", self.closing_protocol)

    def closing_protocol(self):
        """
        When the window closes, call the tkinter close protocol,
        reactivate the necessary buttons, and destroy the window.
        """
        self.master.background_frame.func_activate_buttons()
        self.destroy()

class BackgroundFrame(tk.Frame):
    """
    Create the background frame, configure it, and call the on_creation function.
    """
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.config(
            background=THEME["primary"],
            width=500,
            height=400
        )
        # Initial variables
        self.icon_large = tk.PhotoImage(file=DIR_ICONS + "large.png")
        # Initial widgets
        self.label_large_text: CustomLabel
        self.label_ready: CustomLabel
        self.textbox_large: CustomTextBox
        self.button_ready: CustomButton

        self.create_widget_labels()
        self.create_widget_textbox()
        self.create_widget_button()

    def create_widget_labels(self) -> CustomLabel:
        """ Create all label widgets """
        self.label_large_text = CustomLabel(
            master=self,
            font=(FONT, 15),
            place_coords=(10, 10),
            place_size=(210, 30),
            text=TEXT["LS_large_text"],
            anchor=tk.W
        )
        self.label_ready = CustomLabel(
            master=self,
            font=(FONT, 15),
            place_coords=(370, 10),
            place_size=(80, 30),
            text=TEXT["LS_ready"],
            anchor=tk.E
        )

    def create_widget_textbox(self) -> CustomTextBox:
        """ Create all textbox widgets """
        self.textbox_large = CustomTextBox(
            master=self,
            font=(FONT, 8),
            place_coords=(10, 50),
            place_size=(480, 340)
        )
        self.textbox_large.insert(tk.END, global_var.text_from_entry_home_screen)

    def create_widget_button(self) -> CustomButton:
        """ Create all button widgets """
        self.button_ready = CustomButton(
            master=self,
            background=THEME["white"],
            foreground=THEME["black"],
            bindcolor=THEME["tertiary"],
            font=(FONT, 8),
            command=self.func_ready,
            button_state=tk.NORMAL,
            place_coords=(460, 10),
            place_size=(30, 30),
            image=self.icon_large
        )

    def func_ready(self) -> str:
        """
        Save the text placed in the text box
        1) Saves the text in the global variable
        2) Deletes the text found in the home screen entry
        3) Paste the text from the text box into the home screen entry
        4) Call closing protocol
        """
        global_var.text_from_textbox_large_screen = self.textbox_large.get(1.0, tk.END)
        self.master.master.background_frame.entry_your_text.delete(0, tk.END)
        self.master.master.background_frame.entry_your_text.insert(
            0, global_var.text_from_textbox_large_screen[:-1]
        )
        self.master.closing_protocol()
