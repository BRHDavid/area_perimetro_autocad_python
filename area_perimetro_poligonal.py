from inicializador import Inicializador
from grupo_seleccion import Seleccion
from pyautocad import APoint as AP
from time import sleep

class AreaPoligonal(Inicializador, Seleccion):
    def __init__(self):
        Inicializador.__init__(self)
        self.text_style = []
        self.texto = str
    
    def propiedades(self, texto_estilo , decimal = 2, height = 0.7, width = 10):
        self.decimal = decimal
        self.height = height #d
        self.width = width
        self.texto_estilo = texto_estilo
    
    def selection_style_texto(self):
        for i in self.doc.TextStyles:
            self.text_style.append(i.name)
        return self.text_style
    
    def text(self):
        self.point_text = self.doc.Utility.GetPoint()
        sleep(0.5)
        
        self.text_model = self.acad.model.AddMText(AP(self.point_text[0], 
                                                      self.point_text[1], 
                                                      self.point_text[2]),
                   self.width,
                   self.texto)
        
        self.text_model.height = self.height
        self.text_model.styleName = self.texto_estilo
    
    def area_perimetro(self)-> float:
        Seleccion.__init__(self)
        for elemento in self.grupo:
            self.get_area = round(elemento.Area, self.decimal)
            self.get_perimetro = round(elemento.Length, self.decimal)
            self.texto = f"Área = {self.get_area}m2\nPerímetro = {self.get_perimetro}m"
            self.text()
    
    def area(self) -> float:
        Seleccion.__init__(self)
        
        for elemento in self.grupo:
            self.get_area = round(elemento.Area, self.decimal)
            self.texto = f"Área = {self.get_area}m2"
            self.text()
            
    def perimetro(self)  -> float:
        Seleccion.__init__(self)
        
        for elemento in self.grupo:
            self.get_perimetro = round(elemento.Length, self.decimal)
            self.texto = f"Perímetro = {self.get_perimetro}m"
            self.text()
    
                
if __name__ == "__main__":
    object1 = AreaPoligonal()
    object1.propiedades("Standard")
    object1.area_perimetro()

"""Programado por DHBR. - Marzo 2024"""
    
        
        

    
