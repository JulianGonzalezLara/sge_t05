from typing import List
class Usuario:
    def __init__(self, dni = None, contrasenna = None, ultimoAcceso = None, es_admin = None):
        self._dni = dni
        self._contrasenna = contrasenna
        self._ultimoAcceso = ultimoAcceso
        self._es_admin = es_admin
        self._usuarios :List[Usuario] = []
    
    def getListaUsuarios(self):
        return self._usuarios
    
    def setListaSocios(self,listaUsuarios:List[Usuario]):
        self._usuarios = listaUsuarios
    
    def insertarUsuario(self, dni, contrasenna, ultimoAcceso, es_admin):        
        try:
            usuario = Usuario(dni,contrasenna, ultimoAcceso, es_admin)
            self._usuarios.append(usuario)
        except Exception as exc:
            return "Ha ocurrido un error en la insercion del usuario"
        finally:
            return "Insercion realizada con exito"

    def getInfo(self):
        return "Dni: {}. \n\tContraseña:  {}. \n\tUltimo Acceso:  {}. \n\tEs Admin:  {}.".format(self._dni,self._contrasenna,self._ultimoAcceso,self._es_admin)