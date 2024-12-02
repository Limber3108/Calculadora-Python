while True:
    mensaje= int(input("""Hola esto es una calculadora selecciona algunas de estas 4 opciones:
                    1: Sumar
                    2: Restar
                    3: Multiplicar
                    4: Dividir
                    5: Salir
Introduce el numero indicado:\n """))
    if mensaje >= 1 and mensaje <= 4:
        num1 = float(input("Introduce el primer numero: "))
        num2 = float(input("Introduce el segundo numero: "))
        if mensaje == 1:
            suma = num1 + num2
            print("la suma de tu operacion es: ", round(suma))
        elif mensaje == 2:
            resta= num1 - num2
            print("la resta de tu operacion es: ", round(resta))
        elif mensaje == 3:
            multiplicar= num1 * num2
            print("La multiplicacion de tu operacion es: ",round(multiplicar))
        elif mensaje == 4:
            division = num1 / num2
            print("la division de tu operacion es: ", round(division))
    elif mensaje == 5:
        print("Nos vemos pronto")
        break
    else:
        print("No funciona esta operacion")