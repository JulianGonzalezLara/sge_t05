clientes = {}
opcion = 0

while opcion != '6':

    if opcion == '1':
        nif = input('Introduce el nif del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        apellidos = input('Introduce los apellidos del cliente: ')
        direccion = input('Introduce la direccion del cliente: ')
        telefono = input('Introduce el telefono del cliente: ')
        correo = input('Introduce el correo electronico del cliente: ')
        preferente = input('¿Es un cliente preferente (S/N)? ')
        if(preferente.lower() == "s"):
            cliente = {'nombre':nombre, 'apellidos':apellidos, 'direccion':direccion, 'telefono':telefono, 'correo':correo, 'preferente':'true'}
        else:
            cliente = {'nombre':nombre, 'apellidos':apellidos, 'direccion':direccion, 'telefono':telefono, 'correo':correo, 'preferente':'false'}
        clientes[nif] = cliente

    if opcion == '2':
        nif = input('Introduce nif del cliente: ')
        if nif in clientes:
            del clientes[nif]
        else:
            print('No existe el cliente con el nif', nif)

    if opcion == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            print('NIF:', nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el cliente con el nif', nif)

    if opcion == '4':
        print('Lista de clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])

    if opcion == '5':
        print('Lista de clientes preferentes')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])

    
    print("----------Menú de opciones----------")
    print("(1) Añadir cliente")
    print("(2) Eliminar Cliente")
    print("(3) Mostrar Cliente")
    print("(4) Listar Clientes")
    print("(5) Listar clientes preferentes")
    print("(6) Terminar")
    print("------------------------------------")
    opcion = input('Elige una opción:')