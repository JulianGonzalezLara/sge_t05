from modelo import GestionJSON
from modelo.Club import Club
from modelo.Usuario import Usuario
from modelo.Socio import Socio

from typing import List

class ControladorSocios:
    def __init__(self, club: Club):
        self._club = club
        self._vistaSocio=VistaSocio(self)
        self._vistaSocio.inicio()

    def controlOpciones(self,opc):
        if (opc == 0): 
            self._vistaSocio.salir()
        elif (opc == 1):
            self._vistaSocio.mostrarListaSocios()
            self._vistaSocio.inicio()
        elif (opc == 2):
            pass
        elif (opc == 3):
            pass
        elif (opc == 4):
            pass
        else:
            pass #Confiamos en la validación del cliente porque es una app de escritorio.

    def mostrarListaSocios(self):
        return self._club.getListaSocios()

    def crearSocio(self, dni, contrasenna, es_admin, nombreCompleto, direccion, telefono, mail):  
        try: 
            usuario = self._club.crearUsuario(dni,contrasenna,es_admin)
            socio = self._club.crearSocio(usuario,nombreCompleto,direccion,telefono,mail)
            self._club.annadirSocio(socio)
        except Exception as exc:
            return "Ha ocurrido un error en la insercion"
    
    def crearJson(self):
        sociosAux = list()
        for i in self._club.getListaSocios():
            sociosAux.append(i.prepararDict())
        GestionJSON.guardarJSON("socios.json", sociosAux)
        sociosAux=list()
    
    def leerJSON(self):
        listaSocios=list()
        listaSociosJson=GestionJSON.leerJSON("socios.json") 
        for i in listaSociosJson:
            listaSocios.append(Socio(Usuario(i["_usuario"]["_dni"],i["_usuario"]["_contrasenna"],i["_usuario"]["_es_admin"]), i["_nombreCompleto"], i["_direccion"], i["_telefono"], i["_mail"]))
        
        return listaSocios

from vista.VistaModeloSocio import VistaSocio
