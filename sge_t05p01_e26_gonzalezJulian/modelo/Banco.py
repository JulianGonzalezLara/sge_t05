def __init__(this, nombre = None, cuentas = [], saldo = 0):
    this.nombre = nombre
    this.cuentas = cuentas
    this.saldo = saldo

def existe_cliente(this, dni):
    for i in this.cuentas:
        if (dni == i.dni):
            return dni
        else:
            return None