import tkinter as tk

class Button:
    def __init__(self, frame, text, bgcolor, bindcolor, fgcolor, font, sizefont, command, state, coordX, coordY, width, height):
        self.frame = frame
        self.text = text
        self.bgcolor = bgcolor
        self.bindcolor = bindcolor
        self.fgcolor = fgcolor
        self.font = font
        self.sizefont = sizefont
        self.command = command
        self.state = state
        self.coordX = coordX
        self.coordY = coordY
        self.width = width
        self.height = height
        self.create()

    def create(self):
        def on_enter(x):
            self.globalButton["background"] = self.bindcolor
        def on_leave(x):
            self.globalButton["background"] = self.bgcolor

        self.globalButton = tk.Button(self.frame,state=self.state, textvariable=self.text, border=0, bg=self.bgcolor, fg=self.fgcolor, command=self.command, font=(self.font, self.sizefont))    
            
        self.globalButton.bind("<Enter>", on_enter)
        self.globalButton.bind("<Leave>", on_leave)
        self.globalButton.place(x=self.coordX, y=self.coordY, width=self.width, height=self.height)

    def off(self):
        self.globalButton["state"] = "disabled"

    def on(self):
        self.globalButton["state"] = "normal"

class ImgButton(Button):
    def __init__(self, frame, text, bgcolor, bindcolor, fgcolor, font, sizefont, command, state, coordX, coordY, width, height):
        super().__init__(frame, text, bgcolor, bindcolor, fgcolor, font, sizefont, command, state, coordX, coordY, width, height)

    def create(self):
        def on_enter(x):
            self.globalButton["background"] = self.bindcolor
        def on_leave(x):
            self.globalButton["background"] = self.bgcolor

        self.globalButton = tk.Button(self.frame,state=self.state, image=self.text, border=0, bg=self.bgcolor, fg=self.fgcolor, command=self.command, font=(self.font, self.sizefont))    
            
        self.globalButton.bind("<Enter>", on_enter)
        self.globalButton.bind("<Leave>", on_leave)
        self.globalButton.place(x=self.coordX, y=self.coordY, width=self.width, height=self.height)