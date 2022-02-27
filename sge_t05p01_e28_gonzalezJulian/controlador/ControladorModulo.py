from datetime import datetime
from modelo import GestionJSON
from modelo.Club import Club
from modelo.Usuario import Usuario
from modelo.Socio import Socio

from typing import List
class ControladorAdmin:
    def __init__(self, club: Club, usuario: Socio):
        self._club = club
        self._usuarioConectado = usuario
        self._vistaAdmin=VistaAdministrador(self)
        self._vistaAdmin.mostrarMenuZona()
        self._vistaAdmin.inicio()

    def controlOpciones(self,opc):
        if (opc == 0): 
            now = datetime.now()
            self._usuarioConectado.getUsuario().setUltimoAcceso(("{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)))
            self.crearJson()
            self._vistaAdmin.salir()
        elif (opc == 1):
            self._vistaAdmin.mostrarListaSocios()
            input("Press Enter to continue...")
            self._vistaAdmin.inicio()
        elif (opc == 2):
            self._vistaAdmin.insertarSocio()            
            input("Press Enter to continue...")
            self._vistaAdmin.inicio()
        elif (opc == 3):
            self._vistaAdmin.addFamilia()
            input("Press Enter to continue...")
            self._vistaAdmin.inicio()
        elif (opc == 4):
            input("Press Enter to continue...")
            self._vistaAdmin.inicio()
        else:
            pass #Confiamos en la validación del cliente porque es una app de escritorio.

    def mostrarListaSocios(self):
        return self._club.getListaSocios()
    
    def comprobarDni(self,dni):
        respuesta = self._club.comprobarDni(dni)
        return respuesta

    def crearSocio(self, dni, contrasenna, es_admin, nombreCompleto, direccion, telefono, mail):  
        try: 
            usuario = self._club.crearUsuario(dni,contrasenna,es_admin)
            socio = self._club.crearSocio(usuario,nombreCompleto,direccion,telefono,mail)
            self._club.annadirSocio(socio)
        except Exception as exc:
            return "Ha ocurrido un error en la insercion"
    
    def getUsuarioConectado(self):
        return self._usuarioConectado
    
    def crearJson(self):
        clubAux = self._club.prepararDict()
        GestionJSON.guardarJSON("club.json", clubAux)
    
    def addFamilia(self,dniTitular,dniFamilia,tipoFamilia):
        socioTitular:Socio = self._club.socioPorDni(dniTitular)
        socioFamilia:Socio = self._club.socioPorDni(dniFamilia)
        respuesta = socioTitular.crearFamilia(socioFamilia,tipoFamilia)

        if tipoFamilia == 1:
            socioFamilia.crearFamilia(socioTitular,tipoFamilia)
        else:
            if socioTitular.getFamilia().getPareja() != None:
                socioPareja:Socio = self._club.socioPorDni(socioTitular.getFamilia().getPareja().getUsuario().getDni())
                socioPareja.crearFamilia(socioFamilia,tipoFamilia)

        return respuesta


from vista.VistaModeloAdministrador import VistaAdministrador
