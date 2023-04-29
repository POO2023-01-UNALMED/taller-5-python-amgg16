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
    def get_listado(cls):
        return cls._listado
    @classmethod
    def set_listado(cls, listado):
        cls._listado=listado

    def get_colorEscamas(self):
        return self._colorEscamas
    def set_colorEscamas(self, colorEscamas):
        self._colorEscamas=colorEscamas

    def get_cantidadAletas(self):
        return self._cantidadAletas
    def set_cantidadAletas(self, cantidadAletas):
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


