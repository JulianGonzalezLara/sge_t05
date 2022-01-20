from modelo.Socio import Socio


class Cuotas:
    def __init__(this, annio = None, socio:Socio = None, pagada = False, cantidadPagar = None, tipoDescuento = None, fecha = None):
        this.annio = annio
        this.socio = socio
        this.pagada = pagada
        this.cantidadPagar = cantidadPagar
        this.tipoDescuento = tipoDescuento
        this.fecha = fecha