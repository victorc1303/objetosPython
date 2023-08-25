##propiedades de instancia sin parentesis

class Celular:
## metodo constructor 
    def __init__(self,marca,modelo,camara):#constructor
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
celular1 = Celular("nokia","1100","40mpx")#Objetos
celular2 = Celular("samsung","s13","50mpx")#Objetos

print(celular1.marca)
print(celular2.modelo)