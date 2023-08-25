##Ejemplo con celulares
#Crear clases
'''
class NombreClase():
    #atributos estaticos
    propiedadUnO  = "Valor 1"
    propiedadDos  = "Valor 2"
    propiedadTres = "valor 3"

#Objeto
nombreObjeto = NombreClase()
print(nombreObjeto.propiedadUnO)#nombre del objeto mas atributo 
print(nombreObjeto.propiedadDos)
print(nombreObjeto.propiedadTres)

'''
#Ejemplo Celulares
class Celular():
    marca = "samsung"
    modelo = "s23"
    camara = "48MP"

#Creacion de objetos, objeto es una instancia de un objeto 
Celular1 = Celular()
Celular2 = Celular()
Celular3 = Celular()
Celular4 = Celular()

# mostras propiedades del objeto
print(Celular1.marca)