import datetime

class Fecha:
    def __init__(this, dia = 0, mes = 0, annio = 0):
        this.dia = dia
        this.mes = mes
        this.annio = annio

    def __str__(this): 
        return(this.dia,"/",this.mes,"/",this.annio)

    def fechaActual(this):
        this.dia = datetime.datetime.now().day
        this.mes = datetime.datetime.now().month
        this.annio = datetime.datetime.now().year