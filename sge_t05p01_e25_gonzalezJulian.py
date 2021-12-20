import math
from typing import final

class punto:
    def __init__(this, x=0, y=0):
        this.x = x
        this.y = y

    def __str__(this) -> str:
        return "("+str(this.x)+","+str(this.y)+")"

    def cuadrante(this):
        if(this.x == 0 and this.y != 0):
            return ("Se encuentra sobre el eje Y")
        elif(this.x != 0 and this.y == 0):
            return ("Se encuentra sobre el eje X")
        elif(this.x == 0 and this.y == 0):
            return ("Se encuentra sobre el origen")
        elif(this.x > 0 and this.y > 0):
            return ("Se encuentra en el cuadrante 1")
        elif(this.x < 0 and this.y > 0):
            return ("Se encuentra en el cuadrante 2")
        elif(this.x < 0 and this.y < 0):
            return ("Se encuentra en el cuadrante 3")
        elif(this.x > 0 and this.y < 0):
            return ("Se encuentra en el cuadrante 4")

    def vector(this,punto2):
        #"("+str(punto.x - this.x)+","+str(punto.y - this.y)+")"
        return (punto((punto2.x - this.x),(punto2.y - this.y)))

    def distancia(this,punto):
        return (math.sqrt((punto.x-this.x)**2 + (punto.y - this.y)**2))

class rectangulo:
    def __init__(this, inicial=punto(0,0), final=punto(5,5)):
        this.inicial = inicial
        this.final = final
    
    def es_rectangulo(this):
        esRectangulo = False
        vector=this.inicial.vector(this.final)
        if(vector.x != vector.y):
            esRectangulo=True
        return (esRectangulo)
    
    def base(this):
        return (this.inicial.vector(this.final).x)
    
    def altura(this):
        return (this.inicial.vector(this.final).y)
    
    def area(this):
        base = this.base()
        altura = this.altura()
        return (base*altura)


opcion = 0
opcionSubMenu = 'd'

x = input("Introduzca la x del primer punto")
y = input("Introduzca la y del primer punto")
x2 = input("Introduzca la x del segundo punto")
y2 = input("Introduzca la y del segundo punto")
punto1 = punto(x,y)
punto2 = punto(x2,y2)

while opcion != '3':
    print("---------------------Menú de opciones---------------------")
    print("(1) Operaciones con puntos. Muestra el siguiente submenú:")
    print("(a) Mostrar cuadrante al que pertenecen.")
    print("(b) Calcular Vector")
    print("(c) Calcular Distancia")
    print("(2) Operaciones con rectángulos. Muestra el siguiente submenú:")
    print("(a) Calcular Base")
    print("(b) Calcular Altura")
    print("(c) Calcular Area")
    print("(3) Salir")
    print("---------------------------------------------------------")
    opcion = input('Elige una opción:')

    #while opcionSubMenu == 'a' or opcionSubMenu == 'b' or opcionSubMenu == 'c'

    p1 = punto(5,2)
    p2 = punto(2,3)
    r1 = rectangulo(p1,p2)
    print(p1)
    print(p1.cuadrante())
    print(p1.vector(p2))
    print("La distancia es ",p1.distancia(p2))
    print(r1.es_rectangulo())
    print(r1.base())
    print(r1.altura())
    print(r1.area())