from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado=[]
    caballos=0
    leones=0

    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)

    @classmethod
    def get_listado(cls):
        return cls._listado
    @classmethod
    def set_listado(cls, listado):
        cls._listado=listado
    
    def get_pelaje(self):
        return self._pelaje
    def set_pelaje(self, pelaje):
        self._pelaje=pelaje

    def get_patas(self):
        return self._patas
    def set_patas(self, patas):
        self._patas=patas

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    def crearCaballo(nombre,edad,genero):
        mamifero= Mamifero(nombre,edad,"pradera",genero,True,4)
        Mamifero.caballos+=1
        return mamifero
    
    def crearLeon(nombre,edad,genero):
        mamifero=Mamifero(nombre,edad,"selva",genero,True,4)
        Mamifero.leones+=1
        return mamifero

    
