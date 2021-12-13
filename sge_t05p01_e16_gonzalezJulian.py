num = int(input('Introduzca un número: '))
suma = 0

while(num<1):
    print ("El numero introducido debe ser mayor o igual a 1")
    num = int(input('Introduzca un número: '))

try:
    for i in range(num):
        suma += (num**2)/(i+1)
except ZeroDivisionError:
    print("Division entre cero")

print ("El resultado es = ", suma)