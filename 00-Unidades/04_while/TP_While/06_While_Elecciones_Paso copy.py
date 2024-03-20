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
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de 
#valores:

#Para ello deberás programar el botón  para poder cargar 10 operaciones de compra con los siguientes datos:
    #* Nombre
    #* Monto en pesos de la operación (no menor a $10000)
    #* Tipo de instrumento(CEDEAR, BONOS, MEP) 
    #* Cantidad de instrumentos  (no menos de cero) 
    
#Realizar los siguientes informes:

    #! 1) - Tipo de instrumento que menos se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion del usuario que invirtio menos dinero
    #! 6) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total

    def btn_validar_on_click(self):

        peticion = True #bandera

        contadorinicio = 10

        contadorcedear= 0
        contadorbonos= 0
        contadormep= 0
        
        acumuladromep= 0
        acumuladorusuariosmeprango= 0
        
        acumuladrousuariosnocedear= 0
    
        while contadorinicio < 10:
            nombre=input("Ingrese su nombre")
            montoingersado= input("Ingrese el monto deseado")
            montoingersado= int(montoingersado)
            while montoingersado < 10000:
                montoingersado= input("Reingrese el monto deseado") 
            tipodeinstrumento= input ("Ingese en que desea invertir su dinero")
            while input !="CEDEAR" !="BONOS" !="MEP":
                tipodeinstrumento= input ("Reingese en que desea invertir su dinero")
            cantidadinstrumentos= input("Ingrese en cuantos instrumentos desea invertir")
            cantidadinstrumentos=int(cantidadinstrumentos)
            
            while cantidadinstrumentos == 0:
                cantidadinstrumentos= input("Reingrese en cuantos instrumentos desea invertir")
            
            contadorinicio += 1
        #! 1) - Tipo de instrumento que menos se operó en total.  #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP
            match (tipodeinstrumento):
                case "BONOS":
                    contadorbonos += 1
                case "CEDEAR":
                    contadorcedear += 1
                    
                case _:
                    contadormep += 1
                    acumuladromep = cantidadinstrumentos
        #! 3) - Cantidad de usuarios que no compraron CEDEAR 
            acumuladrousuariosnocedear= contadormep + contadorbonos
        #! 4)  Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
            



            


        peticion= question("pregunta", "Desea continuar?")


        if contadorbonos < contadorcedear and contadorbonos < contadormep:
            instrumentomenosoperado = contadorbonos
        elif contadorcedear < contadormep:
            instrumentomenosoperado = contadorcedear
        else:
            instrumentomenosoperado = contadormep
#! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
        if acumuladromep > 50 and acumuladromep < 200:
            acumuladorusuariosmeprango += 1
#! 4)  Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
        if tipodeinstrumento == "BONOS" or tipodeinstrumento == "CEDEAR":
                nombre= nombre
                montoingersado=montoingersado


        
        

print (f"1.El instrumentos menos ooperado es: {instrumentomenosoperado}")
print (f"2.Cantidad de usuarios que compraron entre 50  y 200 MEP: {acumuladorusuariosmeprango}")
print (f"3.Cantidad de usuarios que no compraron CEDEAR: {acumuladrousuariosnocedear}")




                
            
            


        
        
        


        
            

        
            


if __name__ == "__main__":
    app = App()
app.geometry("300x300")
app.mainloop()
