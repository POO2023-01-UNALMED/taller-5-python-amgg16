import mamifero,ave,reptil,pez,anfibio


class Animal:
    _totalAnimales=0

    def __init__(self,nombre,edad,habitat,genero):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=None
        Animal._totalAnimales+=1

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales=totalAnimales

    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre=nombre

    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad=edad

    def getHabitat(self):
        return self._habitat
    def setHabitat(self, habitat):
        self._habitat=habitat

    def getGenero(self):
        return self._genero
    def setGenero(self, genero):
        self._genero=genero

    def getZona(self):
        return self._zona
    def setZona(self, zona):
        self._zona=zona


    @staticmethod
    def movimiento():
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        cantmamifero=len(mamifero.Mamifero.getListado())
        cantave=len(ave.Ave.getListado())
        cantreptil=len(reptil.Reptil.getListado())
        cantpez=len(pez.Pez.getListado())
        cantanfibio=len(anfibio.Anfibio.getListado())

        return "Mamiferos: ",cantmamifero,"\n", "Aves: ",cantave,"\n", "Reptiles: ",cantreptil,"\n", "Peces: ",cantpez,"\n", "Anfibios: ",cantanfibio
	
    def toString(self):
        if self.get_zona()!=None: ######
            return "Mi nombre es ", self.getNombre(),", tengo una edad de " ,self.getEdad(), ", habito en ",self.getHabitat()," y mi genero es ",self.getGenero(),", la zona en la que me ubico es ",self._zona.getNombre(),", en el ",self.getZona().getZoo().getNombre()
        else: 
            return "Mi nombre es ", self.getNombre(),", tengo una edad de " ,self.getEdad(), ", habito en ",self.getHabitat()," y mi genero es ",self.getGenero()
		
	