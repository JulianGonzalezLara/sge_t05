import json
from modelo.Club import Club
from modelo.Socio import Socio
from modelo.Usuario import Usuario

def guardarJSON(rutaFich, coleccion):
    with open(rutaFich, 'w') as f:
        json.dump(coleccion, f, indent=2)

def leerJSONClub(rutaFich):
    with open(rutaFich, 'r') as f:
        cadjson=json.load(f)

    listaAux=list()
    club=Club(cadjson["_nombreClub"], cadjson["_cif"], cadjson["_sede"])
    for j in cadjson["_listaSocios"]:
        socio=Socio(Usuario(j["_usuario"]["_dni"],j["_usuario"]["_contrasenna"],j["_usuario"]["_es_admin"]), j["_nombreCompleto"], j["_direccion"], j["_telefono"], j["_mail"])
        socio.getUsuario().setUltimoAcceso(j["_usuario"]["_ultimoAcceso"])
        listaAux.append(socio)
    club.setListaSocios(listaAux)
    return club