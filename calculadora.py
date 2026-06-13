num1 = int(input("Número 1: ")) 
num2 = int(input("Número 2: ")) 
while True:
    print("""
    Seleccione opción:
    1- Sumar 
    2- Restar
    3- Multiplicar
    4- Dividir 
    """)
    opcion = int(input("Elige una opción: "))     
    if opcion == 1:
        print(f"La suma es: {num1 + num2}")
        break  # Rompe el bucle porque la operación fue exitosa
    elif opcion == 2:
        print(f"La resta es: {num1 - num2}")
        break
    elif opcion == 3:
        print(f"La multiplicación es: {num1 * num2}")
        break
    elif opcion == 4:
        if num2 == 0:
            print("Error: No se puede dividir entre cero. Intenta con otra opción o reinicia.")
        else:
            print(f"La división es: {num1 / num2}")
            break
    else:
        print("Opción incorrecta. Por favor, elige un número del 1 al 4.")
