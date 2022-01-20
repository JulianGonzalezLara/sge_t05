from modelo.Cuotas import Cuotas


class Club:
    def __init__(this, nombreClub = None, cif = None, sede = None, listaSocios = [], listaEventos = [], saldoTotal = None,cuotas:Cuotas = []):
        this.nombreClub = nombreClub
        this.cif = cif
        this.sede = sede
        this.listaSocios = listaSocios
        this.listaEventos = listaEventos
        this.saldoTotal = saldoTotal
        this.cuotas = cuotas