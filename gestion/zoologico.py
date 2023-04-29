class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=[]

    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre=nombre

    def get_ubicacion(self):
        return self._ubicacion
    def set_ubicacion(self, ubicacion):
        self._ubicacion=ubicacion

    def get_zonas(self):
        return self._zonas
    def set_zonas(self, zonas):
        self._zonas=zonas

    def agregasZonas(self, zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        totalAnimales=0
        for i in self._zonas:
            totalAnimales+=i.cantidadAnimales()

        return totalAnimales



    