
from controlador.ControladorModuloSocios import ControladorSocios
from typing import List

from modelo.Cuota import Cuota

class VistaSocio:
    def __init__(self, contr: ControladorSocios): 
        self._controlador=contr

    def inicio(self):
        self.mostrarMenu()
        try:
            opc=self.leerOpcionMenu()
            self._controlador.controlOpciones(opc)
        except Exception as exc:
            self.mostrarError(exc)
        finally:
            self.salir
    
    def mostrarMenuZona(self):
        print("*****************************************")
        print("*           LOS SATANASES DEL           *")
        print("*             INFIERNO APP              *")
        print("*****************************************")
        print("*             Zona de socios            *")
        print("*           Usuario: {:<19}*".format(self._controlador.getUsuarioConectado().getNombreCompleto()))
        print("*     Último acc.: {:<21}*".format(self._controlador.getUsuarioConectado().getUsuario().getUltimoAcceso()))
        print("*****************************************")

    def mostrarMenu(self):
        print("-------------------------------Menú---------------------------------")
        print("1. Ver mis próximos eventos y la lista de inscritos")
        print("2. Ver y apuntarme (si me gusta) a eventos abiertos.")
        print("3. Ver mis bicicletas.")
        print("4. Ver mis reparaciones/mantenimientos.")
        print("5. Añadir nueva bicicleta.")
        print("6. Añadir reparación/mantenimiento a una de mis bicicletas.")
        print("7. Ver mi familia")
        print("8. Ver mi histórico y estado de cuotas con toda su información.")
        print("0. Salir.")
        print("--------------------------------------------------------------------")
    
    def leerOpcionMenu(self):
        try:
            opc=int(input("Deme una opción: "))
        except:
            raise Exception("Debes introducir un número entero.")

        if (opc >=0 and opc <=8):
            return opc
        else:
            raise Exception("Debes introducir un número entero entre 0 y 8.")

    def mostrarError(self, exc):
        print("Error!! {}".format(exc))

    def salir(self):
        print("Cerrando aplicación...")
        exit()
    
    def mostrarFamilia(self):
        respuesta = self._controlador.mostrarFamilia()
        print("--------------------------------------------------------------------")
        if respuesta.getFamilia().getPareja() != None:
            print("Pareja: {:<10}  ,  {:<10} \n".format(respuesta.getUsuario().getDni(),self._controlador.socioPorDni(respuesta.getFamilia().getPareja().getUsuario().getDni()).getNombreCompleto()))
        else:
            print("No tiene pareja")
        
        if len(respuesta.getFamilia().getHijos()) > 0:
            print("Hijos:")
            for i in respuesta.getFamilia().getHijos():
                print("Hijo: {:<10}  ,  {:<10} \n".format(i.getUsuario().getDni(),self._controlador.socioPorDni(i.getUsuario().getDni()).getNombreCompleto()))
        else:
            print("No tiene hijos")
    
    def mostrarCuotas(self):
        cuotas:List[Cuota] = self._controlador.mostrarCuotas()
        texto = ""
        pagado = ""
        fecha = ""
        for i in cuotas:
            if i.getPagada():
                pagado = "Pagado"
            else:
                pagado = "No Pagado"
            
            if i.getFecha() == None:
                fecha = ""
            else:
                fecha = i.getFecha()
            texto += "Año: {:<6} Pagada:  {:<10} Cantidad:  {:<10} Fecha:  {:<10} Tipo descuento:  {:<20} \n".format(i.getAnnio(), pagado, i.getCantidadPagar(), fecha, i.getTipoDescuento())
    
        print (texto)