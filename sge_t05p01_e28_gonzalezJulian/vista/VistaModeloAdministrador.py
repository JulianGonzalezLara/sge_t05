
from controlador.ControladorModulo import Controlador

class VistaAdministrador:
    def __init__(this, contr: Controlador): 
        this._controlador=contr

    def inicio(this):
        this.mostrarMenu()
        try:
            opc=this.leerOpcionMenu()
            this._controlador.controlOpciones(opc)
        except Exception as exc:
            this.mostrarError(exc)
        finally:
            this.salir

    def mostrarMenu(this):
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
    
    def leerOpcionMenu(this):
        try:
            opc=int(input("Deme una opción: "))
        except:
            raise Exception("Debes introducir un número entero.")

        if (opc >=0 and opc <=9):
            return opc
        else:
            raise Exception("Debes introducir un número entero entre 0 y 9.")

    def mostrarError(this, exc):
        print("Error!! {}".format(exc))

    def salir(this):
        print("Cerrando aplicación...")
    
    def mostrarListaSocios(this,info):
        print(info)

    def insertarSocio(this):
        dni=str(input("Introduzca el dni: "))
        contrasenna=str(input("Introduzca la contraseña: "))
        ultimoAcceso=str(input("Introduzca el ultimo acceso: "))
        es_admin=str(input("Introduzca (True o False) si es admin: "))
        nombreCompleto=str(input("Introduzca el nombre completo: "))
        direccion=str(input("Introduzca la direccion: "))
        telefono=str(input("Introduzca el telefono: "))
        mail=str(input("Introduzca el mail: "))
        respuesta = this._controlador.insetarSocio(dni,contrasenna, ultimoAcceso, es_admin,nombreCompleto,direccion,telefono,mail)
        print("----------------------------------")
        print(respuesta)