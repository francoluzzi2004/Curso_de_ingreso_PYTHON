import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Franco damian    
apellido:Luzzi
Tutor: Natali
---
TP: ES_Facturaciones
---
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        pass
        importesuma=self.txt_importe_1.get()
        importesuma1=self.txt_importe_2.get()
        importesuma2= self.txt_importe_3.get()

        importesumaentero=int(importesuma)
        importesuma1entero=int(importesuma1)
        importesuma2entero=int(importesuma2)

        final=importesumaentero + importesuma1entero + importesuma2entero
        mensaje="El resultado de su suma es de {0}".format(final)
        alert(title="Resultado de su suma", message=mensaje )


    def btn_promedio_on_click(self):
        pass
        importesumapromedio=self.txt_importe_1.get()
        importesuma1promedio=self.txt_importe_2.get()
        importesuma2promedio= self.txt_importe_3.get()

        importepromedio=int(importesumapromedio)
        importepromedio1=int(importesuma1promedio)
        importepromedio2=int(importesuma2promedio)

        primerresultado=importepromedio + importepromedio1 + importepromedio2
        promediofinal=primerresultado / 3

        mensajefinalpromedio= "Su promedio en productos es de {0}".format(promediofinal)
        alert(title="Su promedio es", message=mensajefinalpromedio)


    def btn_total_iva_on_click(self):
        pass      
        impor=self.txt_importe_1.get()
        impor1=self.txt_importe_2 .get()
        impor2=self.txt_importe_3 .get()

        imporentero=int(impor)
        impor1entero=int(impor1)
        impor2entero=int(impor2)

        sumatotal= imporentero + impor1entero + impor2entero

        iva= 0.21
        incremento=sumatotal * iva
        preciofinal=sumatotal + incremento

        msjfinal="Su total con un incremento del 21% quedaria en: {0} ".format(preciofinal)

        alert(title="IVA", message=msjfinal)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()