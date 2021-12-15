import string

dicc_pal = {}
dicc_let = {}
cadena = input('Introduzca una cadena: ')
cadenaMinuscula = cadena.lower()
listaPalabras = cadenaMinuscula.split()

for w in listaPalabras:
    #print(listaPalabras.count(w))
    #print(listaPalabras[listaPalabras.index(w)])
    dicc_pal[listaPalabras[listaPalabras.index(w)]] = listaPalabras.count(w)

print(dicc_pal)

for w in list(string.ascii_lowercase):
    dicc_let[w] = cadenaMinuscula.count(w)

dicc_let["noLetra"] = cadenaMinuscula.count(" ")

print(dicc_let)

