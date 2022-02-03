from typing import List
class Usuario:
    def __init__(self, dni = None, contrasenna = None, es_admin = None):
        self._dni = dni
        self._contrasenna = contrasenna
        self._ultimoAcceso = None
        self._es_admin = es_admin
    
    def getDni(self):
        return self._dni
    
    def setDni(self, dni):
        self._dni = dni

    def getContrasenna(self):
        return self._contrasenna
    
    def setContrasenna(self, contrasenna):
        self._contrasenna = contrasenna
    
    def getUltimoAcceso(self):
        return self._ultimoAcceso
    
    def setUltimoAcceso(self, ultimoAcceso):
        self._ultimoAcceso = ultimoAcceso
    
    def getEsAdmin(self):
        return self._es_admin
    
    def setEsAdmin(self, esAdmin):
        self._es_admin = esAdmin
    

    def getInfo(self):
        return "Dni: {}. \n\tContraseña:  {}. \n\tUltimo Acceso:  {}. \n\tEs Admin:  {}.".format(self._dni,self._contrasenna,self._ultimoAcceso,self._es_admin)