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
    def get_totalAnimales(cls):
        return cls._totalAnimales
    @classmethod
    def set_totalAnimales(cls, totalAnimales):
        cls._totalAnimales=totalAnimales

    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre=nombre

    def get_edad(self):
        return self._edad
    def set_edad(self, edad):
        self._edad=edad

    def get_habitat(self):
        return self._habitat
    def set_habitat(self, habitat):
        self._habitat=habitat

    def get_genero(self):
        return self._genero
    def set_genero(self, genero):
        self._genero=genero

    def get_zona(self):
        return self._zona
    def set_zona(self, zona):
        self._zona=zona


    @staticmethod
    def movimiento():
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        cantmamifero=len(mamifero.get_listado())
        cantave=len(ave.get_listado())
        cantreptil=len(reptil.get_listado())
        cantpez=len(pez.get_listado())
        cantanfibio=len(anfibio.get_listado())

        return "Mamiferos: ",cantmamifero,"\n", "Aves: ",cantave,"\n", "Reptiles: ",cantreptil,"\n", "Peces: ",cantpez,"\n", "Anfibios: ",cantanfibio
	
    def toString(self):
        if self.get_zona()!=None:
            return "Mi nombre es ", self.get_nombre(),", tengo una edad de " ,self.get_edad(), ", habito en ",self.get_habitat()," y mi genero es ",self.get_genero(),", la zona en la que me ubico es ",self.get_zona(),", en el ",self.get_zona().get_zoo()
        else: 
            return "Mi nombre es ", self.get_nombre(),", tengo una edad de " ,self.get_edad(), ", habito en ",self.get_habitat()," y mi genero es ",self.get_genero()
		
	