productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2], 
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
}


def stock_marca(marca):
    verificar  = []
    suma = 0

    for nombre in productos.items():
        if marca == nombre[1][0].lower():
            verificar.append(nombre[0])

    for v in stock.items():
        for i in range(len(verificar)):
            if verificar[i] == v[0]:
                suma += v[1][1]
                
        
    print(f"El stock es: {suma}")
            
def busqueda_precio(p_min, p_max):
    verificar = []
    marcas = []

    for n in stock.items():
        if p_min >= 0:
            if n[1][1] != 0:
                if n[1][0] <= p_max and n[1][0] >= p_min:
                    verificar.append(n[0])

    for v in verificar:
        for m in productos.items():
            if v == m[0]:
                marcas.append(f"{m[1][0]}--{m[0]}")
    if verificar == []:
        print("No hay notebooks en ese rango de precios.")
    else:
        marcas.sort()
        print(f"Los notebooks entre los precios consultas son: {marcas}")
                

def eliminar_producto(modelo):
    eliminar = []
    for m in productos.items():
        if modelo == m[0].lower():
            eliminar.append(m[0])

    if eliminar == []:
        return False
    else:
        for e in eliminar:
            for p in productos.items():
                if e == p[0]:
                    productos.pop(e)
                    stock.pop(e)
                    return True

while True:
    print("\n*** MENÚ PRINCIPAL ***")
    print("1.- Stock marca.")
    print("2.- Búsqueda por precio.")
    print("3.- Eliminar producto.")
    print("4.- Salir.")
    opc = int(input("Ingrese opción: "))

    match opc:
        case 1:
            option = input("Ingrese marca a consultar: ").lower()
            stock_marca(option)
        case 2:
            while True:
                try:
                    minimo = int(input("Ingrese el monto mínimo: "))
                    maximo = int(input("Ingrese el monto máximo: "))
                    busqueda_precio(minimo, maximo)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!\n")
                    continue
        case 3:
            while True:
                modelo = input("Ingrese el modelo a actualizar: ").lower()
                if eliminar_producto(modelo) == True:
                    print("Producto Eliminado!!")
                else:
                    print("El modelo no existe!!")
                
                while True:
                    desicion = input("Desea eliminar otro producto (s/n)?: ").lower()
                    if desicion == "si":
                        break
                    elif desicion == "no":
                        break
                    else:
                        print("Ingrese una desición válida.")
                if desicion == "si":
                    continue
                else:
                    break

        case 4:
            print("Programa finalizado.")
            break
        case _:
            print("Debe seleccionar una opción válida!!")