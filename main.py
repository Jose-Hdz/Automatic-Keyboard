from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
import keyboard
import time

#-----Def menu window--
app = QtWidgets.QApplication([])
app.setWindowIcon(QtGui.QIcon("images/logo.png"))

#-----load ui files----
menu = uic.loadUi("main_menu.ui")
finish_menu = uic.loadUi("finish_menu.ui")

#-----Definitons-------
#Buttons

def start_txt():
    texto = menu.textinput.text()
    textod = menu.textinput_2.text()

    if len(texto) == 0 or len(textod) == 0 or ():
        menu.txterror.setText("Error")
    
    else:
        try:
            textodelay = float(textod)

            if textodelay < 0 or textodelay > 1.5:
                menu.txterror.setText("Error")

            else:
                time.sleep(3)
                keyboard.write(texto, delay=textodelay)
                menu_f()
        except:
            menu.txterror.setText("Error")

def refresh_button():
    menu.txterror.setText("")

#Menus
def menu_f():
    menu.hide()
    finish_menu.show()
def menu_b():
    menu.show()
    finish_menu.hide()

#Translations
def opteng():
    menu.label.setText("PLACE YOUR TEXT HERE")
    menu.label_3.setText("SET THE DELAY (0 - 1.5)")
    menu.playButton.setText("START")
    menu.optlanguage.setTitle("Language")
    finish_menu.finish_txt.setText(" COMPLETED")
def optspa():
    menu.label.setText("COLOCA TU TEXTO AQUÍ")
    menu.label_3.setText("COLOCA EL DELAY (0 - 1.5)")
    menu.playButton.setText("COMENZAR")
    menu.optlanguage.setTitle("Idioma")
    finish_menu.finish_txt.setText("COMPLETADO")
def optrus():
    menu.label.setText("ЗАПОЛНИТЕ СВОЙ ТЕКСТ ЗДЕСЬ")
    menu.label_3.setText("УСТАНОВИТЕ ЗАДЕРЖКУ (0 - 1.5)")
    menu.playButton.setText("НАЧАЛО")
    menu.optlanguage.setTitle("Язык")
    finish_menu.finish_txt.setText("ЗАВЕРШЕННЫЙ")

#-----Buttons----------

menu.playButton.clicked.connect(start_txt)
menu.refreshButton.clicked.connect(refresh_button)
finish_menu.okButton.clicked.connect(menu_b)

menu.optenglish.triggered.connect(opteng)
menu.optspanish.triggered.connect(optspa)
menu.optrussian.triggered.connect(optrus)

#-----Start menu window
menu.show()
app.exec()
