import tkinter as tk
from tkinter import ttk
from area_perimetro_poligonal import AreaPoligonal

objeto = AreaPoligonal()

class Interfaz():
    
    def datos_usuario(self):
        try:
            self.decimal = int(decimales.get())
            self.height = float(altura.get())
            self.width = float(ancho.get())
            self.comprobar = "si"
        except:
            self.comprobar = "no"
            
        return self.comprobar
    
    def cargar_estilos(self):
        if texto_estilos["values"] == "":
            texto_estilos["values"] = objeto.selection_style_texto()
            
        return texto_estilos
    
    def estilo_texto(self):

        if texto_estilos.get() == "":
            self.texto_est = "Standard"
        else:
            self.texto_est = texto_estilos.get()

        return self.texto_est
    
    def area(self):
        self.datos_usuario()
        self.estilo_texto()
        
        if self.comprobar == "si":
            objeto.propiedades(self.texto_est, self.decimal, self.height, self.width)
            objeto.area()
        elif self.comprobar == "no":
            objeto.propiedades(self.texto_est)
            objeto.area()
    
    def perimetro(self):
        self.datos_usuario()
        self.estilo_texto()
        
        if self.comprobar == "si":
            objeto.propiedades(self.texto_est, self.decimal, self.height, self.width)
            objeto.perimetro()
        elif self.comprobar == "no":
            objeto.propiedades(self.texto_est)
            objeto.perimetro()
    
    def area_perimetro(self):
        self.datos_usuario()
        self.estilo_texto()
        
        if self.comprobar == "si":
            objeto.propiedades(self.texto_est, self.decimal, self.height, self.width)
            objeto.area_perimetro()
        elif self.comprobar == "no":
            objeto.propiedades(self.texto_est)
            objeto.area_perimetro()
        
        
            
objecto_gui = Interfaz()

# GUI
window = tk.Tk()
window.title("AutoCAD Área")
window.geometry("300x360")
window.wm_attributes("-topmost", 1)
window.resizable(0,0)

label = tk.Label(window, text="CALCULAR ÁREA Y PERÍMETRO")
label.pack()

label = tk.Label(window, text="-"*50)
label.pack()

label = tk.Label(window, text="CANTIDAD DE DECIMALES (pd: 2)")
label.pack()

decimales = tk.Entry(window,width=15,)
decimales.pack()

label = tk.Label(window, text="ALTURA DE TEXTO (pd: 0.7)")
label.pack()

altura = tk.Entry(window,width=15,)
altura.pack()

label = tk.Label(window, text="ANCHO DE TEXTO (pd: 10)")
label.pack()

ancho = tk.Entry(window,width=15,)
ancho.pack()

label = tk.Label(window, text="-"*50)
label.pack()

label = tk.Label(window, text="ESTILOS")
label.pack()

texto_estilos = ttk.Combobox(width=10)
texto_estilos.pack()

label = tk.Label(window, text="-"*50)
label.pack()

button1 = tk.Button(window, text="-- CARGAR ESTILOS --", command = objecto_gui.cargar_estilos)
button1.pack()

button2 = tk.Button(window, text="ÁREA Y PERÍMETRO", command = objecto_gui.area_perimetro)
button2.pack()

button3 = tk.Button(window, text="PERÍMETRO",command = objecto_gui.perimetro)
button3.pack()

button4 = tk.Button(window, text="ÁREA", command = objecto_gui.area)
button4.pack()

window.mainloop()

