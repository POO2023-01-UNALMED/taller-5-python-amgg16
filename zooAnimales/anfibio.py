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
    def get_listado(cls):
        return cls._listado
    @classmethod
    def set_listado(cls, listado):
        cls._listado=listado
    
    def get_colorPiel(self):
        return self._colorPiel
    def set_colorPiel(self, colorPiel):
        self._colorPiel=colorPiel

    def get_venenoso(self):
        return self._venenoso
    def set_venenoso(self, venenoso):
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

    