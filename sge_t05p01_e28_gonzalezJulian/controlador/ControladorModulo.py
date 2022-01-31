from modelo.Club import Club
from modelo.Usuario import Usuario
from modelo.Socio import Socio

from typing import List
class Controlador:
    def __init__(self, club: Club):
        self._club = club
        self._vistaAdmin=VistaAdministrador(self)
        self._vistaAdmin.inicio()

    def controlOpciones(self,opc):
        if (opc == 0): 
            self._vistaAdmin.salir()
        elif (opc == 1):
            self._vistaAdmin.mostrarListaSocios()
            self._vistaAdmin.inicio()
        elif (opc == 2):
            self._vistaAdmin.insertarSocio()
            self._vistaAdmin.inicio()
        else:
            pass #Confiamos en la validación del cliente porque es una app de escritorio.

    def mostrarListaSocios(self):
        return self._club.getListaSocios()

    def insertarSocio(self, dni, contrasenna, es_admin, nombreCompleto, direccion, telefono, mail):  
        try:
            usuario = Usuario.insertarUsuario(dni,contrasenna,es_admin)
            socio = Socio.insertarSocio(usuario,nombreCompleto,direccion,telefono,mail)
            self._club.annadirSocio(socio)
            print(socio)
        except Exception as exc:
            return "Ha ocurrido un error en la insercion"
        # finally:
        #     return "Insercion realizada con exito"

from vista.VistaModeloAdministrador import VistaAdministrador
