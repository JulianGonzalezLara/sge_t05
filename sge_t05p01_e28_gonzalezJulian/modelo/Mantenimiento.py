from enum import Enum

class Categoria(Enum):
    ruedas = 'ruedas'
    frenos = 'frenos'
    asiento = 'asiento'
    cuadro = 'cuadro'
    delantera = 'delantera'
    trasera = 'trasera'
    otros = 'otros'

class Mantenimiento:
    def __init__(self, fecha = None, coste = None, descripcion = None, categoria:Categoria = None):
        self.fecha = fecha
        self.coste = coste
        self.descripcion = descripcion
        self.categoria = categoria