
from controlador.ControladorModulo import Controlador
from modelo.Socio import Socio

from typing import List
class VistaAdministrador:
    def __init__(self, contr: Controlador): 
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

    def mostrarMenu(self):
        print("-------------------------------Menú---------------------------------")
        print("1. Ver listado completo de socios.")
        print("2. Insertar un nuevo socio (y crear su usuario).")
        print("3. Añadir a un socio su familia(pareja y/o sus hijos).")
        print("4. Ver listado completo de los próximos eventos.")
        print("5. Buscar eventos por fecha y mostrar toda su información.")
        print("6. Insertar un nuevo evento.")
        print("7. Ver el control de cuotas-socios por años.")
        print("8. Actualizar el control de cuotas-socio para el año en curso.")
        print("9. Realizar el pago de una cuota por DNI de socio.")
        print("0. Salir.")
        print("--------------------------------------------------------------------")
    
    def leerOpcionMenu(self):
        try:
            opc=int(input("Deme una opción: "))
        except:
            raise Exception("Debes introducir un número entero.")

        if (opc >=0 and opc <=9):
            return opc
        else:
            raise Exception("Debes introducir un número entero entre 0 y 9.")

    def mostrarError(self, exc):
        print("Error!! {}".format(exc))

    def salir(self):
        print("Cerrando aplicación...")
    
    def mostrarListaSocios(self):
        socios:List[Socio] = self._controlador.mostrarListaSocios()
        texto = ""
        for i in socios:
            texto += "Socio: " + i + "\n"
            texto += "Dni: {:<10}. Contraseña:  {:<20}. \n".format(i.getUsuario().getDni(), i.getNombreCompleto())
            print (texto)

    def insertarSocio(self):
        dni=str(input("Introduzca el dni: "))
        contrasenna=str(input("Introduzca la contraseña: "))
        aux=input("Introduzca (True o False) si es admin: ")
        if(aux=="True"):
            es_admin = True
        elif(aux=="False"):
            es_admin = False
        nombreCompleto=str(input("Introduzca el nombre completo: "))
        direccion=str(input("Introduzca la direccion: "))
        telefono=str(input("Introduzca el telefono: "))
        mail=str(input("Introduzca el mail: "))
        respuesta = self._controlador.insertarSocio(dni,contrasenna,es_admin,nombreCompleto,direccion,telefono,mail)
        print("----------------------------------")
        print(respuesta)