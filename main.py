from tkinter import *
from tkinter import messagebox, ttk
import keyboard
import time

root = Tk()

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(width="400", height="175", bg="#c33b80")
        self.pack()

############PROCESS####################

        self.wd_label()
        self.wd_button()
        self.m_bar()
        self.wd_ComboBox()
        self.wd_switch()
        self.wd_process()
        self.theme_dark()

############THEMES#####################

    def theme_light(self):
        self.config(bg="#269321")
        self.label_1["bg"] = "#269321"
        self.label_2["bg"] = "#269321"
        self.label_3["bg"] = "#269321"
        self.label_loop["bg"] = "#269321"
        self.label_menuloop["bg"] = "#269321"
        self.label_process["bg"] = "#269321"
        self.label_strProcess["bg"] = "#269321"
        self.switch_button["bg"] = "#269321"
    def theme_dark(self):
        self.config(bg="#010101")
        self.label_1["bg"] = "#010101"
        self.label_2["bg"] = "#010101"
        self.label_3["bg"] = "#010101"
        self.label_loop["bg"] = "#010101"
        self.label_menuloop["bg"] = "#010101"
        self.label_process["bg"] = "#010101"
        self.label_strProcess["bg"] = "#010101"
        self.switch_button["bg"] = "#010101"
    def theme_pink(self):
        self.config(bg="#c33b80")
        self.label_1["bg"] = "#c33b80"
        self.label_2["bg"] = "#c33b80"
        self.label_3["bg"] = "#c33b80"
        self.label_loop["bg"] = "#c33b80"
        self.label_menuloop["bg"] = "#c33b80"
        self.label_process["bg"] = "#c33b80"
        self.label_strProcess["bg"] = "#c33b80"
        self.switch_button["bg"] = "#c33b80"

############LANGUAGE####################

    def lan_spa(self):
        pass
    def lan_eng(self):
        pass
    def lan_rus(self):
        pass

############WIDGETS####################
    def wd_switch(self):
        self.State = 0
        self.image_desactivated = PhotoImage(file="images/switch_1.png")
        self.image_activated = PhotoImage(file="images/switch_2.png")

        def switch(event):
            if self.State == 1:
                self.switch_button.config(image=self.image_desactivated)
                self.switch_str.set("Desactivated")
                self.State = 0
                self.swt_loop()
            else:
                self.switch_button.config(image=self.image_activated)
                self.switch_str.set("Activated")
                self.State = 1
                self.swt_loop()

        self.switch_button = Label(image=self.image_desactivated, bg="#c33b80")
        self.switch_button.bind("<Button-1>", switch)
        self.switch_button.place(x=30, y=15, height=16)

        self.switch_str = StringVar()
        self.switch_str.set("Desactivated")

    def swt_loop(self):
        self.swt = self.switch_str.get()

        if self.swt == "Activated":
            self.box_send["state"] = "readonly"
            self.entry_loop["state"] = NORMAL
            self.label_loop["state"] = NORMAL
        else:
            self.box_send["state"] = "disabled"
            self.entry_loop["state"] = DISABLED
            self.label_loop["state"] = DISABLED

    def wd_ComboBox(self):
        self.send = StringVar()
        self.send.set("None")

        self.box_send = ttk.Combobox(self, values=["None", "Enter", "Shift", "Ctrl", "Backspace", "Space", "Tab"],
        state="disabled", textvariable=self.send)
        self.box_send.place(width=61, height=22,x=10, y=140)

        self.entry_loop = Entry(self, justify=CENTER, state=DISABLED)
        self.entry_loop.place(width="41", height="20",x=20, y=110)

        self.label_loop = Label(self, bg="#c33b80", fg="white", justify=CENTER,state=DISABLED, font=('Arial Black', 8))
        self.label_loop["text"] = "LOOP"
        self.label_loop.place(height=14,x=20, y=90)

        self.label_menuloop = Label(self, bg="#c33b80", fg="white", justify=CENTER, font=('Arial Black', 8))
        self.label_menuloop["text"] = "LOOP MENU"
        self.label_menuloop.place(height=14,x=10, y=1)

    def wd_label(self):
        self.entry_1 = Entry(self, justify=CENTER)
        self.entry_1.place(width="231", height="32",x=80, y=20)
        self.entry_2 = Entry(self, justify=CENTER)
        self.entry_2.place(width="71", height="22",x=160, y=73)

        self.label_1 = Label(self, bg="#c33b80", fg="white", justify=CENTER, font=('Arial Black', 8))
        self.label_1["text"] = "PLACE YOUR TEXT HERE"
        self.label_1.place(height=14, width=190,x=100, y=1)

        self.label_2 = Label(self, bg="#c33b80", fg="white", justify=CENTER, font=('Arial Black', 8))
        self.label_2["text"] = "SET THE DELAY (0 - 1.5)"
        self.label_2.place(height=12, width=190,x=100, y=56)

        self.label_process = Label(self, bg="#c33b80", fg="white", justify=CENTER, font=('Arial Black', 8))
        self.label_process["text"] = ""
        self.label_process.place(height=16,x=195, y=160, anchor="center")

        self.label_3 = Label(self, bg="#c33b80", fg="white", justify=CENTER, font=('Arial Black', 8))
        self.label_3["text"] = "PROCESS"
        self.label_3.place(height=16,x=355, y=80, anchor="center")

    def wd_process(self):
        self.process_str = StringVar()
        self.process_str.set("INACTIVE")

        self.label_strProcess = Label(textvariable=self.process_str, fg="white", justify=CENTER, bg="#c33b80", font=('Arial Black', 8))
        self.label_strProcess.place(height=16,x=355, y=100, anchor="center")

    def wd_button(self):
        self.img_refresh = PhotoImage(file = "images/refresh.png")

        self.playButton = Button(self,state=NORMAL, text="START", command=self.start, font=('Arial Black', 8))
        self.playButton.place(width="90", height="40",x=150, y=110)
        self.refreshButton = Button(self,state=DISABLED, image = self.img_refresh, command=self.restart, font=('Arial Black', 8))
        self.refreshButton.place(width="32", height="32",x=260, y=115)
        self.clearButton = Button(self, text="🗑", command=self.clear, font=('Arial Black', 8))
        self.clearButton.place(width="20", height="20",x=320, y=27)

    def m_bar(self):
        menubar = Menu(self)
        root.config(menu=menubar)
        settings = Menu(menubar, tearoff=0)
        theme = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Options", menu=settings)
        settings.add_cascade(label="Theme", menu=theme)
        settings.add_command(label="Clear All", command=self.clear)
        settings.add_separator()

        settings.add_command(label="About", command=self.about_info)

        theme.add_command(label="Pink", command=self.theme_pink)
        theme.add_command(label="Dark", command=self.theme_dark)
        theme.add_command(label="Green", command=self.theme_light)

############BUTTONS FUNCTIONS####################

    def restart(self):
        self.playButton["state"] = NORMAL
        self.refreshButton["state"] = DISABLED
        self.playButton["text"] = "START"
        self.label_process["text"] = ""
        self.process_str.set("INACTIVE")

    def clear(self):
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)
        self.entry_loop.delete(0, END)

############START####################

    def start(self):
            swt_input = self.switch_str.get()
            
            if swt_input == "Activated":
                txt_input = self.entry_1.get()
                txt_input_2 = self.entry_2.get()
                txt_input_3 = self.entry_loop.get()
                str_input = self.box_send.get()

                if len(txt_input) == 0 or len(txt_input_2) == 0 or len(txt_input_3) == 0:
                    self.label_process["text"] = "Enter text, loop times and delay"
                    self.playButton["state"] = DISABLED
                    self.refreshButton["state"] = NORMAL
                    self.playButton["text"] = "ERROR"
                else:
                    try:
                        delay_input = float(txt_input_2)
                        loop_input = int(txt_input_3)

                        if delay_input < 0 or delay_input > 1.5:
                            self.label_process["text"] = "Wrong delay"
                            self.playButton["state"] = DISABLED
                            self.refreshButton["state"] = NORMAL
                            self.playButton["text"] = "ERROR"

                        elif delay_input == 0:
                            self.label_process["text"] = "Min delay in Loop mode is 0.1"
                            self.playButton["state"] = DISABLED
                            self.refreshButton["state"] = NORMAL
                            self.playButton["text"] = "ERROR"

                        elif loop_input < 0:
                            self.label_process["text"] = "Min loops are 0"
                            self.playButton["state"] = DISABLED
                            self.refreshButton["state"] = NORMAL
                            self.playButton["text"] = "ERROR"

                        elif loop_input > 500:
                            self.label_process["text"] = "Max loops are 500"
                            self.playButton["state"] = DISABLED
                            self.refreshButton["state"] = NORMAL
                            self.playButton["text"] = "ERROR"

                        else:
                            try:
                                if str_input == "None":
                                    self.str_progress()
                                    for i in range(loop_input):
                                        keyboard.write(txt_input, delay=delay_input)
                                        time.sleep(delay_input)
                                    self.process_str.set("FINISHED!")
                                else:
                                    self.str_progress()
                                    for i in range(loop_input):
                                        keyboard.write(txt_input, delay=delay_input)
                                        keyboard.send(str_input)
                                        time.sleep(delay_input)
                                    self.process_str.set("FINISHED!")

                            except:
                                self.label_process["text"] = "An error has occurred"
                                self.playButton["state"] = DISABLED
                                self.refreshButton["state"] = NORMAL
                                self.playButton["text"] = "ERROR"
                                    

                    except:
                        self.label_process["text"] = "Wrong delay or loop times"
                        self.playButton["state"] = DISABLED
                        self.refreshButton["state"] = NORMAL
                        self.playButton["text"] = "ERROR"

            else:
                txt_input = self.entry_1.get()
                txt_input_2 = self.entry_2.get()

                if len(txt_input) == 0 or len(txt_input_2) == 0:
                    self.label_process["text"] = "Enter text and delay"
                    self.playButton["text"] = "ERROR"
                    self.playButton["state"] = DISABLED
                    self.refreshButton["state"] = NORMAL
                else:
                    try:
                        delay = float(txt_input_2)

                        if delay < 0 or delay > 1.5:
                            self.label_process["text"] = "Wrong delay"
                            self.playButton["text"] = "ERROR"
                            self.playButton["state"] = DISABLED
                            self.refreshButton["state"] = NORMAL

                        else:
                            try:
                                self.str_progress()
                                keyboard.write(txt_input, delay=delay)
                                self.process_str.set("FINISHED!")
                                
                            except:
                                self.label_process["text"] = "An error has occurred"
                                self.playButton["text"] = "ERROR"
                                self.playButton["state"] = DISABLED
                                self.refreshButton["state"] = NORMAL
                    except:
                        self.label_process["text"] = "Wrong delay"
                        self.playButton["text"] = "ERROR"
                        self.playButton["state"] = DISABLED
                        self.refreshButton["state"] = NORMAL

    def str_progress(self):
        self.process_str.set("               ")
        self.update_idletasks()
        time.sleep(0.2)
        self.playButton["state"] = DISABLED
        self.refreshButton["state"] = NORMAL
        self.process_str.set("3")
        self.update_idletasks()
        time.sleep(1)
        self.process_str.set("2")
        self.update_idletasks()
        time.sleep(1)
        self.process_str.set("1")
        self.update_idletasks()
        time.sleep(1)
        self.process_str.set("LOADING...")
        self.update_idletasks()

    def about_info(self):
        messagebox.showinfo("About",
        "#############################################\n"
        "                      ABOUT AUTOMATIC KEYBOARD\n"
        "\nAuto Keyboard is an open source application created in order to practice in my learning journey with python, it is for this reason that there may be things that are not done in the most optimal way, keep in mind that I am learning."
        "\n\nHow does it work?"
        "\n\n                                    NORMAL MODE"
        "\nIn normal mode you just have to place the text you want to write automatically"
        "\nin the \"text\" area you place the text you want to automate"
        "\nin the \"delay\" area you put the time it will take between each keyboard"
        "\n(WARNING: you must take into account that the time is in seconds, so if you put a high delay the task can take too long)"
        "\n\n                                       LOOP MODE"
        "\nThe loop mode works differently, it works for a repetition task (for example writing the same thing many times)"
        "\n\nin the \"text\" area you place the text you intend to repeat"
        "\nin the \"delay\" area you place the time it will take between each key"
        "\nin the \"loop\" area you place the number of times the process will be repeated"
        "\nin the \"special key\" area you can select a special key every time the loop ends"
        "\n#############################################"
        "\nversion 2.0.0                                                     -MADE BY PJOSEP"
        )

root.title("Automatic Keyboard V2")
root.iconbitmap("icon.ico")
root.resizable(0, 0)
root.geometry("400x192")

app = Application(master=root)
app.mainloop()