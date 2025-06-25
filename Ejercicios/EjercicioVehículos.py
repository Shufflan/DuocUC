#Desarrolle un programa en Python que permita gestionar un registro de vehículos
#mediante un menú interactivo. El menú principal debe ofrecer las siguientes opciones:

# 1.- Ingresar vehículos
# 2.- Buscar vehículos
# 3.- Eliminar vehículos
# 4.- Mostrar vehículos
# 5.- Salir

# Funcionalidad de cada opción: 1. Ingresar vehículo
# El usuario debe ingresar los siguientes datos de forma individual:
# • Patente del vehículo
# • Tipo de vehículo (Auto, Moto o Camión)
# • Año de fabricación
# Para que el ingreso del vehículo se debe validar que:
# La patente debe estar compuesta de 4 letras seguida de 2 dígitos y no debe estar registrada previamente.
# El tipo debe ser exactamente uno de los siguientes: "Auto", "Moto" o "Camión".
# El año de fabricación debe estar entre 2007 y el año actual.
# Si todas las validaciones se cumplen, el vehículo se registra exitosamente.

# 2. Buscar vehículo
# Permite al usuario buscar un vehículo ingresando su patente. Si el vehículo existe en el
# registro, se deben mostrar sus datos: tipo y año de fabricación. En caso contrario, se debe informar que el vehículo no se encuentra.

# 3. Eliminar vehículo
# Permite eliminar un vehículo ingresando su patente. Si la patente existe, se elimina el registro y se muestra el mensaje: "¡Vehículo eliminado!". Si no se encuentra, se debe mostrar: "No se pudo eliminar el vehículo."

# 4. Mostrar Vehículos
# Despliega todos los vehículos registrados con sus correspondientes datos.

# 5. Salir

# Finaliza la ejecución del programa, desplegando la cantidad total de vehículos en el registro
# Si el usuario ingresa una opción no válida, el programa debe informar que se debe seleccionar una opción correcta.
# Todas las opciones del menú deben estar implementadas mediante funciones separadas, llamadas desde el programa principal (main). También, pueden generarse otras funciones que contribuyan a la modularidad de la aplicación.

vehiculos = []

def ingresar_veh():
    while True:
        patente = input("Ingrese la patente del vehículo: ")
        letras = patente[:4]
        digitos = patente[4:]
        if (len(patente) == 6) and letras.isalpha() and digitos.isdigit():
            break
        else:
            print("Error, ingrese otra patente.")
    
    while True:
        tipo = input("Ingrese el tipo de auto (Auto, Moto, Camión): ").lower().replace("ó","o")
        if tipo == "auto" or tipo == "moto" or "camion":
            break
        else:
            print("El tipo de auto no existe")
    while True:
        anio = int(input("Ingrese el año de fabricación (2007 a 2025): "))
        if anio >= 2007 and anio <= 2025:
            break
        else:
            print("El año de fabricación no es válido.")
    
    nuevoAuto = {
        'patente':patente,
        'tipo':tipo,
        'anio':anio
    }
    
    vehiculos.append(nuevoAuto)
    print("¡Vehículo registrado exitosamente!")
    
def buscar_veh(patente):
    mostrarP = []
    for p in vehiculos:
        if patente == p['patente']:
            mostrarP.append(p)
    if mostrarP == []:
        print("El vehículo no está registrado")
    else:
        for i in mostrarP:
            print(f"Patente: {i['patente']}")
            print(f"Tipo: {i['tipo'].capitalize()}")
            print(f"Año: {i['anio']}")
            

def eliminar_veh(eliminar):
    verificar = []
    for a in vehiculos:
        if eliminar == a['patente']:
            verificar.append(eliminar)
            vehiculos.remove(a)
            print("¡Vehículo eliminado!")
            break
    if verificar == []:
        print("No se pudo eliminar el vehículo.")
    
            

def mostrar_veh():
    for v in vehiculos:
        print(f"Patente: {v['patente']}")
        print(f"Tipo: {v['tipo']}").capitalize()
        print(f"Año: {v['anio']}\n")


while True:
    print("\nMenú Vehículos")
    print("1.- Ingresar vehículos")
    print("2.- Buscar vehículos")
    print("3.- Eliminar vehículos")
    print("4.- Mostrar vehículos")
    print("5.- Salir")
    opcion = int(input("Ingrese la opción: "))
    
    match opcion:
        case 1:
            print("")
            ingresar_veh()
        case 2:
            buscarAuto = input("Ingrese la patente: ")
            print("")
            buscar_veh(buscarAuto)
        case 3:
            eliminarAuto = input("Ingrese la patente: ")
            print("")
            eliminar_veh(eliminarAuto)
        case 4:
            print("")
            mostrar_veh()
        case 5:
            print("Hasta luego!")
            break
        case _:
            print("Opción ingresada no es válida.")
    