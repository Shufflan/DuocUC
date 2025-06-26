mascotas = []

def datos():
    while True:
        nombre = input("Ingrese el nombre de la mascota: ").lower()
        if nombre.isalpha():
            break
        else:
            print("El nombre solo puede contener letras.")
    while True:
        print("Tipo de mascota\nP: Perro\nG: para Gato\nA: para ave")
        tipo = input("Ingresa el tipo de mascota: ").lower()
        if tipo == "p":
            tipo = "Perro"
            break
        elif tipo == "g":
            tipo = "Gato"
            break
        elif tipo == "a":
            tipo = "Ave"
            break
        else:
            print("")
            print("Tipo de mascota no válida.")
            print("")
            
    while True:
        fecha = input("Ingresa la fecha de registro (DD-MM-AAAA): ")
        if len(fecha) == 8:
            dias = int(fecha[:2])
            mes = int(fecha[2:4])
            anio = int(fecha[4:])
        else:
            print("La fecha es demasiado corta")
            continue
        
        if dias <= 31 and dias >= 1:
            if mes <= 12 and mes >= 1:
                if anio <= 2025 and anio >= 2000:
                    fecha = f'{dias}-{mes}-{anio}'
                    break
        else:
            print("La fecha no existe.")
    while True:
        edad = int(input("Ingresa la edad de la mascota: "))
        if edad > 0 and edad <= 25:
            break
        else:
            print("La edad ingresada no existe.")
        
    animal = {
        'nombre':nombre,
        'tipo': tipo,
        'fecha':fecha,
        'edad':edad  
    }
    
    mascotas.append(animal)

def buscarMascota(nombreAnimal):
    datos = []
    for a in mascotas:
        if nombreAnimal == a['nombre']:
            datos.append(a)
    if datos == []:
        print("La mascota no se encuentra")
    else:
        for d in datos:
            print(f"Tipo: {d['tipo']}")
            print(f"Fecha de Registro: {d['fecha']}")
            print(f"Edad: {d['edad']}")

def eliminarMascota(nombreAnimal):
    verificar = []
    for a in mascotas:
        if nombreAnimal == a['nombre']:
            verificar.append(a)
            mascotas.remove(a)
    if verificar == []:
        print("No se pudo eliminar la mascota.")
    else:
        print("¡Mascota Eliminada!")
    
def mostrarMascotas(anio):
    anios = []
    for a in mascotas:
        if str(anio) == a['fecha'][-5:].replace("-",""):
            anios.append(a)
    if anios == []:
        print("No hay mascotas registradas en ese año")
    else:
        for f in anios:
            print(f"\n{f['nombre'].capitalize()}")
            print(f"Tipo: {f['tipo']}")
            print(f"Fecha: {f['fecha']}")
            print(f"Edad: {f['edad']}")
            

    
    
while True:
    try:
        print("\nMascotas Pachi")
        print("1.- Ingresar mascota")
        print("2.- Buscar mascota")
        print("3.- Eliminar mascota")
        print("4.- Mostrar mascotas registradas en un año específico")
        print("5.- Salir")
        opcion = int(input("Ingrese una opción: "))
        
        match opcion:
            case 1:
                datos()
            case 2:
                nombre = input("Ingresa el nombre de su mascota: ").lower()
                buscarMascota(nombre)
            case 3:
                nombre = input("Ingresa el nombre de su mascota: ").lower()
                eliminarMascota(nombre)
            case 4:
                while True:
                    anios = int(input("Ingresa el año a buscar: "))
                    if anios >= 2000 and anios <= 2025:
                        mostrarMascotas(anios)
                        break
                    else:
                        print("Error, el año debe ser entre 2000 y 2025")
            case 5:
                print("Gracias por su preferencia")
                print(f"Se registraron {len(mascotas)} mascotas")
                break
            case _:
                print("No es una opción válido.")
    except ValueError:
        print("Ingresa solo números enteros.")