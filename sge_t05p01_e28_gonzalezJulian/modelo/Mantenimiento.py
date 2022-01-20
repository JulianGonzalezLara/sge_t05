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
    def __init__(this, fecha = None, coste = None, descripcion = None, categoria:Categoria = None):
        this.fecha = fecha
        this.coste = coste
        this.descripcion = descripcion
        this.categoria = categoria