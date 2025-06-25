# Nombre del LOCAL = Pasushi. En honor a mi gato.

# Iniciamos las variables que utilizaremos luego en el programa
pikachuRoll = 4500
otakuRoll = 5000
pulpoVRoll = 5200
anguilaERoll = 4800
sumaTotal = 0
contadorPR = 0
contadorOR = 0
contadorPVR = 0
contadorAER = 0
contadorTotal = 0


# Iniciamos el programa con un While para saber si el usuario quiere ver la carta
# Si el usuario selecciona Sí (s). Comenzamos el ciclo.
while True:
    
    # Usamos un Try Except dentro del Ciclo para controlar que el usuario no ingrese
    # Algún valor que no se el que se le pide, en este caso, se le pide un valor como
    # String, no valores numéricos.
    try:
        print("+----------------------------------+")
        print("|      Bienvenido a PASUSHI        |")
        print("+----------------------------------+")
        print("|      ¿Desea ver la carta?        |")
        print("|                                  |")
        print("| Sí (s)                    No (n) |")
        print("+----------------------------------+")
        desicion = input("Ingrese la opción: ").lower()
        
        # Acá iniciamos el IF, al ser dos opciones, no quise usar un match. Si el usuario ingresa "s" podemos pasar
        # a imprimirle la carta y dejar que decida lo que quiera llevar.
        if desicion == "s":
            while True:
                
                # Nuevamente ingresamos un try except para controlar que ingrese solamente valores numéricos
                try:
                    print("\n+----------------------------------------+")
                    print("| Seleccione los rolls que desea agregar |")
                    print("| Luego seleccione salir.                |")
                    print("|                                        |")
                    print("| 1.- Pikachu Roll $4500                 |")
                    print("| 2.- Otaku Roll $5000                   |")
                    print("| 3.- Pulpo Venenoso Roll $5200          |")
                    print("| 4.- Anguila Eléctrica Roll $4800       |")
                    print("| 5.- Salir                              |")
                    print("+-----------------------------------------+")
                    opcion = int(input("Ingrese la opción: "))
                    
                    # Creo un match para controlar este menú porque son más opciones.
                    # Cree el mismo tipo de mensaje para cada vez que se repita el ciclo
                    # Así el usuario podrá saber cuanta cantidad de cada una lleva hasta el momento.
                    # Hago que se agrege uno al contador individual de cada sushi y además uno al total de todos.
                    # Al ingresar salimos de este menú y pasamos al siguiente.
                    match opcion:
                        case 1:
                            sumaTotal += pikachuRoll
                            contadorPR += 1
                            contadorTotal += 1
                            print( "\n+-------------------------------------------------+")
                            print(f"| Cantidad de Pikachu Roll = {contadorPR}                    |")
                            print(f"| Cantidad de Otaku Roll = {contadorOR}                      |")
                            print(f"| Cantidad de Pulpo Venenoso Roll = {contadorPVR}             |")
                            print(f"| Cantidad de Anguila Venenoso Roll = {contadorAER}           |")
                            print( "+-------------------------------------------------+")
                            continue
                        case 2:
                            sumaTotal += otakuRoll
                            contadorOR += 1
                            contadorTotal += 1
                            print( "\n+-------------------------------------------------+")
                            print(f"| Cantidad de Pikachu Roll = {contadorPR}                    |")
                            print(f"| Cantidad de Otaku Roll = {contadorOR}                      |")
                            print(f"| Cantidad de Pulpo Venenoso Roll = {contadorPVR}             |")
                            print(f"| Cantidad de Anguila Venenoso Roll = {contadorAER}           |")
                            print( "+-------------------------------------------------+")
                            continue
                        case 3:
                            sumaTotal += pulpoVRoll
                            contadorPVR += 1
                            contadorTotal += 1
                            print( "\n+-------------------------------------------------+")
                            print(f"| Cantidad de Pikachu Roll = {contadorPR}                    |")
                            print(f"| Cantidad de Otaku Roll = {contadorOR}                      |")
                            print(f"| Cantidad de Pulpo Venenoso Roll = {contadorPVR}             |")
                            print(f"| Cantidad de Anguila Venenoso Roll = {contadorAER}           |")
                            print( "+-------------------------------------------------+")
                            continue
                        case 4:
                            sumaTotal += anguilaERoll
                            contadorAER += 1
                            contadorTotal += 1
                            print( "\n+-------------------------------------------------+")
                            print(f"| Cantidad de Pikachu Roll = {contadorPR}                    |")
                            print(f"| Cantidad de Otaku Roll = {contadorOR}                      |")
                            print(f"| Cantidad de Pulpo Venenoso Roll = {contadorPVR}             |")
                            print(f"| Cantidad de Anguila Venenoso Roll = {contadorAER}           |")
                            print( "+-------------------------------------------------+")
                            continue
                        case 5:
                            break
                        case _:
                            print("La opción ingresada no es válida.")
                            continue
                except ValueError:
                    print("Ingresa solo valores numéricos.")
                
            while True:
                # Nuevamente otro Try except para verificar que solo ingrese S o N.
                try: 
                    print("\n+-----------------------------+")
                    print("| ¿Posee código de descuento? |")
                    print("+-----------------------------+")
                    print("| Sí (s)               No (n) |")
                    print("+-----------------------------+")
                    eleccion = input("Ingrese la opción: ").lower()
                    
                    # Si el usuario elije la opción que posee descuento
                    # Creamos una condición donde se verifique si efectivamente tiene uno y pueda ingresarlo
                    # Si el código no es "soyotaku" se le mostrará un mensaje preguntando si desea reintentarlo o volver al menú.
                    # acá hay un doble "break" porque si decide volver al menú, saltamos directo a la impresión del total.
                    if eleccion == "s":   
                        while True:
                            # Este try except es para verificar que solo use valores como string y no numéricos.
                            try:
                                codigo = input("Ingrese el código de descuento: ")
                                if codigo == "soyotaku":
                                    codigoDescuento = 0.10
                                    print("Código válido")
                                    break
                                else:
                                    print("\n+------------------------------+")
                                    print("| ¿Desea reingresar el código? |")
                                    print("+------------------------------+")
                                    print("| Sí (s)                No (x) |")
                                    print("+------------------------------+")
                                    opcionCodigo = input("Ingrese la opción: ")
                                    if opcionCodigo == "s":
                                        continue
                                    elif opcionCodigo == "x":
                                        break
                                    else:
                                        print("Opción no válida.")
                                        break
                            except ValueError:
                                print("Ingrese solo letras.")
                        break                            
                    elif eleccion == "n":
                        codigoDescuento = 0
                        break
                    else:
                        print("Opción ingresada no es válida.")    
                except ValueError:
                    print("Ingrese solo letras.")
            
            # Por último, imprimimos todo el total para que el usuario pueda verlo
            print("\n******************************")
            print(f"TOTAL PRODUCTOS: {contadorTotal}")
            print(f"Pikachu Roll: {contadorPR}")
            print(f"Otaku Roll: {contadorOR}")
            print(f"Pulpo Venenoso Roll: {contadorPVR}")
            print(f"Anguila Eléctrica Roll: {contadorAER}")
            print("******************************")
            print(f"Subtotal por pagar: {sumaTotal}")
            print(f"Descuento por código: {sumaTotal * codigoDescuento}")
            print(f"TOTAL = {sumaTotal - (sumaTotal * codigoDescuento)}")
            
            
            # Luego de la impresión del pedido, le consultamos al usuario si necesita realizar otro.
            # Usamos otro try para controlar que no se usen números.
            # Si el usuario desea hacer otro pedido, reiniciamos los valores de las variables, para crear otro desde 0.
            # De lo contrario se acaba el programa.
            while True:
                try:
                    print("\n+------------------------------+")
                    print("| ¿Desea realizar otro pedido? |")
                    print("+------------------------------+")
                    print("| Sí (s)                No (n) |")
                    print("+------------------------------+")
                    terminar = input("Ingrese la opción: ")

                    if terminar == "s":
                        sumaTotal = 0
                        contadorPR = 0
                        contadorOR = 0
                        contadorPVR = 0
                        contadorAER = 0
                        contadorTotal = 0
                        continue
                    
                    elif terminar == "n":
                        break
                    else:
                        print("Gracias por su preferencia.")
                        continue
                except ValueError:
                    print("Ingresa solo letras.")
            # Acá si el usuario no quiere seguir comprando, se termina el ciclo con break, y se termina.
            print("\n+------------------------------+")
            print("| Gracias por preferir Pasushi |")
            print("+------------------------------+")
            break
        elif desicion == "n":
            print("Gracias por su preferencia")
            break
        else:
            print("Opción ingresada no es válida")
    except ValueError:
        print("Ingrese solo letras.")
