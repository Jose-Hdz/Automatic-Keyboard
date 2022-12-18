from tkinter import *
from tkinter import messagebox
import keyboard, time, objects as obj, pickle, tkinter.ttk as ttk

#Configuracion por defecto
DEFAULT_CONFIG = {"language":"English", "theme":"Dark", "splashscreen":True, "timetostart":3}
#Directorios
DIR_IMG = "./resources/images/"; DIR_ICONS = "./resources/icons/"

configuration = open("./config.ak", "ab+")
configuration.seek(0) #Mover el cursor al principio del archivo
try: #Intentar cargar la informacion del archivo
    config = pickle.load(configuration)
except: #Si esta vacio, agregar las configuraciones por defecto
    configuration = open("./config.ak", "wb") #Abrir el archivo en modo escritura
    pickle.dump(DEFAULT_CONFIG, configuration) #Agregar la informacion por defecto
    configuration.close()
    configuration = open("./config.ak", "ab+")
    configuration.seek(0) #Mover el cursor al principio del archivo
    config = pickle.load(configuration)
finally: #Cerrar el archivo y borrar la variable
    configuration.close()
    del(configuration)

#Paleta de colores
if config["theme"] == "Blue":
    PL_BLUE = "#c9c9ff"; PL_WHITE = "#ffffff"; PL_GREEN = "#e1f7d5"; PL_PINK = "#ffbdbd"; PL_PURPLE = "#f1cbff"; PL_BLACK = "#30302e"
elif config["theme"] == "Dark":
    PL_BLUE = "#30302e"; PL_WHITE = "#ffffff"; PL_GREEN = "#e1f7d5"; PL_PINK = "#ffbdbd"; PL_PURPLE = "#f1cbff"; PL_BLACK = "#30302e"
elif config["theme"] == "Pink":
    PL_BLUE = "#ffbdbd"; PL_WHITE = "#ffffff"; PL_GREEN = "#e1f7d5"; PL_PINK = "#c9c9ff"; PL_PURPLE = "#f1cbff"; PL_BLACK = "#30302e"
elif config["theme"] == "Purple":
    PL_BLUE = "#f1cbff"; PL_WHITE = "#ffffff"; PL_GREEN = "#e1f7d5"; PL_PINK = "#c9c9ff"; PL_PURPLE = "#ffbdbd"; PL_BLACK = "#30302e"

#Ventana principal
class AkHome:
    #Constructor
    def __init__(self):
        #Crear Ventana
        self.root = Tk()
        #Informacion sobre la ventana (posicion, tamaño, etc)
        self.screenwidth = self.root.winfo_screenwidth() #Toma las medidas a lo ancho
        self.screenheight = self.root.winfo_screenheight() #Toma las medidas a lo largo
        #Medidas de la pantalla y de la ventana para centrar ventana al inicializarla
        self.root_width = 500 #Medidas iniciales a lo ancho
        self.root_height = 200 #Medidas iniciales a lo largo
        self.root_x = (self.screenwidth/2) - (self.root_width/2) #Coordenadas x donde inicializara la ventana
        self.root_y = (self.screenheight/2) - (self.root_height/2) #Coordenadas y donde inicializara la ventana
        self.root.iconbitmap("./icon.ico")
        #Configurar ventana
        self.root.geometry("%dx%d+%d+%d" % (self.root_width, self.root_height, self.root_x, self.root_y))
        self.root.title("Automatic Keyboard v3")
        self.root.resizable(0,0)
        #Configuracion por defecto
        self.config = config
        #Cargar o crear archivo de configuracion
        #Variables iniciales
        self.timetostart = self.config["timetostart"]
        #Frames
        self.bg = Frame(self.root, bg=PL_BLUE, width=500, height=200)
        self.bg.pack()
        #Funciones iniciales
        if config["language"] == "English":
            self.english()
        elif config["language"] == "Spanish":
            self.spanish()
        self.widgets()
        self.func_switch_specialkey()
        #Inicializar ventana
        self.root.mainloop()
    #Lenguajes
    def english(self):
        #Crear los textos usados en el programa en el idioma ingles
        #TEXTOS CONSTANTES ---------------------- BEGIN
        self.str_cancel = StringVar()
        self.str_cancel.set("CANCEL")
        self.str_accept = StringVar()
        self.str_accept.set("ACCEPT")
        #TEXTOS CONSTANTES ---------------------- END

        #TEXTOS HOME ---------------------- BEGIN
        #Textos de los "labels"
        self.str_yourText = StringVar()
        self.str_yourText.set("YOUR TEXT")
        self.str_delayText = StringVar()
        self.str_delayText.set("DELAY")

        #Textos de los botones
        self.str_delText = StringVar()
        self.str_delText.set("DEL")
        self.str_largueText = StringVar()
        self.str_largueText.set("LAR")
        self.str_loopmodeText = StringVar()
        self.str_loopmodeText.set("LOOP MODE")
        self.str_startText = StringVar()
        self.str_startText.set("START")

        #Textos de los procesos
        self.str_processText = StringVar()
        self.str_processText.set("PROGRESS INACTIVE")

        self.str_processText_normalstart = "START IN"
        self.str_processText_writing = "WRITING"
        self.str_processText_done = "DONE"
        # TEXTOS HOME ---------------- END

        # TEXTOS LARGE ----------------- BEGIN
        self.str_largetitle = StringVar()
        self.str_largetitle.set("LARGE TEXT")
        self.str_largeready = StringVar()
        self.str_largeready.set("READY")
        # TEXTOS LARGE ----------------- END

        # TEXTOS SETTINGS ----------------- BEGIN
        self.str_settings_title = StringVar()
        self.str_settings_title.set("SETTINGS")
        self.str_settings_titletheme = StringVar()
        self.str_settings_titletheme.set("Theme")
        self.str_settings_titlelanguage = StringVar()
        self.str_settings_titlelanguage.set("Language")
        self.str_settings_titlesplash = StringVar()
        self.str_settings_titlesplash.set("Splash Screen")
        self.str_settings_titletimestart = StringVar()
        self.str_settings_titletimestart.set("Time to start")
        #Textos de los botones
        self.str_settings_themeblue = StringVar()
        self.str_settings_themeblue.set("BLUE")
        self.str_settings_themedark = StringVar()
        self.str_settings_themedark.set("DARK")
        self.str_settings_themepink = StringVar()
        self.str_settings_themepink.set("PINK")
        self.str_settings_themepurple = StringVar()
        self.str_settings_themepurple.set("PURPLE")
        #Lenguajes
        self.str_settings_languageeng = StringVar()
        self.str_settings_languageeng.set("ENGLISH")
        self.str_settings_languagespa = StringVar()
        self.str_settings_languagespa.set("ESPAÑOL")
        #Splash Screen
        self.str_settings_sson = StringVar()
        self.str_settings_sson.set("ON")
        self.str_settings_ssoff = StringVar()
        self.str_settings_ssoff.set("OFF")
        #Time to start
        self.str_settings_timestart3 = StringVar()
        self.str_settings_timestart3.set("3 sec")
        self.str_settings_timestart5 = StringVar()
        self.str_settings_timestart5.set("5 sec")
        self.str_settings_timestart10 = StringVar()
        self.str_settings_timestart10.set("10 sec")
        
        #Selecciones
        self.str_settings_selectiontheme = StringVar()
        self.str_settings_selectiontheme.set("Blue")
        self.str_settings_selectionlanguage = StringVar()
        self.str_settings_selectionlanguage.set("English")
        self.str_settings_selectionss = StringVar()
        self.str_settings_selectionss.set("On")
        self.str_settings_selectiontimestart = StringVar()
        self.str_settings_selectiontimestart.set("3")

        self.str_settings_selectiontheme_blue = "Blue"
        self.str_settings_selectiontheme_dark = "Dark"
        self.str_settings_selectiontheme_pink = "Pink"
        self.str_settings_selectiontheme_purple = "Purple"
        self.str_settings_selectionlanguage_eng = "English"
        self.str_settings_selectionlanguage_spa = "Spanish"
        self.str_settings_selectionss_on = "On"
        self.str_settings_selectionss_off = "Off"
        self.str_settings_selectiontimestart_3 = "3"
        self.str_settings_selectiontimestart_5 = "5"
        self.str_settings_selectiontimestart_10 = "10"

        #Checkboxs
        self.str_settings_splashscreen = StringVar()
        self.str_settings_splashscreen.set("Splash Screen")
        self.str_settings_timetostart = StringVar()
        self.str_settings_timetostart.set("Time to start")
        
        #Textos al aceptar los cambios
        self.str_settings_warning = StringVar()
        self.str_settings_warning.set("Warning")
        self.str_settings_warningtext = StringVar()
        self.str_settings_warningtext.set("Restart the program to make the changes")

        # TEXTOS SETTINGS ----------------- END

        # TEXTOS LOOP --------------------- BEGIN
        self.str_loop_loops = StringVar()
        self.str_loop_loops.set("LOOPS")
        self.str_loop_specialkey = StringVar()
        self.str_loop_specialkey.set("SPECIAL KEY")
        # TEXTOS LOOP --------------------- END

        #Textos de errores
        self.str_processText_error00 = "AN ERROR HAS OCURRED"
        self.str_processText_error01 = "ENTER TEXT AND DELAY"
        self.str_processText_error02 = "WRONG DELAY"
        self.str_processText_error03 = "DELAY MIN 0 & MAX 1.5"
        self.str_processText_error04 = "EMPTY ENTRIES"
        self.str_processText_error05 = "WRONG DELAY OR LOOPS"
        self.str_processText_error06 = "LOOPS MIN 1 & MAX 500"
    
    def spanish(self):
        #Crear los textos usados en el programa en el idioma ingles
        #TEXTOS CONSTANTES ---------------------- BEGIN
        self.str_cancel = StringVar()
        self.str_cancel.set("CANCELAR")
        self.str_accept = StringVar()
        self.str_accept.set("ACEPTAR")
        #TEXTOS CONSTANTES ---------------------- END

        #TEXTOS HOME ---------------------- BEGIN
        #Textos de los "labels"
        self.str_yourText = StringVar()
        self.str_yourText.set("TEXTO")
        self.str_delayText = StringVar()
        self.str_delayText.set("RETRASO")

        #Textos de los botones
        self.str_delText = StringVar()
        self.str_delText.set("DEL")
        self.str_largueText = StringVar()
        self.str_largueText.set("LAR")
        self.str_loopmodeText = StringVar()
        self.str_loopmodeText.set("LOOP MODE")
        self.str_startText = StringVar()
        self.str_startText.set("COMENZAR")

        #Textos de los procesos
        self.str_processText = StringVar()
        self.str_processText.set("PROGRESO INACTIVO")

        self.str_processText_normalstart = "COMIENZA EN"
        self.str_processText_writing = "ESCRIBIENDO"
        self.str_processText_done = "LISTO"
        # TEXTOS HOME ---------------- END

        # TEXTOS LARGE ----------------- BEGIN
        self.str_largetitle = StringVar()
        self.str_largetitle.set("TEXTO LARGO")
        self.str_largeready = StringVar()
        self.str_largeready.set("LISTO")
        # TEXTOS LARGE ----------------- END

        # TEXTOS SETTINGS ----------------- BEGIN
        self.str_settings_title = StringVar()
        self.str_settings_title.set("AJUSTES")
        self.str_settings_titletheme = StringVar()
        self.str_settings_titletheme.set("Tema")
        self.str_settings_titlelanguage = StringVar()
        self.str_settings_titlelanguage.set("Lenguaje")
        self.str_settings_titlesplash = StringVar()
        self.str_settings_titlesplash.set("Pantalla de carga")
        self.str_settings_titletimestart = StringVar()
        self.str_settings_titletimestart.set("Retraso")
        #Textos de los botones
        self.str_settings_themeblue = StringVar()
        self.str_settings_themeblue.set("AZUL")
        self.str_settings_themedark = StringVar()
        self.str_settings_themedark.set("OSCURO")
        self.str_settings_themepink = StringVar()
        self.str_settings_themepink.set("ROSA")
        self.str_settings_themepurple = StringVar()
        self.str_settings_themepurple.set("MORADO")
        #Lenguajes
        self.str_settings_languageeng = StringVar()
        self.str_settings_languageeng.set("INGLES")
        self.str_settings_languagespa = StringVar()
        self.str_settings_languagespa.set("ESPAÑOL")
        #Splash Screen
        self.str_settings_sson = StringVar()
        self.str_settings_sson.set("ENCENDIDO")
        self.str_settings_ssoff = StringVar()
        self.str_settings_ssoff.set("APAGADO")
        #Time to start
        self.str_settings_timestart3 = StringVar()
        self.str_settings_timestart3.set("3 seg")
        self.str_settings_timestart5 = StringVar()
        self.str_settings_timestart5.set("5 seg")
        self.str_settings_timestart10 = StringVar()
        self.str_settings_timestart10.set("10 seg")
        
        #Selecciones
        self.str_settings_selectiontheme = StringVar()
        self.str_settings_selectiontheme.set("Blue")
        self.str_settings_selectionlanguage = StringVar()
        self.str_settings_selectionlanguage.set("English")
        self.str_settings_selectionss = StringVar()
        self.str_settings_selectionss.set("On")
        self.str_settings_selectiontimestart = StringVar()
        self.str_settings_selectiontimestart.set("3")

        self.str_settings_selectiontheme_blue = "Blue"
        self.str_settings_selectiontheme_dark = "Dark"
        self.str_settings_selectiontheme_pink = "Pink"
        self.str_settings_selectiontheme_purple = "Purple"
        self.str_settings_selectionlanguage_eng = "English"
        self.str_settings_selectionlanguage_spa = "Spanish"
        self.str_settings_selectionss_on = "On"
        self.str_settings_selectionss_off = "Off"
        self.str_settings_selectiontimestart_3 = "3"
        self.str_settings_selectiontimestart_5 = "5"
        self.str_settings_selectiontimestart_10 = "10"

        #Checkboxs
        self.str_settings_splashscreen = StringVar()
        self.str_settings_splashscreen.set("Splash Screen")
        self.str_settings_timetostart = StringVar()
        self.str_settings_timetostart.set("Time to start")
        
        #Textos al aceptar los cambios
        self.str_settings_warning = StringVar()
        self.str_settings_warning.set("Aviso")
        self.str_settings_warningtext = StringVar()
        self.str_settings_warningtext.set("Reinicia el programa para realizar los cambios")

        # TEXTOS SETTINGS ----------------- END

        # TEXTOS LOOP --------------------- BEGIN
        self.str_loop_loops = StringVar()
        self.str_loop_loops.set("LOOPS")
        self.str_loop_specialkey = StringVar()
        self.str_loop_specialkey.set("TECLA ESPECIAL")
        # TEXTOS LOOP --------------------- END

        #Textos de errores
        self.str_processText_error00 = "HA OCURRIDO UN ERROR"
        self.str_processText_error01 = "TEXTO Y DELAY VACIOS"
        self.str_processText_error02 = "DELAY INCORRECTO"
        self.str_processText_error03 = "DELAY MIN 0 & MAX 1.5"
        self.str_processText_error04 = "ENTRADAS VACIAS"
        self.str_processText_error05 = "DELAY,LOOPS INCORRECTO"
        self.str_processText_error06 = "LOOPS MIN 1 & MAX 500"
    #Widgets y ventanas
    def widgets(self): #Widgets ventana principal
        #Labels
        self.label_yourtext = Label(self.bg, textvariable=self.str_yourText, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 24), anchor=W)
        self.label_yourtext.place(x=10, y=15, width=190, height=30)
        self.label_delaytext = Label(self.bg, textvariable=self.str_delayText, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 20), anchor=W)
        self.label_delaytext.place(x=10, y=100, width=150, height=30)
        self.label_loopstext = Label(self.bg, textvariable=self.str_loop_loops, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 20), anchor=W)
        self.label_loopstext.place(x=140, y=100, width=110, height=30)

        self.label_specialkey = Label(self.bg, textvariable=self.str_loopmodeText, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 10), wraplength=80, justify=CENTER)
        self.label_specialkey.place(x=220, y=20, width=80, height=30)
        self.label_process = Label(self.bg, textvariable=self.str_processText, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 14), wraplength=150, justify=CENTER)
        self.label_process.place(x=360, y=60, width=140, height=50)

        #Entrys
        self.entry_text = Entry(self.bg, fg=PL_BLACK, font=("Sono Light", 10), justify=CENTER)
        self.entry_text.place(x=10, y=60, width=220, height=30)
        self.entry_delay = Entry(self.bg, fg=PL_BLACK, font=("Sono Light", 10), justify=CENTER)
        self.entry_delay.place(x=10, y=140, width=100, height=30)
        self.entry_delay.insert(0, 0.1)
        self.entry_loop = Entry(self.bg, fg=PL_BLACK, font=("Sono Light", 10), justify=CENTER, state=DISABLED)
        self.entry_loop.place(x=140, y=140, width=90, height=30)

        #Buttons || Botones personalizados importados de el archivo objetos
        self.button_start = obj.Button(self.bg, self.str_startText, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 15, self.func_start, NORMAL, 370, 120, 120, 50)
        #Cargar iconos
        self.img_settings = PhotoImage(file=DIR_ICONS + "settings.png")
        self.img_delete = PhotoImage(file=DIR_ICONS + "delete.png")
        self.img_large = PhotoImage(file=DIR_ICONS + "large.png")
        #Crear botones con imagenes
        self.button_settings = obj.ImgButton(self.bg, self.img_settings, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.AkSettings, NORMAL, 460, 20, 30, 30)
        self.button_del = obj.ImgButton(self.bg, self.img_delete, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.func_del, NORMAL, 240, 60, 30, 30)
        self.button_large = obj.ImgButton(self.bg, self.img_large, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.AkLargeText, NORMAL, 280, 60, 30, 30)
        #ComboBox
        self.specialkey_var = StringVar()
        self.specialkey_var.set("None")
        self.combo_specialkey = ttk.Combobox(self.bg, values=["None", "Enter", "Shift", "Ctrl", "Backspace", "Space", "Tab"], state=DISABLED, textvariable=self.specialkey_var)
        self.combo_specialkey.place(x=270, y=145, width=70, height=20)

    def AkSettings(self): #Ventana ajustes
        #Desativar el boton settings
        self.button_settings.off()
        #Tomar la posicion de la ventana home y crear las medidas de la ventana Settings
        self.settings_x = self.root.winfo_x()
        self.settings_y = self.root.winfo_y()
        self.settings_width = 500
        self.settings_height = 400
        #Crear la ventana y configurarla
        self.toplevel_settings = Toplevel()
        self.toplevel_settings.geometry("%dx%d+%d+%d" % (self.settings_width, self.settings_height, self.settings_x, self.settings_y))
        self.toplevel_settings.resizable(0,0)
        #Crear frames
        self.settings_bg = Frame(self.toplevel_settings, bg=PL_BLUE, width=500, height=400)
        self.settings_bg.pack()
        #Widgets
        #Labels
        self.label_settings_title = Label(self.settings_bg, textvariable=self.str_settings_title, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 20))
        self.label_settings_title.place(x=150, y=10, width=200, height=40)
        self.label_settings_titletheme = Label(self.settings_bg, textvariable=self.str_settings_titletheme, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 20), anchor=W)
        self.label_settings_titletheme.place(x=20, y=50, width=110, height=30)
        self.label_settings_titlelanguage = Label(self.settings_bg, textvariable=self.str_settings_titlelanguage, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 20), anchor=W)
        self.label_settings_titlelanguage.place(x=20, y=130, width=150, height=30)
        self.label_settings_titlesplash = Label(self.settings_bg, textvariable=self.str_settings_titlesplash, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 20), anchor=W)
        self.label_settings_titlesplash.place(x=20, y=210, width=300, height=30)
        self.label_settings_titletimestart = Label(self.settings_bg, textvariable=self.str_settings_titletimestart, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 20), anchor=W)
        self.label_settings_titletimestart.place(x=20, y=290, width=230, height=30)
        #Opciones seleccionadas
        self.label_settings_selectionlanguage = Label(self.settings_bg, textvariable=self.str_settings_selectionlanguage, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 13))
        self.label_settings_selectionlanguage.place(x=190, y=170, width=90, height=30)
        self.label_settings_selectiontheme = Label(self.settings_bg, textvariable=self.str_settings_selectiontheme, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 13))
        self.label_settings_selectiontheme.place(x=350, y=90, width=80, height=30)
        self.label_settings_selectionss = Label(self.settings_bg, textvariable=self.str_settings_selectionss, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 13))
        self.label_settings_selectionss.place(x=190, y=250, width=90, height=30)
        self.label_settings_selectiontimestart = Label(self.settings_bg, textvariable=self.str_settings_selectiontimestart, bg=PL_BLUE, fg=PL_WHITE, font=("Sono SemiBold", 13))
        self.label_settings_selectiontimestart.place(x=260, y=330, width=50, height=30)
        #Botones Temas
        self.button_settings_bluetheme = obj.Button(self.settings_bg, self.str_settings_themeblue, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.func_settings_themeblue, NORMAL, 20, 90, 70, 30)
        self.button_settings_darktheme = obj.Button(self.settings_bg, self.str_settings_themedark, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.func_settings_themedark, NORMAL, 100, 90, 70, 30)
        self.button_settings_pinktheme = obj.Button(self.settings_bg, self.str_settings_themepink, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.func_settings_themepink, NORMAL, 180, 90, 70, 30)
        self.button_settings_purpletheme = obj.Button(self.settings_bg, self.str_settings_themepurple, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.func_settings_themepurple, NORMAL, 260, 90, 70, 30)
        #Botones lenguajes
        self.button_settings_eng = obj.Button(self.settings_bg, self.str_settings_languageeng, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.func_settings_languageeng, DISABLED, 20, 170, 70, 30)
        self.button_settings_spa = obj.Button(self.settings_bg, self.str_settings_languagespa, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.func_settings_languagespa, NORMAL, 100, 170, 70, 30)
        #Botones Splash Screen
        self.button_settings_sson = obj.Button(self.settings_bg, self.str_settings_sson, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.func_settings_splashon, NORMAL, 20, 250, 70, 30)
        self.button_settings_ssoff = obj.Button(self.settings_bg, self.str_settings_ssoff, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.func_settings_splashoff, NORMAL, 100, 250, 70, 30)
        #Botones Time to Start
        self.button_settings_timestart3 = obj.Button(self.settings_bg, self.str_settings_timestart3, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.func_settings_timestart3, NORMAL, 20, 330, 70, 30)
        self.button_settings_timestart5 = obj.Button(self.settings_bg, self.str_settings_timestart5, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.func_settings_timestart5, NORMAL, 100, 330, 70, 30)
        self.button_settings_timestart10 = obj.Button(self.settings_bg, self.str_settings_timestart10, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.func_settings_timestart10, NORMAL, 180, 330, 70, 30)
        #Definir botones por defecto de los temas
        if config["theme"] == "Blue":
            self.func_settings_themeblue()
        elif config["theme"] == "Dark":
            self.func_settings_themedark()
        elif config["theme"] == "Pink":
            self.func_settings_themepink()
        elif config["theme"] == "Purple":
            self.func_settings_themepurple()
        #Definir botones por defecto de los Lenguajes
        if config["language"] == "English":
            self.func_settings_languageeng()
        elif config["language"] == "Spanish":
            self.func_settings_languagespa()
        #Definir botones por defecto de la pantalla de carga
        if config["splashscreen"] == True:
            self.func_settings_splashon()
        elif config["splashscreen"] == False:
            self.func_settings_splashoff()
        #Definir botones por defecto de la pantalla del tiempo de espera
        if config["timetostart"] == 3:
            self.func_settings_timestart3()
        elif config["timetostart"] == 5:
            self.func_settings_timestart5()
        elif config["timetostart"] == 10:
            self.func_settings_timestart10()
        


        #Botones aceptar y cancelar
        self.button_settings_accept = obj.Button(self.settings_bg, self.str_accept, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.func_settings_accept, NORMAL, 410, 350, 70, 30)
        self.button_settings_cancel = obj.Button(self.settings_bg, self.str_cancel, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 9, self.close_AkSettings, NORMAL, 330, 350, 70, 30)
        #Cuando se cierre la ventana llamar a la funcion para activar el boton "Settings"
        self.toplevel_settings.protocol("WM_DELETE_WINDOW", self.close_AkSettings)

    def AkLargeText(self): #Ventana textos grandes
        #Tomar la posicion de la ventana home y crear las medidas de la ventana large
        self.large_x = self.root.winfo_x()
        self.large_y = self.root.winfo_y()
        self.large_width = 500
        self.large_height = 400
        #Desactivar el boton "Large"
        self.button_large.off()
        #Crear ventana y configurarla
        self.toplevel_large = Toplevel()
        self.toplevel_large.geometry("%dx%d+%d+%d" % (self.large_width, self.large_height, self.large_x, self.large_y))
        self.toplevel_large.resizable(0,0)
        #Crear frames
        self.large_topframe = Frame(self.toplevel_large, width=500, height=30, bg=PL_WHITE)
        self.large_topframe.pack()
        self.large_centerframe = Frame(self.toplevel_large, width=500, height=370, bg=PL_BLUE)
        self.large_centerframe.pack()
        #Widgets
        #Labels
        self.label_largetext = Label(self.large_topframe, textvariable=self.str_largetitle, bg=PL_WHITE, fg=PL_BLACK, font=("Sono SemiBold", 14))
        self.label_largetext.place(x=0, y=0, width=130, height=30)
        #self.label_largeload = Label(self.large_topframe, textvariable=self.str_largeload, bg=PL_WHITE, fg=PL_BLACK, font=("Sono SemiBold", 14), anchor=E)
        #self.label_largeload.place(x=140, y=0, width=90, height=30)
        #self.label_largesave = Label(self.large_topframe, textvariable=self.str_largesave, bg=PL_WHITE, fg=PL_BLACK, font=("Sono SemiBold", 14), anchor=E)
        #self.label_largesave.place(x=260, y=0, width=90, height=30)
        self.label_largeready = Label(self.large_topframe, textvariable=self.str_largeready, bg=PL_WHITE, fg=PL_BLACK, font=("Sono SemiBold", 14), anchor=E)
        self.label_largeready.place(x=380, y=0, width=90, height=30)

        #Cargar imagenes
        self.img_load = PhotoImage(file=DIR_ICONS + "files.png")
        self.img_save = PhotoImage(file=DIR_ICONS + "doc.png")
        self.img_ready = PhotoImage(file=DIR_ICONS + "large.png")
        #Buttons
        #self.button_largeload = obj.ImgButton(self.large_topframe, self.img_load, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 8, None, NORMAL, 230, 0, 30, 30)
        #self.button_largesave = obj.ImgButton(self.large_topframe, self.img_save, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 8, None, NORMAL, 350, 0, 30, 30)
        self.button_largeready = obj.ImgButton(self.large_topframe, self.img_ready, PL_WHITE, PL_PURPLE, PL_BLACK, "Sono SemiBold", 8, self.func_large_ready, NORMAL, 470, 0, 30, 30)

        #Text Box
        self.large_textbox = Text(self.large_centerframe, bg=PL_WHITE, fg=PL_BLACK, font=("Sono Light", 10))
        self.large_textbox.place(x=10, y=10, width=480, height=350)

        #Cuando se cierre la ventana llamar a la funcion para activar el boton "large"
        self.toplevel_large.protocol("WM_DELETE_WINDOW", self.close_AkLargeText)
    
    #Funciones de cierre
    def close_AkLargeText(self): #Cerrar la ventana de textos grandes
        #Destruir la ventana large
        self.toplevel_large.destroy()
        #Activar el boton large
        self.button_large.on()

    def close_AkSettings(self): #Cerrar la ventana de ajustes
        self.toplevel_settings.destroy()
        self.button_settings.on()
    
    #Funciones Home
    def func_del(self): #Eliminar el texto de el entry y cambiar el delay a 0.1
        #Eliminar texto de los entrys "delay y text", luego insertar el valor "0.1" en el entry delay
        self.entry_delay.delete(0, END)
        self.entry_delay.insert(0, 0.1)
        self.entry_text.delete(0, END)

    def func_start(self): #Comenzar el proceso de escritura automatica 
        if self.switch_state == 1:
            self.func_start_loop()
        else:
            self.func_start_normal()

    def func_start_normal(self): #Si el loop mode esta desactivado
        #Obtener el texto de los entrys "Text y Delay"
        self.entry_text_value = self.entry_text.get()
        self.entry_delay_value = self.entry_delay.get()

        #Si el campo texto o el campo delay estan vacios entonces marcar un error
        if len(self.entry_text_value) == 0 or len(self.entry_delay_value) == 0:
            self.str_processText.set(self.str_processText_error01)
        #Caso contrario
        else:
            #Intentar convertir el delay en un numero flotante
            try:
                self.delay_value = float(self.entry_delay_value)
                #Si el delay excede el valor minimo y maximo asignados marcar un error
                if self.delay_value < 0 or self.delay_value > 1.5:
                    self.str_processText.set(self.str_processText_error03)
                #Caso contrario intentar correr la funcion de proceso
                else:
                    try:
                        #intentar correr la funcion de el proceso
                        self.func_process_normal()
                    except:
                        #Error desconocido >> error00
                        self.str_processText.set(self.str_processText_error00)
            #Si el campo delay es texto marcar un error
            except:
                self.str_processText.set(self.str_processText_error02)

    def func_start_loop(self): #Si el loop mode esta activado
        #Obtener el texto de los entrys "Text, Loops, Delay"
        self.entry_text_value = self.entry_text.get()
        self.entry_delay_value = self.entry_delay.get()
        self.entry_loop_value = self.entry_loop.get()

        #Si el campo texto o el campo delay estan vacios entonces marcar un error
        if len(self.entry_text_value) == 0 or len(self.entry_delay_value) == 0 or len(self.entry_loop_value) == 0:
            self.str_processText.set(self.str_processText_error04)
        #Caso contrario
        else:
            try:
                #Intentar convertir el delay y los loops a numeros flotantes
                self.delay_value = float(self.entry_delay_value)
                self.loop_value = int(self.entry_loop_value)
                #Si el delay es menor a 0 o mayor a 1.5 marcar un error
                if self.delay_value < 0 or self.delay_value > 1.5:
                    self.str_processText.set(self.str_processText_error03)
                #Si los loops son menores a 1 o mayores a 500 marcar un error
                elif self.loop_value < 1 or self.loop_value > 500:
                    self.str_processText.set(self.str_processText_error06)
                else:
                    try:
                        self.func_process_loops()
                    except:
                        self.str_processText.set(self.str_processText_error00)
            except:
                #Caso contrario marcar un error
                self.str_processText.set(self.str_processText_error05)

    def func_process_normal(self): #Comenzar el conteo antes de comenzar a escribir
        #Asignar el valor de los segundos de espera a el contador
        self.processText_counter = self.timetostart
        #Crear un bucle for con el numero de segundos para comenzar
        for x in range(self.timetostart):
            #en cada segundo eliminar 1 a el contador y actualizar el texto de proceso
            self.str_processText.set(f"{self.str_processText_normalstart}: {self.processText_counter}")
            self.processText_counter = self.processText_counter - 1
            self.root.update_idletasks()
            time.sleep(1)
        #Actualizar el texto de proceso
        self.str_processText.set(self.str_processText_writing)
        self.root.update_idletasks()
        #Iniciar a teclear automaticamente el texto ingresado por el usuario
        keyboard.write(self.entry_text_value, delay=self.delay_value)
        #Actualizar el texto de proceso
        self.str_processText.set(self.str_processText_done)
        self.root.update_idletasks() #Actualizar pantalla
    
    def func_process_loops(self): #Comenzar el conteo antes de comenzar a escribir
        #Asignar el valor de los segundos de espera a el contador
        self.processText_counter = self.timetostart
        #Leer el estado de la tecla especial
        self.specialkey_value = self.specialkey_var.get()
        #Crear un bucle for con el numero de segundos para comenzar
        for x in range(self.timetostart):
            #en cada segundo eliminar 1 a el contador y actualizar el texto de proceso
            self.str_processText.set(f"{self.str_processText_normalstart}: {self.processText_counter}")
            self.processText_counter = self.processText_counter - 1
            self.root.update_idletasks()
            time.sleep(1)
        #Actualizar el texto de proceso
        self.str_processText.set(self.str_processText_writing)
        self.root.update_idletasks()
        #Si la tecla especial esta desactivada
        if self.specialkey_value == "None":
            #Iniciar a teclear automaticamente el texto ingresado por el usuario
            for i in range(self.loop_value):
                keyboard.write(self.entry_text_value, delay=self.delay_value)
        #Si la tecla especial esta activada
        else:
            #Iniciar a teclear automaticamente el texto ingresado por el usuario
            for i in range(self.loop_value):
                keyboard.write(self.entry_text_value, delay=self.delay_value)
                keyboard.send(self.specialkey_value)
        
        #Actualizar el texto de proceso
        self.str_processText.set(self.str_processText_done)
        self.root.update_idletasks() #Actualizar pantalla

    #Funciones textos grandes
    def func_large_ready(self): #Guardar el texto escrito y colocarlo en el entry de el texto
        #Eliminar el texto de el entry text
        self.entry_text.delete(0, END)
        #Guardar el texto de el textbox
        self.largetext_save = self.large_textbox.get(1.0, END)
        #Insertar el texto en el entry text
        self.entry_text.insert(0, self.largetext_save[:-1])
        #Ejecutar el cerrar ventana
        self.close_AkLargeText()
    #Funciones ajustes
    def func_settings_themeblue(self): #Desactivar el boton presionado y activar los demas
        self.button_settings_bluetheme.off()
        self.button_settings_darktheme.on()
        self.button_settings_pinktheme.on()
        self.button_settings_purpletheme.on()
        self.str_settings_selectiontheme.set(self.str_settings_selectiontheme_blue) #Cambiar el texto de el tema seleccionado

    def func_settings_themedark(self): #Desactivar el boton presionado y activar los demas
        self.button_settings_darktheme.off()
        self.button_settings_bluetheme.on()
        self.button_settings_pinktheme.on()
        self.button_settings_purpletheme.on()
        self.str_settings_selectiontheme.set(self.str_settings_selectiontheme_dark) #Cambiar el texto de el tema seleccionado
        
    def func_settings_themepink(self): #Desactivar el boton presionado y activar los demas
        self.button_settings_pinktheme.off()
        self.button_settings_darktheme.on()
        self.button_settings_bluetheme.on()
        self.button_settings_purpletheme.on()
        self.str_settings_selectiontheme.set(self.str_settings_selectiontheme_pink) #Cambiar el texto de el tema seleccionado
    
    def func_settings_themepurple(self): #Desactivar el boton presionado y activar los demas
        self.button_settings_purpletheme.off()
        self.button_settings_pinktheme.on()
        self.button_settings_darktheme.on()
        self.button_settings_bluetheme.on()
        self.str_settings_selectiontheme.set(self.str_settings_selectiontheme_purple) #Cambiar el texto de el tema seleccionado

    def func_settings_languageeng(self): #Desactivar el boton presionado y activar los demas
        self.button_settings_eng.off()
        self.button_settings_spa.on()
        self.str_settings_selectionlanguage.set(self.str_settings_selectionlanguage_eng) #Cambiar el texto de el lenguaje seleccionado

    def func_settings_languagespa(self): #Desactivar el boton presionado y activar los demas
        self.button_settings_spa.off()
        self.button_settings_eng.on()
        self.str_settings_selectionlanguage.set(self.str_settings_selectionlanguage_spa) #Cambiar el texto de el lenguaje seleccionado

    def func_settings_splashon(self):
        self.button_settings_sson.off()
        self.button_settings_ssoff.on()
        self.str_settings_selectionss.set(self.str_settings_selectionss_on)

    def func_settings_splashoff(self):
        self.button_settings_ssoff.off()
        self.button_settings_sson.on()
        self.str_settings_selectionss.set(self.str_settings_selectionss_off)

    def func_settings_timestart3(self):
        self.button_settings_timestart3.off()
        self.button_settings_timestart5.on()
        self.button_settings_timestart10.on()
        self.str_settings_selectiontimestart.set(self.str_settings_selectiontimestart_3)

    def func_settings_timestart5(self):
        self.button_settings_timestart5.off()
        self.button_settings_timestart3.on()
        self.button_settings_timestart10.on()
        self.str_settings_selectiontimestart.set(self.str_settings_selectiontimestart_5)

    def func_settings_timestart10(self):
        self.button_settings_timestart10.off()
        self.button_settings_timestart3.on()
        self.button_settings_timestart5.on()
        self.str_settings_selectiontimestart.set(self.str_settings_selectiontimestart_10)

    def func_settings_accept(self):
        #Obtener los ajustes
        self.finalsettings_theme = self.str_settings_selectiontheme.get()
        self.finalsettings_language = self.str_settings_selectionlanguage.get()
        self.finalsettings_splash = self.str_settings_selectionss.get()
        self.finalsettings_timestart = self.str_settings_selectiontimestart.get()
        self.finalwarning = self.str_settings_warning.get()
        self.finalwarningtext = self.str_settings_warningtext.get()
        #Modificarlos localmente
        DEFAULT_CONFIG["theme"] = self.finalsettings_theme
        DEFAULT_CONFIG["language"] = self.finalsettings_language
        DEFAULT_CONFIG["timetostart"] = int(self.finalsettings_timestart)
        if self.finalsettings_splash == "On":
            DEFAULT_CONFIG["splashscreen"] = True
        elif self.finalsettings_splash == "Off":
            DEFAULT_CONFIG["splashscreen"] = False
        #Modificar el archivo de configuracion con los nuevos ajustes
        configuration = open("./config.ak", "wb") #Abrir el archivo en modo escritura
        pickle.dump(DEFAULT_CONFIG, configuration) #Agregar la informacion por defecto
        configuration.close()
        del(configuration)
        #Cerrar la ventana
        messagebox.showwarning(self.finalwarning, self.finalwarningtext)
        self.close_AkSettings()

    def func_switch_specialkey(self):
        #Estado de el switch : 0 apagado, 1 encendido
        self.switch_state = 0
        #Cargar imagenes
        self.img_switch_off = PhotoImage(file=DIR_IMG + "switch_off.png")
        self.img_switch_on = PhotoImage(file=DIR_IMG + "switch_on.png")
        #Crear la funcion con los eventos que realizara el switch
        def switch_events(event):
            if self.switch_state == 1:
                self.button_switch.config(image=self.img_switch_off)
                self.switch_state = 0
                self.entry_loop["state"] = "disabled"
                self.combo_specialkey["state"] = "disabled"
            else:
                self.button_switch.config(image=self.img_switch_on)
                self.switch_state = 1
                self.entry_loop["state"] = "normal"
                self.combo_specialkey["state"] = "readonly"
                self.entry_loop.delete(0, END)
                self.entry_loop.insert(0, 0)

        #Crear label con imagen
        self.button_switch = Label(self.bg, image=self.img_switch_off, bg=PL_BLUE)
        #Convertir el label en boton
        self.button_switch.bind("<Button-1>", switch_events)
        #Colocar el boton
        self.button_switch.place(x=310, y=20)

def splashScreen():
    #Crear la ventana de carga
    SplashWindow = Tk()
    
    #Medidas de la pantalla
    SCREENWIDTH = SplashWindow.winfo_screenwidth()
    SCREENHEIGHT = SplashWindow.winfo_screenheight()
    #Medidas de la ventana
    sw_width = 500
    sw_height = 300
    sw_x = (SCREENWIDTH/2) - (sw_width/2)
    sw_y = (SCREENHEIGHT/2) - (sw_height/2)
    #Configurar las dimensiones de la ventana
    SplashWindow.geometry("%dx%d+%d+%d" % (sw_width, sw_height, sw_x, sw_y))
    SplashWindow.configure(bg=PL_BLUE)
    #Eliminar la barra de opciones
    SplashWindow.overrideredirect(1)
    #Funcion que se activa al finalizar la carga
    def newWindow():
        AkHome()
    #DISEÑO VENTANA

    #Titulo "Automatic Keyboard"
    Frame(SplashWindow, bg=PL_BLUE).place(x=0, y=0, width=500, height=300)
    label_title1 = Label(SplashWindow, text="Automatic", font=("Sono SemiBold", 32), bg=PL_BLUE, fg=PL_WHITE)
    label_title1.place(x=10, y=10, width=260, height=50)
    label_title2 = Label(SplashWindow, text="Keyboard", font=("Sono Light", 32), bg=PL_BLUE, fg=PL_WHITE)
    label_title2.place(x=270, y=10, width=220, height=50)
    #Crear los textos "Creado por", "Creado en", "Version"
    label_createdby = Label(SplashWindow, text="Made by JoseHz", font=("Sono SemiBold", 14), bg=PL_BLUE, fg=PL_WHITE)
    label_createdby.place(x=20, y=100, height=20 ,anchor=W)
    label_createdin = Label(SplashWindow, text="Created in Python 3.10", font=("Sono SemiBold", 14), bg=PL_BLUE, fg=PL_WHITE)
    label_createdin.place(x=20, y=120, height=20 ,anchor=W)
    label_version = Label(SplashWindow, text="Version 3.0", font=("Sono SemiBold", 14), bg=PL_BLUE, fg=PL_WHITE)
    label_version.place(x=20, y=140, height=20 ,anchor=W)
    #Crear el texto de advertencia
    label_warning = Label(SplashWindow, text="This program makes no attempt to hide itself, so don't use it for keyloggers or online gaming bots. Be responsible.", font=("Sono Light", 13), bg=PL_BLUE, fg=PL_WHITE, wraplength=500, justify=LEFT)
    label_warning.place(x=20, y=200, height=70, anchor=W)
    #Crear el texto "Loading..."
    st_loading = StringVar()
    st_loading.set("Loading...")

    label_loading = Label(SplashWindow, textvariable=st_loading, font=("Sono Light", 18), bg=PL_BLUE, fg=PL_WHITE)
    label_loading.place(x=320, y=260, height=30 ,anchor=W)
    #DISEÑO VENTANA

    #Bucle for
    for i in range(2):
        st_loading.set("Loading")
        SplashWindow.update_idletasks()
        time.sleep(0.4)

        st_loading.set("Loading.")
        SplashWindow.update_idletasks()
        time.sleep(0.4)

        st_loading.set("Loading..")
        SplashWindow.update_idletasks()
        time.sleep(0.4)

        st_loading.set("Loading...")
        SplashWindow.update_idletasks()
        time.sleep(0.3)

    #Destruir ventana de carga e inicializar la aplicacion
    SplashWindow.destroy()
    newWindow()
    SplashWindow.mainloop()


#Inicializar el programa
if __name__ == "__main__":
    if config["splashscreen"] == True:
        splashScreen()
    else:
        app = AkHome()