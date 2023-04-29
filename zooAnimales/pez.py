from zooAnimales.animal import Animal

class Pez(Animal):
    _listado=[]
    salmones=0
    bacalaos=0

    def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez._listado.append(self)

    @classmethod
    def getListado(cls):
        return cls._listado
    @classmethod
    def setListado(cls, listado):
        cls._listado=listado

    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas=colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas=cantidadAletas

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    @staticmethod
    def movimiento():
        return "nadar"
    
    def crearSalmon(nombre,edad,genero):
        pez=Pez(nombre, edad,"oceano", genero, "rojo", 6)
        Pez.salmones+=1
        return pez

    def crearBacalao(nombre,edad,genero):
        pez=Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos+=1
        return pez


