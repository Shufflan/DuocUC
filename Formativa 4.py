turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"]
}


def turistas_por_pais(pais):
    for turista in pais.values():
        if turista[1] == "Estados Unidos":
            estadosUnidos.append(turista[0])
        elif turista[1] == "Argentina":
            argentina.append(turista[0])
        elif turista[1] == "Mexico":
            mexico.append(turista[0])
        elif turista[1] == "Brasil":
            brasil.append(turista[0])

def turistas_por_mes(mes):
    total = len(turistas)
    contador = 0
    #Recorriendo los valores del diccionario con .values() //IMPORTANTE ESO
    for turista in turistas.values():
        #Acá accedemos directamente a la fecha que es la tercera posición, indice 2.
        fecha = turista[2]
        #Eliminamos los guiones, lo que deja la fecha en ["dd", "mm", "aaaa"] porque split busca el "-" y los separa desde ahí
        fecha_partes = fecha.split("-")
        #Accedemos al indice del mes, que sería la segunda posición, indice 1.
        mesBuscado = int(fecha_partes[1])
        #Si el mes que buscamos es igual al que existe, lo guardamos.
        if int(mes) == mesBuscado:
            contador += 1
    if total == 0:
        return 0
    porcentaje = (contador/total) * 100
    return porcentaje
        

def eliminar_turista():
    pass



while True:
    try:
        print("*** MENU PRINCIPAL ***")
        print("1.- Turistas por país.")
        print("2.- Turistas por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir")
        optUsuario = int(input("Ingrese la opción: "))

        match optUsuario:
            case 1:
                estadosUnidos = []
                argentina = []
                mexico = []
                brasil = []
                turistas_por_pais(turistas)
                try:
                    opcionUsuario = input("Ingrese país a buscar: ")
                    opcionUsuario = opcionUsuario.lower()
                    opcionUsuario = opcionUsuario.replace("é", "e")
                    opcionUsuario = opcionUsuario.replace(" ", "")
                    
                    match opcionUsuario:

                        case "mexico":
                            print(mexico)
                        case "argentina":
                            print(argentina)
                        case "brasil":
                            print(brasil)
                        case "estadosunidos":
                            print(estadosUnidos)
                        case _:
                            print("No hay turistas de ese país.")
                except ValueError:
                    print("Ingrese solo palabras o letras.")
            case 2:
                while True:
                    try:
                        opcionUsuario = int(input("Ingrese el mes a buscar: "))
                        porcentaje = turistas_por_mes(opcionUsuario)
                        if opcionUsuario <= 12 and opcionUsuario >= 1:
                            print(f"El número de turistas equivale al {int(porcentaje)}% del total")
                            break
                        else:
                            print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
                            continue
                    except ValueError:
                        print("Ingresa solo valores numéricos enteros.")
            case 3:
                pass
            case 4:
                print("Programa terminado...")
                break
            case _:
                print("Opción fuera de rango.")
    except ValueError:
        print("Ingrese solo números enteros.")






