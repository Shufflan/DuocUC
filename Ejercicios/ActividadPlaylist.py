# ========================
# ACTIVIDAD 2 = GESTOR DE PLAYLIST MUSICAL
# ========================

# Crea un programa que permita administrar una "LISTA" de canciones.
# Cada canción debe ser representada mediante un "DICCIONARIO" que contenga:
# - 'titulo' {str}: Nombre de la canción
# - 'artista' {str}: Nombre del artista o banda
# - 'genero' {str}: género músical (pop, rock, reggaeton, etc)
# - 'duración' {float}: duración en minutos.

# CREAR AQUÍ LA LISTA DE CANCIONES

playlist = [
    {
    'titulo': "Cantata de Puentes Amarillos",
    'artista': "Pescado Rabioso",
    'genero': "Rock",
    'duracion': 9.07
    },
    {
    'titulo': "Lago en el Cielo",
    'artista': "Gustavo Cerati",        
    'genero': "Rock",
    'duracion': 5.08
    },
    {
    'titulo': "La Verdad",
    'artista': "Kidd Voodoo",
    'genero': "Trap",
    'duracion': 4.56
    },
    {
    'titulo': "Madrid",
    'artista': "Jairo Vera",
    'genero': "Trap",
    'duracion': 3.15
    },
    {
    'titulo': "El Otro Chile",
    'artista': "Portavoz",
    'genero': "Rap",
    'duracion': 3.57
    },
    {
    'titulo': "Negandonos",
    'artista': "Kidd Voodoo",
    'genero': "Trap",
    'duracion': 3.59
    },
    {
    'titulo': "Sigo pensando",
    'artista': "Kidd Voodoo",
    'genero': "Trap",
    'duracion': 3.33
    },
    {
    'titulo': "Bajan",
    'artista': "Pescado Rabioso",
    'genero': "Rock",
    'duracion': 3.24
    }
]

# ==================================
# Función 1: Ver todas las canciones
# ==================================

def ver_canciones():
    for c in playlist:
        print(f"{c['titulo']} || {c['artista']} || {c['genero']} || {c['duracion']}")

# ==================================
# Función 2: Buscar canciones por artista
# ==================================

def buscar_por_artista(nombre):
    mostrarArtistas = []
    for c in playlist:
        if nombre == c['artista'].lower().replace(" ",""):
            mostrarArtistas.append(c)
    if mostrarArtistas == []:
        print("No existe el artista dentro de la playlist.")
    else:
        print("Canciones encontradas: ")
        for t in mostrarArtistas:
            print(f"{t['titulo']} || {t['artista']} || {t['genero']} || {t['duracion']}")

# ==================================
# Función 3: Agregar una nueva canción
# ==================================

def agregar_cancion(titulo, artista, genero, duracion):
    nuevaCancion = {
        'titulo': titulo,
        'artista': artista,
        'genero': genero,
        'duracion': duracion
    } 
    
    playlist.append(nuevaCancion)
    print("Cancion agregada satisfactoriamente.")

# ==================================
# Función 4: Ver canciones por género
# ==================================

def ver_por_genero(genero):
    generoCancion = []
    for g in playlist:
        if genero == g['genero']:
            generoCancion.append(g)
    if generoCancion == []:
        print("No existe ese género en la playlist.")
    else:
        for gen in generoCancion:
            print(f"{gen['titulo']} || {gen['artista']} || {gen['genero']} || {gen['duracion']}")
            

# ==================================
# Bucle principal del menú
# ==================================

while True:
    try:
        print("\nMenú Playlist Personal")
        print("1.- Ver todas las canciones")
        print("2.- Buscar canciones por artista")
        print("3.- Agregar una nueva canción")
        print("4.- Ver canciones por género")
        print("5.- Salir")
        opcion = int(input("Ingrese la opción: "))
        
        match opcion:
            case 1:
                print("")
                ver_canciones()
            case 2:
                    artista = input("Ingrese el nombre del artista: ").lower().replace(" ","")
                    print("")
                    buscar_por_artista(artista)
            case 3:
                titulo = input("Nombre de la canción: ")
                artista = input("Nombre del artista: ")
                genero = input("Genero de la canción: ")
                duracion = float(input("Duración de la canción: "))
                agregar_cancion(titulo, artista, genero, duracion)
            case 4:
                genero = input("Ingresa el genero: ")
                ver_por_genero(genero)
            case 5:
                print("Gracias por su preferencia.")
                break
            case _:
                print("Ingrese solo valores válidos.")
    except ValueError:
        print(f"Ingrese solo números enteros.")