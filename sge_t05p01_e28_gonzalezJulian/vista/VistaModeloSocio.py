
from controlador.ControladorModulo import Controlador

class VistaSocio:
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
    
    def leerOpcionMenu(this):
        try:
            opc=int(input("Deme una opción: "))
        except:
            raise Exception("Debes introducir un número entero.")

        if (opc >=0 and opc <=8):
            return opc
        else:
            raise Exception("Debes introducir un número entero entre 0 y 8.")

    def mostrarError(this, exc):
        print("Error!! {}".format(exc))

    def salir(this):
        print("Cerrando aplicación...")
    
    def mostrarEventosYLista(this,info):
        print(info)