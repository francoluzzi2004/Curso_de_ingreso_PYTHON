import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:franco damian
apellido:luzzi
Tutor:Natali
---
Simulacro Turno Noche

Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

#Nombre listo

#Importe ganado (mayor o igual $1000) listo

#Género (“Femenino”, “Masculino”, “Otro”) listo

#Juego (Ruleta, Poker, Tragamonedas) listo

#Necesitamos saber:

#Nombre y género de la persona que más ganó.listo

#Promedio de dinero ganado en Ruleta.    listo

#Porcentaje de personas que jugaron en el Tragamonedas. listo

#Cuál es el juego menos elegido por los ganadores. listo

#El nombre del jugador que ganó más dinero jugando Poker . listo
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        comienzo = True #bandera
        mayorganancia= 0
        contadorinicial= 0
        acumuladorgananciastotal= 0
        acumuladorruleta= 0 
        contadorruleta= 0
        contadortragamonedas= 0
        acumuladortragamonedas= 0
        acumuladorpoker= 0
        acumuladorgananciapoker= 0
        contadorpoker= 0
        juegomenosjugadoporganadores= 0
        acumuladorjuegos= 0
        while True:

            nombre=input ("Ingrese su nombre: ")

            importeganado= input("Ingrese un monto")
            importeganado=int(importeganado)
            if importeganado > 1000:
                importeganado=int(importeganado)
                importeganado= input("ERROR, Reingrese un monto")
            genero = input("Ingrese su genero: ")
            if genero !="Femenino" !="Masculino" !="Otros":
                genero = input("ERROR, Reingrese su genero: ")
            juegoseleccionado= input ("Ingrese que juego jugara: ")
            if juegoseleccionado !="Ruleta" !="Poker" !="Tragamonedas":
                juegoseleccionado= input ("ERROR, Reingrese que juego jugara: ")

                acumuladorjuegos += juegoseleccionado
                contadorinicial += 1
                acumuladorgananciastotal += importeganado
                #Nombre y género de la persona que más ganó
            if importeganado > mayorganancia:
                mayorganancia= importeganado
                nombre1=nombre
                genero1=genero
                
            match juegoseleccionado:
                case "Ruleta":
                    contadorruleta += 1
                    acumuladorruleta += juegoseleccionado
                case  "Tragamonedas":
                    contadortragamonedas += 1
                    acumuladortragamonedas += juegoseleccionado
                case "Poker":
                    contadorpoker += 1
                    acumuladorpoker += juegoseleccionado
                    if importeganado > acumuladorgananciapoker:
                        acumuladorgananciapoker = importeganado
        
            if juegoseleccionado == "Tragamonedas":
                promediojugarorestragaomendas = (contadorinicial * 100)/ contadortragamonedas
            comienzo= question("Casino MDQ", "Quiere seguir jugando?")
        
            if juegoseleccionado == "Ruleta" and importeganado > acumuladorruleta:
                promediodineroruleta= (acumuladorgananciastotal * 100) / acumuladorgananciapoker
            if contadorpoker > contadortragamonedas and contadorpoker > contadorruleta:
                juegomenosjugadoporganadores="Poker"
            elif contadortragamonedas > contadorruleta:
                juegomenosjugadoporganadores= "Tragamonedas"
            else: 
                juegomenosjugadoporganadores= "Ruleta"

            if juegoseleccionado == "Poker" and importeganado == acumuladorgananciapoker:
                nombre2=nombre
        print(f"1.{nombre1}cuyo genero es {genero1} fue quien tuvo la mayor ganancia esta noche.\nEl promedio de dinero ganado en la ruleta esta noche es de: {promediodineroruleta}.\nEl promedio de gente que jugo al tragamonedas es de: {promediojugarorestragaomendas}%.\nEl juego menos elegido esta noche fue: {juegomenosjugadoporganadores}.\nEl jugador con mayor ganancia en el poker fue: {nombre2}")

        

    

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
