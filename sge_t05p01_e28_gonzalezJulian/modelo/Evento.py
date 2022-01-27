from modelo.Club import Club
from modelo.Socio import Socio


class Evento:
    def __init__(self, fechaEvento = None, maxFechaInscripcion = None, localidad = None, provincia = None, organizador:Club = None, kmTotales = None, precio = None, listSocios:Socio = []):
        self.fechaEvento = fechaEvento
        self.maxFechaInscripcion = maxFechaInscripcion
        self.localidad = localidad
        self.provincia = provincia
        self.organizador =organizador
        self.kmTotales = kmTotales
        self.precio = precio
        self.listSocios = listSocios