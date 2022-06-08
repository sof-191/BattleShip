#Menú 2

from tkinter import *
import random
import time
import Ayuda



def main():
    menu = Tk()
    menu.title("BattleShip: Segundo Proyecto Programado")
    menu.resizable(False, False) # No se puede cambiar el tamaño de la ventana
    menu.wm_attributes("-topmost", 1) #Poner esta ventana enfrente de todas las demas 
    canvas = Canvas(menu, width=1400, height=700, borderwidth =0, highlightthickness=0, bg = "#000000")

    canvas.pack()
    menu.update()

    rojoNaranja = "#FF4500"
    cian = "#00FFFF"
    azul = "#0000FF"
    amarillo = "#FFFF00"
    white = "#FFFFFF"
    black = "#000000"

    #Botones del menu 
    label1 = Label(canvas, text = "Battle Ship", font = ("Haettenschweiler", 100), bg="#000000", fg="#FFFF00")
    label1.place(x=550, y=50)

 
    button_start_again = Button(canvas, text="", font=("fixedsys", "30"), bg = "#3B83BD")
    button_start_again.place(x=200, y=300)


    button_salon_de_la_fama = Button(canvas, text="Salon Fama", command= lambda : Ayuda.SalonFama(menu), font=("fixedsys", "30"), bg= "#008000")
    button_salon_de_la_fama.place(x=1000, y=300)

    button_ayuda = Button(canvas, text="Ayuda", font=("fixedsys", "30"), command= lambda : Ayuda.ayuda_juego(menu) , bg= "#3B83BD")
    button_ayuda.place(x=675, y=500)
 
    menu.mainloop()
main()
