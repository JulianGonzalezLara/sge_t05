from modelo import GestionJSON
from modelo.Club import Club
from modelo.Socio import Socio
from modelo.Usuario import Usuario
from controlador.ControladorModulo import Controlador


if __name__ == "__main__":
    club = Club("Los Satanases del Infierno","L - 76298710","C/ Seis de Junio")
    socio = Socio(Usuario("78980815F","d",True),"Alfonso Garcia","d","3","m")
    socio2 = Socio(Usuario("71389546P","d",True),"Pedro Del Olmo","d","3","m")
    socios = [socio,socio2]
    club.setListaSocios(socios)
    controlador_app = Controlador(club)

    sociosAux = list()
    for i in socios:
        sociosAux.append(i.prepararDict())
    GestionJSON.guardarJSON("socios.json", sociosAux)
    sociosAux=list()