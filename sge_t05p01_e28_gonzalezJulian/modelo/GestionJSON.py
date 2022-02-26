import json
from modelo.Club import Club
from modelo.Familia import Familia
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

        familia = Familia()
        if j["_familia"]["_pareja"] != None:
            familia.setPareja(Socio(Usuario(j["_familia"]["_pareja"]["_dni"], j["_familia"]["_pareja"]["_contrasenna"], j["_familia"]["_pareja"]["_es_admin"]),None,None,None,None))
        
        if j["_familia"]["_hijos"] != None:
            for i in j["_familia"]["_hijos"]:
                familia.addHijo(Socio(Usuario(i["_dni"], i["_contrasenna"], i["_es_admin"]), None,None,None,None))

        socio.setFamilia(familia)
        listaAux.append(socio)
    club.setListaSocios(listaAux)
    return club