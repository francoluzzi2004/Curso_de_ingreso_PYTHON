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
        contador = 5
        contadorF= 0
        contadorM= 0

        contador_exotico= 0
        contador_perro= 0
        contador_gato= 0

        acumulador_peso_gato= 0
        acumulador_peso_perro= 0
        acumulador_peso_exotico= 0
        
        edad_minima_perro= 0
        while contador > 5:
            nombre=prompt("Consulta","Ingrese el nombre de su mascota: ")

            tipo_mascota= prompt("consulta","ingrese que tipo de mascota es: ")
            while tipo_mascota !="perro" and tipo_mascota !="gato" and tipo_mascota !="exotico":
                tipo_mascota= prompt("consulta","reingrese que tipo de mascota es: ")

            peso_mascota=prompt ("Ingrese el peso corporal: ")
            peso_mascota=int(peso_mascota)
            while peso_mascota  < 10 and peso_mascota > 80:
                peso_mascota=prompt ("ERROR DE PARAMETROS, reingrese el peso corporal: ")
                peso_mascota=int(peso_mascota)

            sexo= prompt("ingrese el sexo de su mascota: ")
            while sexo !="F" and sexo !="M":
                sexo= prompt("reingrese el sexo de su mascota: ")

            edad=prompt("Ingrese la edad de su mascota: ")
            edad=int(edad)
            while edad <= 0:
                edad=prompt("reingrese la edad de su mascota: ")
                edad=int(edad)
            
        
            match sexo:
                case "M":
                    contadorM += 1
                case "F":
                    contadorF += 1
            match tipo_mascota:
                case "exotico":
                    contador_exotico += 1
                    acumulador_peso_exotico += peso_mascota
                case "gato":
                    contador_gato += 1
                    acumulador_peso_gato += peso_mascota
                case "perro":
                    contador_perro += 1
                    acumulador_peso_perro += peso_mascota
                    #Informe D- El nombre del perro más joven
                    if edad == 0 or edad  < edad_minima_perro:
                        edad_minima_perro= edad
            #Informe C- El nombre y tipo de la mascota menos pesada
            peso_total_mascotas= acumulador_peso_gato + acumulador_peso_exotico + acumulador_peso_perro
            if acumulador_peso_perro < acumulador_peso_gato and acumulador_peso_perro < acumulador_peso_exotico:
                mascota_menos_pesada= acumulador_peso_perro
                nombre_menos_peso= nombre
                tipo_menos_peso= tipo_mascota
            if contador > 0:
                peso_total_mascotas += peso_mascota

            
            
        contador -= 1
    #Informe A- Cuál fue el sexo menos ingresado (F o M)
        if contadorF > contadorM:
            sexo_menos_ingresado= "M"
        else:
            sexo_menos_ingresado= "F"

    #Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico)
        contador_total_tipo= contador_gato + contador_exotico + contador_perro
        if contador_perro > 0:
            porcentaje_perro= (contador_perro * 100) / contador_total_tipo
        else:
            porcentaje_perro="no se encontraron resultados de perro"
        if contador_exotico > 0:
            porcentaje_exotico= (contador_exotico * 100) / contador_total_tipo
        else:
            porcentaje_exotico="no se encontraro resultados de exotico"
        if contador_gato > 0:
            porcentaje_gatos= (contador_gato * 100) / contador_total_tipo
        else:
            porcentaje_gatos="no se encontraron resultados de gato"

        #Informe C- El nombre y tipo de la mascota menos pesada
        
        #Informe E- El promedio de peso de todas las mascotas
        
        
        if contador > 0:
            promedio_peso_mascotas= peso_total_mascotas / contador

        print(f"1. El sexo menos ingresado fue: {sexo_menos_ingresado}")
        print(f"2. El porcentaje de mascotas que hay por tipo es: perro= {porcentaje_perro}%, gato= {porcentaje_gatos}% y exoticos= {porcentaje_exotico}%")
        print(f"3. La mascota menos pasas es: {nombre_menos_peso}, {tipo_menos_peso}, con un total de {mascota_menos_pesada}kg")
        print(f"4. El perro mas joven tiene {edad_minima_perro} años")
        print(f"5. el promedio de peso de todas las mascotas es: {promedio_peso_mascotas}")






        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
