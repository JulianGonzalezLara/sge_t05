from modelo.Cuotas import Cuotas
class Club:
    def __init__(self, nombreClub = None, cif = None, sede = None):
    #, listaSocios = [], listaEventos = [], saldoTotal = None,cuotas:Cuotas = []
        self._nombreClub = nombreClub
        self._cif = cif
        self._sede = sede
        self._listaSocios = []
        #self.listaEventos = listaEventos
        #self.saldoTotal = saldoTotal
        #self.cuotas = cuotas
    
    def getListaSocios(self):
        return self._listaSocios
    
    def setListaSocios(self, listaSocios):
        self._listaSocios = listaSocios
    
    def annadirSocio(self, socio):
        self._listaSocios.append(socio)