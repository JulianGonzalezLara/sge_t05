from modelo.Club import Club
from modelo.Socio import Socio


class Evento:
    def __init__(this, fechaEvento = None, maxFechaInscripcion = None, localidad = None, provincia = None, organizador:Club = None, kmTotales = None, precio = None, listSocios:Socio = []):
        this.fechaEvento = fechaEvento
        this.maxFechaInscripcion = maxFechaInscripcion
        this.localidad = localidad
        this.provincia = provincia
        this.organizador =organizador
        this.kmTotales = kmTotales
        this.precio = precio
        this.listSocios = listSocios