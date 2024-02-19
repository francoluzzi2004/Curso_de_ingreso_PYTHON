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
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        candidatomasvotado= (" ", 0)
        candidatomenosvotado= (" ", 0)
        promedioedades= 0
        acumulador= 0
        totalvotos= 0
        
        while True:
            nombrecandidatos=prompt("Elecciones", prompt="Ingrese un nombre")
            if nombrecandidatos is None:
                break
        while nombrecandidatos.isdigit():
            nombrecandidatos=prompt("ERROR DE SISTEMA", prompt="Ingrese un nombre")
            if not (nombrecandidatos.isdigit):
                break
            else:
                continue
            edadvotantes=prompt("Elecciones", "Ingrese su edad")
            if edadvotantes == None:
                    break
            edadvotantes= int(edadvotantes)
        while edadvotantes <= 25:
            edadvotantes=prompt("Elecciones", "Ingrese su edad")
            edadvotantes= int(edadvotantes)
            if edadvotantes > 25:
                    break
            else:
                continue
        votos=prompt(title="Elecciones",prompt="Ingrese su voto")
        while votos.isalpha():
                votos=prompt(title="Elecciones",prompt="ERROR, reingtrese su voto")
                if votos == None or not(votos.isalpha()):
                    break
                else:
                    continue
        votos= int(votos)
        if votos < 0:
            while votos < 0:
                votos=prompt(title="Elecciones",prompt="ERROR, reingtrese su voto")
                votos= int(votos)
                if votos < 0:
                    if votos == None or votos >= 0:
                        break
                    else:
                        continue
                if acumulador == 0:
                    candidatomasvotado=(nombrecandidatos , votos)
                    candidatomenosvotado=(nombrecandidatos, votos)
                else:
                    if votos > candidatomasvotado[1]:
                        candidatomasvotado= (nombrecandidatos, votos)
                    elif votos < candidatomenosvotado[1]:
                        candidatomenosvotado= (nombrecandidatos, votos)
                promedioedades += edadvotantes
                totalvotos+= votos
                acumulador += 1
                promedioedades= promedioedades / acumulador
                mensaje= (f"(En estas eleccion paso, el candidato ams votado es: {candidatomasvotado[0]}.El candidato menos votado es{candidatomenosvotado[1]}).\nEn estas elecciones, el promedio de edad en los candidates es de {promedioedades}.\nPor ultimo, la cantidad de total obtenida en votos es de:{totalvotos} ")
            

                

                            
    



                

        
        
            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
