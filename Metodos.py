## los metodos son funciones, todas las funciones dentro de una 
## clase son metodos, se les debe dar el parametro self

class Celular:
## metodo constructor 
    def __init__(self,marca,modelo,camara):#constructor
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    #funcion convertida en metodo    
    def cortar(self):
        print("Ingresa llamada")
    def llamar(self):
        print("Estas realizando una llamada")
        
celular1 = Celular("nokia","1100","40mpx")#Objetos
celular2 = Celular("samsung","s13","50mpx")#Objetos

print(celular1.marca)
print(celular2.modelo)
##Impresion del metodo 
print(celular2.llamar())#forma de convocar el metodo 
