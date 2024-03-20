import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
De 5  mascotas que ingresan a una veterinaria  se deben tomar y validar los siguientes datos.

Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M  )
Edad(mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:
1Informe A- Cuál fue el sexo menos ingresado (F o M)
1Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico)
1Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador_mascotas = 0
        mensaje = ""

        contador_femenino = 0
        contador_masculino = 0
        
        contador_exotico = 0
        contador_gato = 0        
        contador_perro = 0

        acumulador_peso_mascotas = 0
        

        while contador_mascotas < 5:

            nombre = prompt("INRESO", "Ingrese el nombre de la mascota")
            while not nombre.isalpha():
                nombre = prompt("ERROR", "Reingrese el nombre de la mascota")
            
            tipo = prompt("Ingreso", "Ingrese que tipo es")
            while tipo != "Gato" and tipo != "Perro" and tipo != "Exotico":
                tipo = prompt("Ingreso", "Ingrese un tipo de animnal valido")
            
            peso = prompt("UTN", "Ingrese el peso")
            while not (int(peso) > 10 and int(peso) < 80):
                peso = prompt("ERROR", "Reingrese el peso")
            peso = int(peso)

            sexo = prompt("INRESO", "Ingrese el sexo de la mascota")
            while sexo != "Femenino" and sexo != "Masculino":
                sexo = prompt("ERROR", "Reingrese el sexo de la mascota")
            
            edad = prompt("INRESO", "Ingrese la edad de la mascota")
            while int(edad) < 0:
                edad = prompt("INRESO", "Ingrese la edad de la mascota")
            
            #A
            match(sexo):
                case "Femenino":
                    contador_femenino += 1
                case "Masculino":
                    contador_masculino += 1

            #B
            match(tipo):
                case "Exotico":
                    contador_exotico += 1
                case "Gato":
                    contador_gato += 1
                case "Perro":
                    contador_perro += 1
            
            # Informe C- El nombre y tipo de la mascota menos pesada
            if contador_mascotas == 0 or peso < peso_minimo:
                peso_minimo = peso
                tipo_minimo = tipo
                nombre_minimo = nombre

            # Informe D- El nombre del perro más joven
            if contador_mascotas == 0 or edad < edad_minima:
                edad_minima = edad
                nombre_minimo_edad = nombre

            if contador_mascotas > 0:
                acumulador_peso_mascotas += peso

            
            contador_mascotas += 1

        #Informe A- Cuál fue el sexo menos ingresado (F o M)
        if contador_masculino > contador_femenino:
            mensaje += "El sexo mas ingreso es Masculino\n"
        else:
            mensaje += "El sexo mas ingresado es femenino\n"
        
        # Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico)
        porcentaje_perro = (contador_perro * 100) / contador_mascotas
        if contador_perro > 0:
            mensaje += f"El porcentaje de perro es de {porcentaje_perro}%\n"
        
        porcentaje_gato = (contador_gato * 100) / contador_mascotas
        if contador_gato > 0:
            mensaje += f"El porcentaje de gato es de {porcentaje_gato}%\n"

        porcentaje_exotico = (contador_exotico * 100) / contador_mascotas
        if contador_exotico > 0:
            mensaje += f"El porcentaje de animales exoticos es de {porcentaje_exotico}%\n"
        
        # Informe C- El nombre y tipo de la mascota menos pesada
        mensaje += f"La mascota con menor peso se llama {nombre_minimo} y es un {tipo_minimo}\n"

        # Informe D- El nombre del perro más joven
        mensaje += f"El nombre del perro mas joven es {nombre_minimo_edad}"

        #Informe E- El promedio de peso de todas las mascotas
        promedio_peso_mascotas = acumulador_peso_mascotas / contador_mascotas
        if contador_mascotas > 0:
            mensaje += f"El promedio de peso de las mascotas es de {promedio_peso_mascotas} kilos\n"
        
        alert("FINAL", mensaje)






        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
