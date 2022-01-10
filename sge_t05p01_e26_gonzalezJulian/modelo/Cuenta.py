import modelo.Movimiento

def __init__(this, dni = None, nombre = None, saldo = None, movimientos = None):
    this.numCuenta = this.numCuenta + 1
    this.dni = dni
    this.nombre = nombre
    this.saldo = saldo
    this.movimientos = movimientos

def imprimir_cuenta(this): 
    texto = ("Cuenta: ",this.numCuenta,"\n","DNI: ",this.dni,"\n","Nombre: ",this.nombre,"\n","Saldo: ",this.saldo,"\n"
    ,"Movimientos: ")
    for i in this.movimientos:
        texto += (i+1, "\n", i.cantidad, "\n", i.ingreso, "\n", i.concepto)
    
    return texto

def hacer_movimiento(this, movimiento):
    if(this.saldo >= movimiento):
        return True
    else:
        return False