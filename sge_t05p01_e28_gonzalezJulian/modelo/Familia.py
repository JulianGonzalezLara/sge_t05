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
    
    def prepararDictFamilia(self):
        dictPrep=self.__dict__.copy()
        if(self._pareja != None):
            dictPrep["_pareja"]=self._pareja.getUsuario().prepararDictUsuario()
        if(len(self._hijos) > 0):
            hijosAux = list()
            for i in self.getHijos():
                hijosAux.append(i.getUsuario().prepararDictUsuario())
            dictPrep["_hijos"]=hijosAux
        return dictPrep