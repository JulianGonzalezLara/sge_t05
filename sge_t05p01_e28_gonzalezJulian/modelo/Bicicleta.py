from modelo.Mantenimiento import Mantenimiento


class Bicicleta:
    def __init__(self, fechaCompra = None, marca = None, modelo = None, tipo = None, color = None, tamannoCuadro = None, tamannoRuedas = None, precio = None, mantenimiento:Mantenimiento = []):
        self.fechaCompra = fechaCompra
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.color = color
        self.tamannoCuadro = tamannoCuadro
        self.tamannoRuedas = tamannoRuedas
        self.precio = precio
        self.mantenimiento = mantenimiento