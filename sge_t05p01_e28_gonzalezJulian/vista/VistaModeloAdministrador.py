
from controlador.ControladorModulo import ControladorAdmin
from modelo.Socio import Socio

from typing import List
class VistaAdministrador:
    def __init__(self, contr: ControladorAdmin): 
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
        print("*         Zona de administración        *")
        print("*           Usuario: {}     *".format(self._controlador.getUsuarioConectado().getNombreCompleto()))
        print("*     Último acc.: {}     *".format(self._controlador.getUsuarioConectado().getUsuario().getUltimoAcceso()))
        print("*****************************************")

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
        socios.sort(key = lambda x: x.getNombreCompleto())
        texto = ""
        cont = 1
        for i in socios:
            texto += "Socio: " + str(cont) + "\n"
            texto += "Dni: {:<10} Nombre:  {:<20} \n".format(i.getUsuario().getDni(), i.getNombreCompleto())
            cont = cont+1
        
        print (texto)

    def insertarSocio(self):
        dni=str(input("Introduzca el dni: "))
        if self._controlador.comprobarDni(dni) == ("No existe"):
            contrasenna=str(input("Introduzca la contraseña: "))
            aux=input("Introduzca (True o False) si es admin: ")
            if(aux.casefold()=="true"):
                es_admin = True
            elif(aux.casefold()=="false"):
                es_admin = False
            nombreCompleto=str(input("Introduzca el nombre completo: "))
            direccion=str(input("Introduzca la direccion: "))
            telefono=str(input("Introduzca el telefono: "))
            mail=str(input("Introduzca el mail: "))
            respuesta = self._controlador.crearSocio(dni,contrasenna,es_admin,nombreCompleto,direccion,telefono,mail)
            print("----------------------------------")
            print(respuesta)
        else:
            print("El DNI ya existe")
    
    def addFamilia(self):
        sigue=True
        while(sigue==True):
            dniTitular=str(input("Introduzca el dni del socio a añadir familia: "))
            if self._controlador.comprobarDni(dniTitular) == ("Existe"):
                print("Introduzca el tipo de familiar que va a añadir")
                print("1. Pareja.")
                print("2. Hijo.")
                opc=int(input("Deme una opción: "))
                while(opc<1 and opc>2):
                    print("Opcion no valida")
                    print("1. Pareja.")
                    print("2. Hijo.")
                    opc=int(input("Deme una opción: "))
                dniFamilia=str(input("Introduzca el dni del familiar: "))
                if self._controlador.comprobarDni(dniFamilia) == ("Existe"):
                    respuesta = self._controlador.addFamilia(dniTitular,dniFamilia,opc)
                    print(respuesta)
                    print("\n-------------------------------------------")
                    print("¿Desea añadir mas familiares?")
                    print("1. Si.")
                    print("2. No.")
                    opc2=int(input("Deme una opción: "))
                    while(opc<1 and opc>2):
                        print("Opcion no valida")
                        print("1. Si.")
                        print("2. No.")
                        opc2=int(input("Deme una opción: "))
                    if(opc2 == 2):
                        sigue=False
                else:
                    print ("El dni del familiar no existe")
            else:
                print("El dni del titular no existe")
        