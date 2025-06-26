usuarios = []

def ingresarUsuario():
    while True:
        nombre = input("Ingrese nombre de usuario: ").lower()
        if usuarios == []:
            break
        for u in usuarios:
            if nombre == u['usuario']:
                print("Usuario ya existe. Intente otro.")
                nombre = input("Ingrese nombre de usuario: ").lower()
            elif nombre != u['usuario']:
                break
            break
        break

    while True:
        sexo = input("Ingrese su sexo (M) ó (F): ").lower()
        if sexo == "f":
            sexo = "F"
            break
        elif sexo == "m":
            sexo = "M"
            break
        else:
            print("Debe ingresar M o F solamente. Intente de nuevo.")

    while True:
        contrasena = input("Ingrese contraseña: ")
        if len(contrasena) >= 8:
            if " " in contrasena:
                print("Contraseña no valida. Intente otra.")
            else:
                print("Contraseña valida.")
                break
    
    usuarioNuevo = {
        'usuario':nombre,
        'sexo':sexo,
        'contrasena':contrasena
    }

    usuarios.append(usuarioNuevo)
    print("Usuario ingresado con exito!!")

def buscarUsuario(nombre):
    temp = []
    for n in usuarios:
        if nombre == n['usuario']:
            temp.append(n)
    if temp == []:
        print("El usuario no se encuentra.")
    else:
        for i in temp:
            print(f"El sexo del usuario es:{i['sexo']} y la contraseña es: {i['contrasena']}")

def eliminarUsuario(nombre):
    verificar = []
    for c in usuarios:
        if nombre == c['usuario']:
            verificar.append(c)
            usuarios.remove(c)
    if verificar == []:
        print("No se pudo eliminar usuario!")
    else:
        print("Usuario eliminado!")

while True:
    try:
        print("\nMENU PRINCIPAL")
        print("1.- Ingresar usuario.")
        print("2.- Buscar usuario.")
        print("3.- Eliminar usuario.")
        print("4.- Salir.")
        opcion = int(input("Ingrese opción: "))

        match opcion:
            case 1:
                ingresarUsuario()
            case 2:
                nombre = input("Ingrese usuario a buscar: ").lower()
                buscarUsuario(nombre)
            case 3:
                nombre = input("Ingrese usuario a buscar: ").lower()
                eliminarUsuario(nombre)
            case 4:
                print("Programa terminado...")
                break
            case _:
                print("Debe ingresar una opción válida!!")
    except ValueError:
        print("Ingrese solo números enteros.")

