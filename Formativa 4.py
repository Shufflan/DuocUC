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

estadosUnidos = []
argentina = []
mexico = []
brasil = []

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
    print(f"Turistas de Estados Unidos: {estadosUnidos}")
    print(f"Turistas de Argentina: {argentina}")
    print(f"Turistas de México: {mexico}")
    print(f"Turistas de Brasil: {brasil}")

def turistas_por_mes(mes):
    pass

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
                turistas_por_pais(turistas)
            case 2:
                pass
            case 3:
                pass
            case 4:
                print("Programa terminado...")
                break
            case _:
                print("Opción fuera de rango.")
    except ValueError:
        print("Ingrese solo números enteros.")






