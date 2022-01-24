from modelo.Bicicleta import Bicicleta
from modelo.Familia import Familia
from modelo.Usuario import Usuario


class Socio:
    def __init__(this, usuario:Usuario = None, nombreCompleto = None, direccion = None, telefono = None, mail = None):
        #, bicicletas:Bicicleta = [], familia:Familia = None
        this._usuario = usuario
        this._nombreCompleto = nombreCompleto
        this._direccion = direccion
        this._telefono = telefono
        this._mail = mail
        #this.bicicletas = bicicletas
        #this.familia = familia

    def getInfo(this):
        return "\tUsuario: {}. \n\tNombre Completo:  {}. \n\tDireccion:  {}. \n\tTelefono:  {}. \n\tMail:  {}.".format(this._usuario.getInfo(),this._nombreCompleto,this._direccion,this._telefono,this._mail)