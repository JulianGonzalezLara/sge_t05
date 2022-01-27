from modelo.Socio import Socio

class Cuotas:
    def __init__(self, annio = None, socio:Socio = None, pagada = False, cantidadPagar = None, tipoDescuento = None, fecha = None):
        self.annio = annio
        self.socio = socio
        self.pagada = pagada
        self.cantidadPagar = cantidadPagar
        self.tipoDescuento = tipoDescuento
        self.fecha = fecha