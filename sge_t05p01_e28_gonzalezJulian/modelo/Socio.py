from modelo.Bicicleta import Bicicleta
from modelo.Familia import Familia
from modelo.Usuario import Usuario
from modelo.Socio import Socio

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
        self._familia:Familia = None
        self._socios :List[Socio] = [Socio(Usuario("71298765F","holaqtal","23/1/2022",True),"Jose Juan Garcia del Amo","direccion","699372817","mail@gmail.com")]

    def getBicicletas(self):
        return self._bicicletas
    
    def setBicicletas(self,bicicletas:List[Bicicleta]):
        self._bicicletas = bicicletas
    
    def getFamilia(self):
        return self._familia
    
    def setFamilia(self,familia:Familia):
        self._familia = familia
    
    def getListaSocios(self):
        return self._socios
    
    def setListaSocios(self,listaSocios:List[Socio]):
        self._socios = listaSocios
    
    def insertarSocio(self,usuario:Usuario, nombreCompleto, direccion, telefono, mail):        
        try:
            socio = Socio(usuario,nombreCompleto,direccion, telefono,mail)
            self._socios.append(socio)
        except Exception as exc:
            return "Ha ocurrido un error en la insercion"
        finally:
            return "Insercion realizada con exito"

    def getInfo(self):
        return "\tUsuario: {}. \n\tNombre Completo:  {}. \n\tDireccion:  {}. \n\tTelefono:  {}. \n\tMail:  {}.".format(self._usuario.getInfo(),self._nombreCompleto,self._direccion,self._telefono,self._mail)