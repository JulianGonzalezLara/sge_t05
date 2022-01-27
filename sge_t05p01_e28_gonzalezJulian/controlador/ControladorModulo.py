from modelo.Usuario import Usuario
from modelo.Socio import Socio

from typing import List
class Controlador:
    def __init__(self, socio: Socio):
        self._socio=socio
        self._socios :List[Socio] = [self._socio]
        self._vistaAdmin=VistaAdministrador(self)
        self._vistaAdmin.inicio()

    def controlOpciones(self,opc):
        if (opc == 0): 
            self._vistaAdmin.salir()
        elif (opc == 1):
            self.mostrarListaSocios()
            self._vistaAdmin.inicio()
        elif (opc == 2):
            self._vistaAdmin.insertarSocio()
            self._vistaAdmin.inicio()
        else:
            pass #Confiamos en la validación del cliente porque es una app de escritorio.

    def mostrarListaSocios(self):
        try:
            info = ""
            for i in self._socios:
                info += i.getInfo() + " \n"
                
            self._vistaAdmin.mostrarListaSocios(info)
        except:
            raise Exception("Error inesperado al tratar de leer los datos de los socios.")

    def insertarSocio(self, dni, contrasenna, ultimoAcceso, es_admin, nombreCompleto, direccion, telefono, mail):        
        try:
            usuario = Usuario(dni,contrasenna, ultimoAcceso, es_admin)
            socio = Socio(usuario,nombreCompleto,direccion, telefono,mail)
            self._socios.append(socio)
        except Exception as exc:
            return "Ha ocurrido un error en la insercion"
        finally:
            return "Insercion realizada con exito"

from vista.VistaModeloAdministrador import VistaAdministrador
