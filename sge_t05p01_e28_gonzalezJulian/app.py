from modelo.Club import Club
from modelo.Socio import Socio
from modelo.Usuario import Usuario
from controlador.ControladorModulo import Controlador


if __name__ == "__main__":
    club = Club("Los Satanases del Infierno","L - 76298710","C/ Seis de Junio")
    controlador_app = Controlador(club)