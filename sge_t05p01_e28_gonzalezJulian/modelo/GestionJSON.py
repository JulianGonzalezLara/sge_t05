import json

def guardarJSON(rutaFich, coleccion):
    with open(rutaFich, 'w') as f:
        json.dump(coleccion, f, indent=2)

def leerJSON(rutaFich):
    with open(rutaFich, 'r') as f:
        cadjson=json.load(f)
    return cadjson