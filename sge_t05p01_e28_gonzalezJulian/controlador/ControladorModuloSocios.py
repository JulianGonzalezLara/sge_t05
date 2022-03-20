import datetime
from modelo import GestionJSON
from modelo.Club import Club
from modelo.Usuario import Usuario
from modelo.Socio import Socio

from typing import List

class ControladorSocios:
    def __init__(self, club: Club, usuario: Socio):
        self._club = club
        self._usuarioConectado = usuario
        self._vistaSocio=VistaSocio(self)
        self._vistaSocio.mostrarMenuZona()
        self._vistaSocio.inicio()

    def controlOpciones(self,opc):
        if (opc == 0): 
            now = datetime.datetime.now()
            self._usuarioConectado.getUsuario().setUltimoAcceso(("{}-{}-{} {}:{}:{}".format(now.day, now.month, now.year, now.hour, now.minute, now.second)))
            self.crearJson()
            self._vistaSocio.salir()
        elif (opc == 1):
            input("Press Enter to continue...")
            self._vistaSocio.inicio()
        elif (opc == 2):
            input("Press Enter to continue...")
            self._vistaSocio.inicio()
        elif (opc == 3):
            input("Press Enter to continue...")
            self._vistaSocio.inicio()
        elif (opc == 4):
            input("Press Enter to continue...")
            self._vistaSocio.inicio()
        elif (opc == 5):
            input("Press Enter to continue...")
            self._vistaSocio.inicio()
        elif (opc == 6):
            input("Press Enter to continue...")
            self._vistaSocio.inicio()
        elif (opc == 7):
            self._vistaSocio.mostrarFamilia()
            input("Press Enter to continue...")
            self._vistaSocio.inicio()
        elif (opc == 8):
            self._vistaSocio.mostrarCuotas()
            input("Press Enter to continue...")
            self._vistaSocio.inicio()
        else:
            pass #Confiamos en la validación del cliente porque es una app de escritorio.

    def mostrarFamilia(self):
        return self._club.socioPorDni(self.getUsuarioConectado().getUsuario().getDni())

    def crearSocio(self, dni, contrasenna, es_admin, nombreCompleto, direccion, telefono, mail):  
        try: 
            usuario = self._club.crearUsuario(dni,contrasenna,es_admin)
            socio = self._club.crearSocio(usuario,nombreCompleto,direccion,telefono,mail)
            self._club.annadirSocio(socio)
        except Exception as exc:
            return "Ha ocurrido un error en la insercion"
    
    def getUsuarioConectado(self):
        return self._usuarioConectado

    def socioPorDni(self,dni):
        return self._club.socioPorDni(dni)
    
    def mostrarCuotas(self):
        return self._club.getListaCuotasSocio(self.getUsuarioConectado())
    
    def crearJson(self):
        clubAux = self._club.prepararDict()
        GestionJSON.guardarJSON("club.json", clubAux)

from vista.VistaModeloSocio import VistaSocio
