from typing import List

class Familia:
    def __init__(self):
        #, pareja:Socio = None, hijos:List[Socio]=[]
        self._pareja = None
        self._hijos = []
    
    def getPareja(self):
        return self._pareja

    def setPareja(self, pareja):
        self._pareja = pareja
    
    def getHijos(self):
        return self._hijos
    
    def setHijos(self, hijos):
        self._hijos = hijos
    
    def addHijo(self, hijo):
        self._hijos.append(hijo)
    
    def prepararDict(self):
        dictPrep=self.__dict__.copy()
        dictPrep["_pareja"]=self._pareja.__dict__
        sociosAux = list()
        for i in self.getHijos():
            sociosAux.append(i.__dict__)
        dictPrep["_hijos"]=sociosAux
        return dictPrep