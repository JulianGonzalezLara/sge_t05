from modelo.Socio import Socio
from modelo.Usuario import Usuario
from controlador.ControladorModulo import Controlador


if __name__ == "__main__":
    usuario = Usuario("71298765F","holaqtal","23/1/2022",True)
    socio = Socio(usuario,"Jose Juan Garcia del Amo","direccion","699372817","mail@gmail.com")
    controlador_app = Controlador(socio)