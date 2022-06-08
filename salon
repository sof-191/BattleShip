from tkinter import *
import random
import time

def SalonFama(menu):

    menu.withdraw()
    fama = Toplevel()
    fama.title("BattleShip: Segundo Proyecto Programado")
    fama.resizable(False, False) # No se puede cambiar el tamaño de la ventana
    fama.wm_attributes("-topmost", 1) #Poner esta ventana enfrente de todas las demas 
    canvas = Canvas(fama, width=1400, height=700, borderwidth =0, highlightthickness=0, bg = "#000000")

    canvas.pack()
    fama.update()
    
    label1 = Label(canvas, text = "Salón de la Fama", font = ("Haettenschweiler", 100), bg="#000000", fg="#00FFFF")
    label1.place(x=150, y=10)

    label1 = Label(canvas, text = "Nombre-Puntuacion", font = ("Haettenschweiler", 50), bg="#000000", fg="#FFFFFF")
    label1.place(x=140, y=190)
    def regresar():
            menu.deiconify()
            fama.withdraw()
    button_regresar = Button(canvas, text="Regresar", font=("fixedsys", "15"),command=regresar,bg= "#FF0000")
    button_regresar.place(x=600, y=600)
