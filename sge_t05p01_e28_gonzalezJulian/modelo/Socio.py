from modelo.Bicicleta import Bicicleta
from modelo.Familia import Familia
from modelo.Usuario import Usuario


class Socio:
    def __init__(this, usuario:Usuario = None, nombreCompleto = None, direccion = None, telefono = None, mail = None, bicicletas:Bicicleta = [], familia:Familia = None):
        this.usuario = usuario
        this.nombreCompleto = nombreCompleto
        this.direccion = direccion
        this.telefono = telefono
        this.mail = mail
        this.bicicletas = bicicletas
        this.familia = familia