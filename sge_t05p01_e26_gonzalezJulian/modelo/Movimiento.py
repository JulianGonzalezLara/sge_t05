import modelo.Fecha as Fecha

def __init__(this, cantidad = 0, ingreso = False, concepto = None):
    this.cantidad = cantidad
    this.ingreso = ingreso
    this.concepto = concepto

def __str__(this): 
    return(this.cantidad,"\n",this.ingreso,"\n",this.concepto)