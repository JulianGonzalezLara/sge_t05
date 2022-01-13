from modelo.Fecha import Fecha

class Movimiento:
    def __init__(this, cantidad = 0, ingreso = False, concepto = None):
        this.cantidad = cantidad
        this.ingreso = ingreso
        this.concepto = concepto

    def __str__(this): 
        return(this.cantidad,"\n",this.ingreso,"\n",this.concepto)