from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado=[]
    iguanas=0
    serpientes=0

    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._listado.append(self)

    @classmethod
    def get_listado(cls):
        return cls._listado
    @classmethod
    def set_listado(cls, listado):
        cls._listado=listado

    def get_colorEscamas(self):
        return self._colorEscamas
    def set_colorEscamas(self, colorEscamas):
        self._colorEscamas=colorEscamas

    def get_largoCola(self):
        return self._largoCola
    def set_largoCola(self, largoCola):
        self._largoCola=largoCola

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    @staticmethod
    def movimiento():
        return "reptar"
    
    def crearIguana(nombre,edad,genero):
        reptil=Reptil(nombre, edad, "humedal",genero, "verde",3)
        Reptil.iguanas+=1
        return reptil

    def crearSerpiente(nombre,edad,genero):
        reptil=Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes+=1
        return reptil

    

    