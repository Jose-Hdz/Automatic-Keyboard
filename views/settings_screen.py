""" settings screen """

import tkinter as tk

import pickle

from tkinter import messagebox

from modules.style import THEME, TOTAL_THEMES
from modules.texts import TEXT, FONT, TOTAL_LANGUAGES
from modules.config import global_config_program

from components.custom_button import CustomButton
from components.custom_combobox import CustomComboBox
from components.custom_label import CustomLabel
from components.custom_slider import CustomSlider

from data.global_var import DIR_DATA

class SettingsScreen(tk.Toplevel):
    """
    Create the large screen, configure it, and call the on_creation function.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screen_size = (300, 300)
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
            width=300,
            height=300
        )
        # Initial variables
        self.var_time_to_start = tk.IntVar()
        self.var_time_to_start.set(f"{int(global_config_program['time_to_start'])}s")
        self.var_language = tk.StringVar()
        self.var_language.set(global_config_program["language"])
        self.var_theme = tk.StringVar()
        self.var_theme.set(global_config_program["theme"])
        # Initial widgets
        self.label_settings: CustomLabel
        self.label_time_to_start: CustomLabel
        self.label_time_to_start_input: CustomLabel
        self.label_language: CustomLabel
        self.label_theme: CustomLabel
        self.slider_time_to_start: CustomSlider
        self.button_cancel: CustomButton
        self.button_ok: CustomButton
        self.combobox_language: CustomComboBox
        self.combobox_theme: CustomComboBox

        self.create_widget_labels()
        self.create_widget_sliders()
        self.create_widget_combobox()
        self.create_widget_buttons()

    def create_widget_labels(self) -> CustomLabel:
        """ Create all label widgets """
        self.label_settings = CustomLabel(
            master=self,
            place_coords=(70, 10),
            place_size=(160, 30),
            text=TEXT["SS_settings"],
            justify=tk.CENTER
        )
        self.label_time_to_start = CustomLabel(
            master=self,
            place_coords=(90, 70),
            place_size=(130, 20),
            font=(FONT, 9),
            text=TEXT["SS_time_to_start"],
            justify=tk.CENTER
        )
        self.label_time_to_start_input = CustomLabel(
            master=self,
            place_coords=(190, 90),
            place_size=(30, 20),
            font=(FONT, 8),
            textvariable=self.var_time_to_start,
            justify=tk.CENTER
        )
        self.label_language = CustomLabel(
            master=self,
            place_coords=(100, 120),
            place_size=(100, 20),
            font=(FONT, 9),
            text=TEXT["SS_language"],
            justify=tk.CENTER
        )
        self.label_theme = CustomLabel(
            master=self,
            place_coords=(100, 170),
            place_size=(100, 20),
            font=(FONT, 9),
            text=TEXT["SS_theme"],
            justify=tk.CENTER
        )

    def create_widget_sliders(self) -> CustomSlider:
        """ Create all slider widgets """
        self.slider_time_to_start = CustomSlider(
            master=self,
            from_=1,
            to=60,
            place_coords=(90, 90),
            place_size=(90, 20),
            value=global_config_program["time_to_start"],
            variable=self.var_time_to_start,
            command=self.slider_time_to_start_state
        )

    def create_widget_combobox(self) -> CustomComboBox:
        """ Create all combobox widgets """
        self.combobox_language = CustomComboBox(
            master=self,
            values=TOTAL_LANGUAGES,
            textvariable=self.var_language,
            place_coords=(100, 140),
            place_size=(100, 20)
        )
        self.combobox_theme = CustomComboBox(
            master=self,
            values=TOTAL_THEMES,
            textvariable=self.var_theme,
            place_coords=(100, 190),
            place_size=(100, 20)
        )

    def create_widget_buttons(self) -> CustomButton:
        """ Create all button widgets """
        self.button_cancel = CustomButton(
            master=self,
            font=(FONT, 8),
            command=self.func_cancel,
            place_coords=(70, 250),
            place_size=(70, 30),
            text=TEXT["SS_cancel"]
        )
        self.button_ok = CustomButton(
            master=self,
            font=(FONT, 8),
            command=self.func_ok,
            place_coords=(160, 250),
            place_size=(70, 30),
            text=TEXT["SS_ok"]
        )

    def slider_time_to_start_state(self, event) -> None:
        """
        Update the slider time to start text each time
        the slider state is changed, raised, or lowered.
        """
        self.var_time_to_start.set(f"{int(self.slider_time_to_start.get())}s")

    def func_cancel(self) -> None:
        """ Cancel changes and activates all buttons in the home screen """
        self.master.closing_protocol()

    def func_ok(self) -> None:
        """
        Records all selected settings and modifies the config.ak
        file to overwrite them, changes are applied when closing
        and opening the program
        """
        time_to_start = int(self.slider_time_to_start.get())
        language = self.var_language.get()
        theme = self.var_theme.get()

        DEFAULT_CONFIG = {
            "language": language[:2],
            "theme": theme,
            "time_to_start": time_to_start
        }

        with open(f"{DIR_DATA}config.ak", "wb") as configuration:
            pickle.dump(DEFAULT_CONFIG, configuration)

        messagebox.showinfo(TEXT["info"], TEXT["SS_info_ok"])
        self.master.closing_protocol()
