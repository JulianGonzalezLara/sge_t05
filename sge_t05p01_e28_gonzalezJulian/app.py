import sys
from modelo import GestionJSON
from modelo.Club import Club
from modelo.Socio import Socio
from modelo.Usuario import Usuario
from controlador.ControladorModulo import ControladorAdmin
from controlador.ControladorModuloSocios import ControladorSocios

if __name__ == "__main__":
    # club = Club("Los Satanases del Infierno","L - 76298710","C/ Seis de Junio")
    # socio = Socio(Usuario("78980815F","d",True),"Alfonso Garcia","d","3","m")
    # socio2 = Socio(Usuario("71389546P","d",True),"Pedro Del Olmo","d","3","m")
    # socio3 = Socio(Usuario("76389556P","d",True),"Antonio Perez","d","3","m")
    # socios = [socio,socio2,socio3]
    #socios=GestionJSON.leerJSONSocios("socios.json") 
    # club.setListaSocios(socios)
    club=GestionJSON.leerJSONClub("club.json")
    # controlador_Admin = ControladorAdmin(club, club.getListaSocios()[0])

    if len(sys.argv) == 6:
        if sys.argv[5] == "-A":
            for c in club.getListaSocios():
                if sys.argv[1] == "-u":
                    if c.getUsuario().getDni() == sys.argv[2]:
                        if sys.argv[3] == "-p":
                            if c.getUsuario().getContrasenna() == sys.argv[4]:
                                if c.getUsuario().getEsAdmin() == True:
                                    controlador_Admin = ControladorAdmin(club, c)
                                else:
                                    print("El usuario no es admin")
                                    exit()
                            else:
                                print("La contraseña no es valida")
                                exit()
                        else:
                            print("El parametro 3 es incorrecto")
                            exit()
                    else:
                        print("El usuario no existe")
                        exit()
                else:
                    print("El parametro 2 es incorrecto")
                    exit()
    elif len(sys.argv) == 5:
        for c in club.getListaSocios():
                if sys.argv[1] == "-u":
                    if c.getUsuario().getDni() == sys.argv[2]:
                        if sys.argv[3] == "-p":
                            controladorSocio = ControladorSocios(club, c)
                        else:
                            print("El parametro 3 es incorrecto")
                            exit()
                    else:
                        print("El usuario no existe")
                        exit()
                else:
                    print("El parametro 2 es incorrecto")
                    exit()
    else:
        print ("El numero de parametros introducido es incorrecto")

