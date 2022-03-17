from modelo.Cuota import Cuota
from modelo.Socio import Socio
from modelo.Usuario import Usuario
import datetime

from typing import List
class Club:    
    #Constantes Pagos
    PAGOENERO = 15
    PAGOJULIO = 8
    #Constantes descuentos
    DESCUENTOPAREJA = 10
    DESCUENTOHIJOS = 15 
    DESCUENTOPAREJAHIJOS = 30

    def __init__(self, nombreClub = None, cif = None, sede = None):
        self._nombreClub = nombreClub
        self._cif = cif
        self._sede = sede
        self._listaSocios:List[Socio] = []
        #self.listaEventos = []
        self._saldoTotal = 0
        self._cuotas:List[Cuota] = []
    
    def getSaldoTotal(self):
        return self._saldoTotal
    
    def setSaldoTotal(self, saloTotal):
        self._saldoTotal = saloTotal
    
    def getListaCuotas(self):
        return self._cuotas
    
    def getListaCuotasSocio(self,socio:Socio):
        auxCuotas:List[Cuota] = []
        for i in self.getListaCuotas():
            if i.getSocio().getUsuario().getDni() == socio.getUsuario().getDni():
                auxCuotas.append(i)
        return auxCuotas
    
    def getListaCuotasAnio(self,anio):
        auxCuotas:List[Cuota] = []
        for i in self.getListaCuotas():
            if int(i.getAnnio()) == int(anio):
                auxCuotas.append(i)
        return auxCuotas
    
    def setListaCuotas(self, listaCuotas):
        self._cuotas = listaCuotas
    
    def annadirCuota(self, cuota):
        try:
            self._cuotas.append(cuota)
        except Exception as exc:
            return "Ha ocurrido un error en la insercion de la cuota"
    
    def getListaSocios(self):
        return self._listaSocios
    
    def setListaSocios(self, listaSocios):
        self._listaSocios = listaSocios
    
    def annadirSocio(self, socio):
        try:
            self._listaSocios.append(socio)
        except Exception as exc:
            return "Ha ocurrido un error en la insercion del socio"

    def crearUsuario(self, dni, contrasenna,es_admin):        
        try:
            usuario = Usuario(dni,contrasenna,es_admin)
            return usuario
        except Exception as exc:
            return "Ha ocurrido un error en la creacion del usuario"
    
    def crearSocio(self,usuario:Usuario, nombreCompleto, direccion, telefono, mail):        
        try:
            socio = Socio(usuario,nombreCompleto,direccion, telefono,mail)
            currentDateTime = datetime.datetime.now()
            date = currentDateTime.date()
            year = date.strftime("%Y")
            calculoCuotas = self.calculoCuotas(socio)
            tipoDescuento = self.tipoDescuento(socio)
            cuotaS = Cuota(year,socio,False,calculoCuotas,tipoDescuento,None)
            self.annadirCuota(cuotaS)
            return socio
        except Exception as exc:
            return "Ha ocurrido un error en la creacion del socio"
    
    def comprobarDni(self, dni):
        for i in self.getListaSocios():
            if i.getUsuario().getDni() == dni:
                return "Existe"
            else:
                opc = "No existe"
        return opc
    
    def socioPorDni(self, dni):
        for i in self.getListaSocios():
            if i.getUsuario().getDni() == dni:
                return i
    
    def comprobarSiEsHijo(self, dni):
        for i in self.getListaSocios():
            for j in i.getFamilia().getHijos():
                if j.getUsuario().getDni() == dni:
                    return i
    
    def comprobarSiEsPareja(self, dni):
        for i in self.getListaSocios():
            if i.getFamilia().getPareja() != None:
                if i.getFamilia().getPareja().getUsuario().getDni() == dni:
                    return i
    
    def getCuotaDni(self, dni):
        for i in self.getListaCuotas():
            if i.getSocio().getUsuario().getDni() == dni:
                return i
    
    def comprobarCuotaAnnio(self, dni, annio):
        for i in self.getListaCuotas():
            if i.getSocio().getUsuario().getDni() == dni:
                if int(i.getAnnio()) == int(annio):
                    return i
    
    def cuotasAnnio(self):
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        for i in self.getListaSocios():
            comp = self.comprobarCuotaAnnio(i.getUsuario().getDni(),year)
            if comp == None:
                calculoCuotas = self.calculoCuotas(i)
                tipoDescuento = self.tipoDescuento(i)
                cuotaS = Cuota(year,i,False,calculoCuotas,tipoDescuento,None)
                self.annadirCuota(cuotaS)
            else:
                comp.setCantidadPagar(self.calculoCuotas(i))
                comp.setTipoDescuento(self.tipoDescuento(i))
    
    def calculoCuotas(self, socio:Socio):
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        month = int(date.strftime("%m"))
        year = date.strftime("%Y")
        cantidadPagar = 0
        comprobarSiEsHijo = self.comprobarSiEsHijo(socio.getUsuario().getDni())
        if comprobarSiEsHijo == None:
            if month>0 and month < 6:
                cantidadPagar = self.PAGOENERO
            elif month>5 and month < 13:
                cantidadPagar = self.PAGOJULIO
            if socio.getFamilia().getPareja() != None and len(socio.getFamilia().getHijos()) == 0:
                descuento = cantidadPagar * (self.DESCUENTOPAREJA / 100)
                cantidadPagar = cantidadPagar - descuento
            if socio.getFamilia().getPareja() == None and len(socio.getFamilia().getHijos()) > 0:
                descuento = cantidadPagar * (self.DESCUENTOHIJOS / 100)
                cantidadPagar = cantidadPagar - descuento
            if socio.getFamilia().getPareja() != None and len(socio.getFamilia().getHijos()) > 0:
                descuento = cantidadPagar * (self.DESCUENTOPAREJAHIJOS / 100)
                cantidadPagar = cantidadPagar - descuento
        else:
            cuotaPadre = self.getCuotaDni(comprobarSiEsHijo.getUsuario().getDni())
            cantidadPagar = cuotaPadre.getCantidadPagar()
        return cantidadPagar
    
    def tipoDescuento(self, socio:Socio):
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        month = int(date.strftime("%m"))
        year = date.strftime("%Y")
        cantidadPagar = 0
        tipoDescuento = ""
        comprobarSiEsHijo = self.comprobarSiEsHijo(socio.getUsuario().getDni())
        if comprobarSiEsHijo == None:
            if month>0 and month < 6:
                cantidadPagar = self.PAGOENERO
            elif month>5 and month < 13:
                cantidadPagar = self.PAGOJULIO
            if socio.getFamilia().getPareja() == None and len(socio.getFamilia().getHijos()) == 0:
                tipoDescuento = "No se le aplica ningun descuento"
            if socio.getFamilia().getPareja() != None and len(socio.getFamilia().getHijos()) == 0:
                tipoDescuento = "Se le aplica descuento por pareja"
            if socio.getFamilia().getPareja() == None and len(socio.getFamilia().getHijos()) > 0:
                tipoDescuento = "Se le aplica descuento por tener hijos"
            if socio.getFamilia().getPareja() != None and len(socio.getFamilia().getHijos()) > 0:
                tipoDescuento = "Se le aplica descuento por pareja e hijos"
        else:
            tipoDescuento = "Se le aplica descuento por ser hijo"
        return tipoDescuento
    
    def sumarSaldoTotal(self):
        suma = 0
        for i in self.getListaCuotas():
            if i.getPagada() == True:
                suma += i.getCantidadPagar()
        self.setSaldoTotal(suma)
    
    def prepararDict(self):
        self.sumarSaldoTotal()
        dictPrep=self.__dict__.copy()
        sociosAux = list()
        for i in self.getListaSocios():
            sociosAux.append(i.prepararDict())
        dictPrep["_listaSocios"]=sociosAux
        cuotasAux = list()
        for i in self.getListaCuotas():
            cuotasAux.append(i.prepararDictCuota())
        dictPrep["_cuotas"]=cuotasAux
        return dictPrep