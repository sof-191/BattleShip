#Menú 2

from email.mime import image
from tkinter import *
import random
import time
import Ayuda
import salon

global menu


def main():
    
    menu = Tk()
    menu.title("BattleShip: Segundo Proyecto Programado")
    menu.resizable(False, False) # No se puede cambiar el tamaño de la ventana
    menu.wm_attributes("-topmost", 1) #Poner esta ventana enfrente de todas las demas 
    menu_imagen = PhotoImage(file = "imgs/fondo.png")
    canvas = Canvas(menu, width=1400, height=700, borderwidth =0, highlightthickness=0, bg = "#000000")
    canvas.create_image(700,350,image=menu_imagen)

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


    iniciar_imagen = PhotoImage(file = "imgs/INICIAR.png")
    button_start_again = Button(canvas, text="", image = iniciar_imagen, font=("fixedsys", "30"), bg="#000000")
    button_start_again.place(x=200, y=300)

    salon_imagen = PhotoImage(file = "imgs/SALON.png")
    button_salon_de_la_fama = Button(canvas, text="Salon Fama", image = salon_imagen, command= lambda : salon.SalonFama(menu), font=("fixedsys", "30"), bg= "#000000")
    button_salon_de_la_fama.place(x=1000, y=300)


    ayuda_imagen = PhotoImage(file = "imgs/AYUDA.png")
    button_ayuda = Button(canvas, text="Ayuda", font=("fixedsys", "30"), image = ayuda_imagen,command= lambda : Ayuda.ayuda_juego(menu) , bg= "#000000")
    button_ayuda.place(x=675, y=500)


 
    menu.mainloop()



if __name__ == "__main__":
    main()
