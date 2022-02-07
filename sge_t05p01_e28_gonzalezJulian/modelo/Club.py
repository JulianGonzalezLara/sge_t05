from modelo.Cuotas import Cuotas
from modelo.Socio import Socio
from modelo.Usuario import Usuario
class Club:
    def __init__(self, nombreClub = None, cif = None, sede = None):
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
            return socio
        except Exception as exc:
            return "Ha ocurrido un error en la creacion del socio"
    
    def comprobarDni(self, dni):
        for i in self.getListaSocios():
            if i.getUsuario().getDni() == dni:
                return None
    
    def prepararDict(self):
        dictPrep=self.__dict__.copy()
        sociosAux = list()
        for i in self.getListaSocios():
            sociosAux.append(i.prepararDict())
        dictPrep["_listaSocios"]=sociosAux
        return dictPrep