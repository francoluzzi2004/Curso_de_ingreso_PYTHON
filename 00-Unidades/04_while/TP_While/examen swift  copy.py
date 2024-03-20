import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
#Alumno= Franco Damian Luzzi
#Tutor= Natali
#De 20 contenedores que llegan al puerto de Rosario, se deben pedir y validar los siguientes datos

1#Marca (no validar)
1#Categoría (peligroso, comestible, indumentaria)
1#Peso ( entre 100 y 800)
1#Tipo de material ( aluminio, hierro , madera)
1#Costo en $ (mayor a 0)

#Pedir datos por prompt y mostrar por print, se debe informar:
1#Informe A- Cuál fue tipo de material menos usado ( aluminio, hierro , madera)
1#Informe B- El porcentaje de contenedores por Categoría (peligroso, comestible, indumentaria)
1#Informe C- La marca y tipo del contenedor más costoso
1#Informe D- La marca del contenedor de aluminio con mayor costo
#Informe E- El promedio de costo de todos los contenedores


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador_contenedores = 0

        contador_aluminio= 0
        contador_madera= 0
        contador_hierro= 0

        acumulador_costo_hierro= 0
        acumulador_costo_madera= 0
        acumulador_costo_aluminio= 0

        while contador_contenedores <= 20:
            #Marca (no validar)
            marca=prompt("contenedores","Ingrese de que marca es su contenedor: ")
            #Categoría (peligroso, comestible, indumentaria)
            categoria= prompt("contenedores", "Ingrese de que categoria es su contenedor: ")
            while categoria !="peligroso" and categoria !="comestible" and categoria != "indumentaria":
                categoria=prompt("contenedores","ERROR, reingrese su categoria: ")
            #Peso ( entre 100 y 800)
            peso_contenedores=prompt("contenedores", "Ingrese el peso de su contenedor: ")
            peso_contenedores=int(peso_contenedores)
            while peso_contenedores < 100 or peso_contenedores > 800:
                peso_contenedores=prompt("contenedores", "ERROR, reingrese el peso de su contenedor: ")
                peso_contenedores=int(peso_contenedores)
            #Tipo de material ( aluminio, hierro , madera)
            material=prompt("contenedores", "Ingrese de que material es su contenedor: ")
            while material !="aluminio" and material !="hierro" and material != "madera":
                material=prompt("contenedores", "ERROR, reingrese de que material es su contenedor: ")
            #Costo en $ (mayor a 0)
            costo=prompt("contenedores", "Ingrese el costo de su contenedor: ")
            costo=int(costo)
            while costo <= 0:
                costo=prompt("contenedores", "ERROR, reingrese el costo de su contenedor: ")
                costo=int(costo)
            #Informe A- Cuál fue tipo de material menos usado ( aluminio, hierro , madera)
            match material:
                case "aluminio":
                    contador_aluminio += 1
                    acumulador_costo_aluminio += costo
                case "hierro":
                    contador_hierro += 1
                    acumulador_costo_hierro += costo
                case "madera":
                    contador_madera += 1
                    acumulador_costo_madera += costo

            costo_contenedores_total= acumulador_costo_aluminio + acumulador_costo_hierro + acumulador_costo_madera
            contador_contenedores += 1

        #Informe A- Cuál fue tipo de material menos usado ( aluminio, hierro , madera)
        if contador_madera < contador_hierro and contador_madera < contador_aluminio:
            material_menos_utilizado= "madera"
        elif contador_hierro < contador_aluminio:
            material_menos_utilizado= "hierro"
        else:
            material_menos_utilizado= "aluminio"
        #Informe B- El porcentaje de contenedores por Categoría (peligroso, comestible, indumentaria)
        porcentaje_contenedores_madera= (contador_madera * 100) / contador_contenedores
        porcentaje_contenedores_hierro= (contador_hierro * 100) / contador_contenedores
        porcentaje_contendores_aluminio= (contador_aluminio * 100) / contador_contenedores
        
        #Informe C- La marca y tipo del contenedor más costoso
        if contador_contenedores == 0 or contenedor_mas_costoso > costo:
            contenedor_mas_costoso = costo
            marca_mas_costoso= marca
            tipo_mas_costoso= material
        
        #Informe D- La marca del contenedor de aluminio con mayor costo
        if acumulador_costo_aluminio < contenedor_aluminio_mas_costoso:
            contenedor_aluminio_mas_costoso= acumulador_costo_aluminio
            marca_aluminio_mas_costoso= marca
        
        #Informe E- El promedio de costo de todos los contenedores
        promedio_costo_todos_contenedores= costo_contenedores_total / contador_contenedores

        print(f"1. El material menos utilizado es: {material_menos_utilizado}\n")
        print (f"\n2. El porcentaje de contenedores dividio por grupoes es: madera= {porcentaje_contenedores_madera}%. hierro= {porcentaje_contenedores_hierro}%. aluminio= {porcentaje_contendores_aluminio}%\n")
        print(f"\n3. El contenedor mas costoso es de la marca {marca_mas_costoso} y su tipo de material es {tipo_mas_costoso}\n")
        print(f"\n4. El contendeor de alumnio mas caro es de la marca {marca_aluminio_mas_costoso}\n")
        print(f"\n5. El promedio de costo de todos los contenedores equivale a: {promedio_costo_todos_contenedores}")





        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
