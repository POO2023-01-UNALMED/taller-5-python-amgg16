from zooAnimales.animal import Animal

class Ave(Animal):
    _listado=[]
    halcones=0
    aguilas=0

    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)

    @classmethod
    def get_listado(cls):
        return cls._listado
    @classmethod
    def set_listado(cls, listado):
        cls._listado=listado

    def get_colorPlumas(self):
        return self._colorPlumas
    def set_colorPlumas(self, colorPlumas):
        self._colorPlumas=colorPlumas

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    @staticmethod
    def movimiento():
        return "volar" 
    
    def crearHalcon (nombre,edad,genero):
        ave=Ave(nombre,edad, "montanas", genero, "cafe glorioso")
        Ave.halcones+=1
        return ave
    
    def crearAguila(nombre,edad,genero):
        ave=Ave(nombre,edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilar=1
        return ave
