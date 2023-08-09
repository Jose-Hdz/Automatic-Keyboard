""" Initial screen of the program """

import tkinter as tk
from tkinter import messagebox
import threading
import time

import pyautogui

from modules.style import THEME
from modules.texts import TEXT, FONT
from modules.config import global_config_program

from components.custom_button import CustomButton
from components.custom_entry import CustomEntry
from components.custom_label import CustomLabel
from components.custom_slider import CustomSlider

from views.large_screen import LargeScreen
from views.settings_screen import SettingsScreen

from data import global_var
from data.global_var import DIR_ICONS

class HomeScreen(tk.Tk):
    """
    Create the home screen, take the measurements of the computer
    screen and calculate to initialize the application in the center of the screen.
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.screen_size = (500, 200)
        self.screen_dimensions = (
            self.winfo_screenwidth(),
            self.winfo_screenheight()
        )
        self.start_screen_position = (
            int((self.screen_dimensions[0] / 2) - (self.screen_size[0] / 2)),
            int((self.screen_dimensions[1] / 2) - (self.screen_size[1] / 2))
        )

        self.title("Automatic Keyboard")
        self.iconbitmap("./icon.ico")
        self.resizable(0, 0)
        self.geometry(
            f"{self.screen_size[0]}x{self.screen_size[1]}+{self.start_screen_position[0]}+{self.start_screen_position[1]}"
        )
        self.background_frame = BackgroundFrame(self)
        self.background_frame.pack()
        self.mainloop()

class BackgroundFrame(tk.Frame):
    """
    Create the background frame, configure it, and call the on_creation function.
    """
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.config(
            background=THEME["primary"],
            width=500,
            height=200
        )
        # Initial variables
        self.var_text_delay = tk.DoubleVar()
        self.var_text_delay.set("0.0")
        self.var_text_loops = tk.IntVar()
        self.var_text_loops.set("0")
        self.var_text_process = tk.StringVar()
        self.var_text_process.set("0")

        self.icon_delete = tk.PhotoImage(file=DIR_ICONS + "delete.png")
        self.icon_large = tk.PhotoImage(file=DIR_ICONS + "large.png")
        self.icon_settings = tk.PhotoImage(file=DIR_ICONS + "settings.png")
        self.icon_layers = tk.PhotoImage(file=DIR_ICONS + "layers.png")
        # Widgets Variables
        self.label_your_text: CustomLabel
        self.label_delay: CustomLabel
        self.label_delay_input: CustomLabel
        self.label_loops: CustomLabel
        self.label_loops_input: CustomLabel
        self.label_process: CustomLabel
        self.entry_your_text: CustomEntry
        self.slider_delay: CustomSlider
        self.slider_loops: CustomSlider
        self.button_delete: CustomButton
        self.button_large_text: CustomButton
        self.button_settings: CustomButton
        self.button_block_mode: CustomButton
        self.button_start: CustomButton

        self.create_widget_labels()
        self.create_widget_entries()
        self.create_widget_slider()
        self.create_widget_button()

    def create_widget_labels(self) -> CustomLabel:
        """ Create all label widgets """
        self.label_your_text = CustomLabel(
            master=self,
            place_coords=(20, 20),
            place_size=(190, 20),
            text=TEXT["HS_your_text"],
            anchor=tk.W
        )
        self.label_delay = CustomLabel(
            master=self,
            place_coords=(20, 120),
            place_size=(90, 20),
            font=(FONT, 12),
            text=TEXT["HS_delay"],
            anchor=tk.W
        )
        self.label_loops = CustomLabel(
            master=self,
            place_coords=(150, 120),
            place_size=(90, 20),
            font=(FONT, 12),
            text=TEXT["HS_loops"],
            anchor=tk.W
        )
        self.label_delay_input = CustomLabel(
            master=self,
            place_coords=(115, 150),
            place_size=(30, 20),
            font=(FONT, 8),
            textvariable=self.var_text_delay,
            justify=tk.CENTER
        )
        self.label_loops_input = CustomLabel(
            master=self,
            place_coords=(245, 150),
            place_size=(30, 20),
            font=(FONT, 8),
            textvariable=self.var_text_loops,
            justify=tk.CENTER
        )
        self.label_process = CustomLabel(
            master=self,
            place_coords=(390, 100),
            place_size=(90, 20),
            font=(FONT, 8),
            textvariable=self.var_text_process,
            justify=tk.CENTER
        )

    def create_widget_entries(self) -> CustomEntry:
        """ Create all entry widgets """
        self.entry_your_text = CustomEntry(
            master=self,
            foreground=THEME["black"],
            font=(FONT, 8),
            place_coords=(20, 60),
            place_size=(220, 30),
            justify=tk.CENTER
        )

    def create_widget_slider(self) -> CustomSlider:
        """ Create all slider widgets """
        self.slider_delay = CustomSlider(
            master=self,
            from_=0,
            to=5,
            place_coords=(20, 150),
            place_size=(90, 20),
            variable=self.var_text_delay,
            command=self.slider_delay_state
        )
        self.slider_loops = CustomSlider(
            master=self,
            background=THEME["primary"],
            from_=0,
            to=20,
            orient=tk.HORIZONTAL,
            place_coords=(150, 150),
            place_size=(90, 20),
            variable=self.var_text_loops,
            command=self.slider_loops_state
        )

    def create_widget_button(self) -> CustomButton:
        """ Create all button widgets """
        self.button_delete = CustomButton(
            master=self,
            font=(FONT, 8),
            command=self.func_delete_yourtext,
            place_coords=(250, 60),
            place_size=(30, 30),
            image=self.icon_delete
        )
        self.button_large_text = CustomButton(
            master=self,
            font=(FONT, 8),
            command=self.func_init_large_screen,
            place_coords=(290, 60),
            place_size=(30, 30),
            image=self.icon_large
        )
        self.button_settings = CustomButton(
            master=self,
            font=(FONT, 8),
            command=self.func_init_settings_screen,
            place_coords=(450, 20),
            place_size=(30, 30),
            image=self.icon_settings
        )
        self.button_block_mode = CustomButton(
            master=self,
            font=(FONT, 8),
            command=self.func_init_block_screen,
            place_coords=(390, 20),
            place_size=(50, 30),
            image=self.icon_layers
        )
        self.button_start = CustomButton(
            master=self,
            font=(FONT, 12),
            command=self.func_start_create_thread,
            place_coords=(390, 130),
            place_size=(90, 50),
            text=TEXT["HS_start"]
        )

    def slider_delay_state(self, event) -> None:
        """
        Update the slider delay text each time
        the slider state is changed, raised, or lowered.
        """
        self.var_text_delay.set(f"{self.slider_delay.get():.1f}")

    def slider_loops_state(self, event) -> None:
        """
        Update the slider loops text each time
        the slider state is changed, raised, or lowered.
        """
        self.var_text_loops.set(f"{int(self.slider_loops.get())}")

    def func_delete_yourtext(self) -> None:
        """ Deletes the text containing the entry named your_text """
        self.entry_your_text.delete(0, tk.END)

    def func_deactivate_buttons(self) -> None:
        """
        Disable the buttons in the home screen
        to avoid opening multiple tabs at the same time.
        """
        self.button_block_mode["state"] = "disabled"
        self.button_delete["state"] = "disabled"
        self.button_large_text["state"] = "disabled"
        self.button_settings["state"] = "disabled"
        self.button_start["state"] = "disabled"

    def func_activate_buttons(self) -> None:
        """ Activates all buttons in the home screen """
        self.button_block_mode["state"] = "normal"
        self.button_delete["state"] = "normal"
        self.button_large_text["state"] = "normal"
        self.button_settings["state"] = "normal"
        self.button_start["state"] = "normal"

    def func_start_create_thread(self) -> None:
        """
        Function that creates the startup thread
        to run the startup process in the background.
        """
        threading.Thread(target=self.func_start).start()

    def func_start(self) -> None:
        """
        Auto-write function, takes the values of
        the input and the sliders, and starts the process.
        """
        time_to_start = global_config_program["time_to_start"]
        text_from_yourtext_entry = self.entry_your_text.get()
        delay_from_delay_slider = float(self.slider_delay.get())
        loops_from_loop_slider = int(self.slider_loops.get())

        if len(text_from_yourtext_entry) > 0:
            self.func_deactivate_buttons()

            for _ in range(time_to_start):
                self.var_text_process.set(str(time_to_start))
                self.update_idletasks()
                time_to_start -= 1
                time.sleep(1)

                self.var_text_process.set(TEXT["HS_writing"])

            if loops_from_loop_slider > 0:
                for _ in range(loops_from_loop_slider):
                    pyautogui.write(text_from_yourtext_entry, interval=delay_from_delay_slider)
            else:
                pyautogui.write(text_from_yourtext_entry, interval=delay_from_delay_slider)

            self.var_text_process.set(time_to_start)
            self.func_activate_buttons()
        else:
            messagebox.showerror(TEXT["error"], TEXT["error_01"])

    def func_init_large_screen(self) -> None:
        """ Large screen """
        global_var.text_from_entry_home_screen = self.entry_your_text.get()
        self.func_deactivate_buttons()
        LargeScreen()

    def func_init_settings_screen(self) -> None:
        """ Settings screen """
        self.func_deactivate_buttons()
        SettingsScreen()

    def func_init_block_screen(self) -> None:
        """ Block Mode screen """
        messagebox.showinfo(message="In development...")
