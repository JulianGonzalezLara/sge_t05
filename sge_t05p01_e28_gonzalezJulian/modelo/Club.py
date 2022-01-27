from modelo.Cuotas import Cuotas


class Club:
    def __init__(self, nombreClub = None, cif = None, sede = None, listaSocios = [], listaEventos = [], saldoTotal = None,cuotas:Cuotas = []):
        self.nombreClub = nombreClub
        self.cif = cif
        self.sede = sede
        self.listaSocios = listaSocios
        self.listaEventos = listaEventos
        self.saldoTotal = saldoTotal
        self.cuotas = cuotas