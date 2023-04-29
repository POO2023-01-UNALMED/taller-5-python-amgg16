from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado=[]
    ranas=0
    salamandras=0

    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)

    @classmethod
    def getListado(cls):
        return cls._listado
    @classmethod
    def setListado(cls, listado):
        cls._listado=listado
    
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self, colorPiel):
        self._colorPiel=colorPiel

    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self, venenoso):
        self._venenoso=venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    @staticmethod
    def movimiento():
        return "saltar"
    
    def crearRana(nombre,edad,genero):
        anfibio=Anfibio(nombre,edad, "selva",genero, "rojo", True)
        Anfibio.ranas+=1
        return anfibio

    def crearSalamandra(nombre,edad,genero):
        anfibio=Anfibio(nombre, edad, "selva",genero, "negro y amarillo", False)
        Anfibio.salamandras+=1
        return anfibio

    