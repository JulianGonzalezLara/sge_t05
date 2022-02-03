from modelo import GestionJSON
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
        elif (opc == 3):
            self.crearJson()
            self._vistaAdmin.inicio()
        elif (opc == 4):
            self.leerJSON()
            self._vistaAdmin.inicio()
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

from vista.VistaModeloAdministrador import VistaAdministrador
