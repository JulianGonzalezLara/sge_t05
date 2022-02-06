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
    if len(sys.argv) == 6:
        if sys.argv[5] == "-A":
            controlador_Admin = ControladorAdmin(club)
    elif len(sys.argv) == 5:
        controlador_Socio = ControladorSocios(club)
    else:
        print ("El numero de parametros introducido es incorrecto")

