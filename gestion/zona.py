class Zona:
    def __init__(self,nombre, zoo):
        self._nombre=nombre
        self._zoo=zoo
        self._animales=[]

    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre=nombre

    def get_zoo(self):
        return self._zoo
    def set_zoo(self, zoo):
        self._zoo=zoo

    def get_animales(self):
        return self._animales
    def set_animales(self, animales):
        self._animales=animales

    def agregarAnimales(self,animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)