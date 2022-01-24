from modelo.Socio import Socio
from modelo.Usuario import Usuario
class Controlador:
    def __init__(this, socio: Socio):
        this.socio=socio
        this._vistaAdmin=VistaAdministrador(this)
        this._vistaAdmin.inicio()

    def controlOpciones(this,opc):
        if (opc == 0): 
            this._vistaAdmin.salir()
        elif (opc == 1):
            this.mostrarListaSocios()
            this._vistaAdmin.inicio()
        elif (opc == 2):
            this._vistaAdmin.insertarSocio()
            this._vistaAdmin.inicio()
        else:
            pass #Confiamos en la validación del cliente porque es una app de escritorio.

    def mostrarListaSocios(this):
        try:
            info=this.socio.getInfo()
            this._vistaAdmin.mostrarListaSocios(info)
        except:
            raise Exception("Error inesperado al tratar de leer los datos del banco.")

    def insetarSocio(this, dni, contrasenna, ultimoAcceso, es_admin, nombreCompleto, direccion, telefono, mail):        
        try:
            usuario = Usuario(dni,contrasenna, ultimoAcceso, es_admin)
            socio = Socio(nombreCompleto,direccion, telefono,mail)
        except Exception as exc:
            return "Ha ocurrido un error en la insercion"
        finally:
            return "Insercion realizada con exito"

from vista.VistaModeloAdministrador import VistaAdministrador
