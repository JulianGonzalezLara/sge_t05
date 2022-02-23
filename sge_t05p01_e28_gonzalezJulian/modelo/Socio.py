from modelo.Bicicleta import Bicicleta
from modelo.Familia import Familia
from modelo.Usuario import Usuario

from typing import List
class Socio:
    def __init__(self, usuario:Usuario = None, nombreCompleto = None, direccion = None, telefono = None, mail = None):
        #, bicicletas:Bicicleta = [], familia:Familia = None
        self._usuario = usuario
        self._nombreCompleto = nombreCompleto
        self._direccion = direccion
        self._telefono = telefono
        self._mail = mail
        self._bicicletas:List[Bicicleta] = []
        self._familia:Familia = Familia()

    def getUsuario(self):
        return self._usuario
    
    def setUsuario(self, usuario):
        self._usuario = usuario
    
    def getNombreCompleto(self):
        return self._nombreCompleto
    
    def setNombreCompleto(self, nombreCompleto):
        self._nombreCompleto = nombreCompleto
    
    def getBicicletas(self):
        return self._bicicletas
    
    def setBicicletas(self,bicicletas:List[Bicicleta]):
        self._bicicletas = bicicletas
    
    def getFamilia(self):
        return self._familia
    
    def setFamilia(self,familia:Familia):
        self._familia = familia
    
    def crearFamilia(self,familiar,tipoFamilia):
        try:
            if(tipoFamilia == 1):
                self._familia.setPareja(familiar)
            else:
                self._familia.addHijo(familiar)
        except Exception as exc:
            return "Ha ocurrido un error al añadir familiar"

    def prepararDict(self):
        dictPrep=self.__dict__.copy()
        dictPrep["_usuario"]=self._usuario.__dict__
        dictPrep["_familia"]=self._familia.prepararDictFamilia()
        return dictPrep

    def getInfo(self):
        return "\tUsuario: {}. \n\tNombre Completo:  {}. \n\tDireccion:  {}. \n\tTelefono:  {}. \n\tMail:  {}.".format(self._usuario.getInfo(),self._nombreCompleto,self._direccion,self._telefono,self._mail)