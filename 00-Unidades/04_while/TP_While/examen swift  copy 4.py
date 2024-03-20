import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

#UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
#que promete revolucionar el mercado. 
#Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 


#Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

#Los datos a ingresar por cada encuestado son:
    #* nombre del empleado
    #* edad (no menor a 18)
    #* genero (Masculino - Femenino - Otro)
    #* tecnologia (IA, RV/RA, IOT)   

#En esta opción, se ingresaran empleados hasta que el usuario lo desee.

#Una vez finalizado el ingreso, mostrar:

    #! 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #! 2) - Tecnología que mas se votó.
    #! 3) - Porcentaje de empleados por cada genero
    #! 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #! 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        bandera=True
        contadorIOT= 0
        contadorIA= 0
        contadorRVRA= 0
        contadorempleadosiotiarango= 0
        contadormasculino= 0
        contadorfemino= 0
        contadorotros= 0
        contadorempleadostotal= 0
        contadoriotrango= 0
        contadorfemeninoia= 0
        acumuladortotalfemeninoia= 0
        while bandera == True:
            #* nombre del empleado
            nombre=input("Ingrese su nombre:")
            #* edad (no menor a 18)
            edad=input("Ingrese su edad: ")
            edad=int(edad)
            while edad < 18:
                edad=input("ERROR, reingrese su edad: ")
                edad=int(edad)
            #* genero (Masculino - Femenino - Otro)
            genero=input("Ingrese su genero: ")
            while genero !="Masculino" and genero !="Femenino" and genero !="Otro":
                genero=input("ERROR, reingrese su genero: ")
            #* tecnologia (IA, RV/RA, IOT) 
            tecnologia=input("Ingrese la tacnologia: ")
            while tecnologia !="IA" and tecnologia !="RV/RA" and tecnologia !="IOT":
                tecnologia=input("ERROR, reingrese la tacnologia: ")
            
            match tecnologia:
                case "IA":
                    contadorIA += 1
                case "IOT":
                    contadorIOT += 1
                    if (edad >=18 and edad <= 25) or (edad >= 33 and edad <= 42):
                        contadoriotrango += 1
                case "RV/RA":
                    contadorRVRA += 1
                    if contadorRVRA == 1 or edad < edad_minima:
                        edad_minima= edad
                        nombre_minmo=nombre
                        genero_minimo=genero
            match genero:
                case "Femenino":
                    contadorfemino += 1
                    if tecnologia == "IA":
                        contadorfemeninoia += 1
                        acumuladortotalfemeninoia += edad
                case "Masculino":
                    contadormasculino += 1
                    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
                    if (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <= 50:
                        contadorempleadosiotiarango += 1
                case "Otro":
                    contadorotros += 1
            

            bandera = question("CONSULTA", "Desea continuar con sus ingresos?")

            
            #!X 2) - Tecnología que mas se votó.
            if contadorRVRA  > contadorIA and contadorRVRA  > contadorIOT:
                tecnologiamasvotada= contadorRVRA
            elif contadorIOT > contadorIA:
                tecnologiamasvotada= contadorIOT
            else:
                tecnologiamasvotada= contadorIA
            
            #!X 3) - Porcentaje de empleados por cada genero
            
            contadortotalempleados= contadorfemino + contadorotros + contadormasculino
            if contadorfemino != 0:
                porcentajefemenino= (contadorfemino * 100) / contadorempleadostotal
            else:
                porcentajefemenino= "NO SE ENCONTRARON FEMENINOS"
            if contadormasculino != 0:
                porcentajemasculino= (contadormasculino * 100) / contadorempleadostotal
            else:
                porcentajemasculino="NO SE ENCONTRARON MASCULINOS"
            if contadorotros != 0:
                porcentaeotros=(contadorotros * 100) / contadorempleadostotal
            else:
                porcentaeotros= "NO SE ENCONTRARON OTROS"

            
            #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
            porcentajeiotrango= (contadoriotrango * 100)/ contadorempleadostotal
            #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
            #porcentajefemeninoia= (acumuladoredadtotalfemeninoia * 100) / contadorfemino TENGO QUE TENER EN CUENTA EN EL CASO DE QUE NO INCLUYAN NINGUN TIPO DE GENERO FEMENINO
            if contadorfemeninoia > 0 :
                porcentajefemeninoia= (acumuladortotalfemeninoia * 100) / contadorfemino
            else:
                porcentajefemeninoia= "No se pudo calcular, no se ingresaron participantes genero femenino"

            #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

        print (f"1.La cantidad de empleados de genero masculino votantes por IOT o por IA en rango de edad es de: {contadorempleadosiotiarango}\n") 
        print (f"\n2.La tecnologia mas votada es: {tecnologiamasvotada}\n")
        print (f"\n3. El procentaje de personas genero femenino es de: {porcentajefemenino} %.\nEl porcentaje genero masculino es de: {porcentajemasculino}%.\nEl porcentaje de genero otros es de: {porcentaeotros}%")
        print (f"\n4.El porcentaje de votante por IOT en rango de edad es de: {porcentajeiotrango}%\n")
        print (f"\n5. El porcentaje de genero femenino que voto por IA es de: {porcentajefemeninoia}%\n")
        print (f"\n6. La persona con menor edad que voto por RV/RA fue {nombre_minmo} de genero {genero_minimo} con una edad de {edad_minima} años")

        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
