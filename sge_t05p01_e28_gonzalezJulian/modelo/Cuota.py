from modelo.Socio import Socio

class Cuota:
    def __init__(self, annio = None, socio:Socio = None, pagada = False, cantidadPagar = None, tipoDescuento = None, fecha = None):
        self._annio = annio
        self._socio:Socio = socio
        self._pagada = pagada
        self._cantidadPagar = cantidadPagar
        self._tipoDescuento = tipoDescuento
        self._fecha = fecha
    
    def getAnnio(self):
        return self._annio
    def setAnnio(self, annio):
        self._annio = annio
    
    def getSocio(self):
        return self._socio
    def setSocio(self, socio):
        self._socio = socio
    
    def getPagada(self):
        return self._pagada
    def setPagada(self, pagada):
        self._pagada = pagada
    
    def getCantidadPagar(self):
        return self._cantidadPagar
    def setCantidadPagar(self, cantidadPagar):
        self._cantidadPagar = cantidadPagar
    
    def getTipoDescuento(self):
        return self._tipoDescuento
    def setTipoDescuento(self, tipoDescuento):
        self._tipoDescuento = tipoDescuento
    
    def getFecha(self):
        return self._fecha
    def setFecha(self, fecha):
        self._fecha = fecha
    
    def prepararDictCuota(self):
        dictPrep=self.__dict__.copy()
        dictPrep["_socio"]=self._socio.prepararDict()
        return dictPrep