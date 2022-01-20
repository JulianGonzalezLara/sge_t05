from modelo.Mantenimiento import Mantenimiento


class Bicicleta:
    def __init__(this, fechaCompra = None, marca = None, modelo = None, tipo = None, color = None, tamannoCuadro = None, tamannoRuedas = None, precio = None, mantenimiento:Mantenimiento = []):
        this.fechaCompra = fechaCompra
        this.marca = marca
        this.modelo = modelo
        this.tipo = tipo
        this.color = color
        this.tamannoCuadro = tamannoCuadro
        this.tamannoRuedas = tamannoRuedas
        this.precio = precio
        this.mantenimiento = mantenimiento