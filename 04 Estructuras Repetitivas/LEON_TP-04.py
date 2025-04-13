# Ejercicio 1: Imprimir números enteros del 0 al 100 en orden creciente
def ejercicio_1():
    for i in range(101):
        print(i)

# Ejercicio 2: Determinar la cantidad de dígitos de un número ingresado
def ejercicio_2():
    numero = int(input("Ingrese un número entero: "))
    cantidad_digitos = len(str(abs(numero)))  # Usamos abs() para ignorar el signo
    print(f"El número {numero} tiene {cantidad_digitos} dígitos.")

# Ejercicio 3: Sumar todos los números entre dos valores dados por el usuario, excluyendo los límites
def ejercicio_3():
    inicio = int(input("Ingrese el primer valor: "))
    fin = int(input("Ingrese el segundo valor: "))
    suma = sum(range(inicio + 1, fin))  # Sumamos desde inicio+1 hasta fin-1
    print(f"La suma de los números entre {inicio} y {fin} es: {suma}")

# Ejercicio 4: Sumar números en secuencia hasta que el usuario ingrese un 0
def ejercicio_4():
    total = 0
    while True:
        numero = int(input("Ingrese un número (0 para terminar): "))
        if numero == 0:
            break
        total += numero
    print(f"El total acumulado es: {total}")

# Ejercicio 5: Juego de adivinar un número aleatorio entre 0 y 9
import random

def ejercicio_5():
    numero_aleatorio = random.randint(0, 9)
    intentos = 0
    while True:
        intento = int(input("Adivina el número entre 0 y 9: "))
        intentos += 1
        if intento == numero_aleatorio:
            print(f"¡Acertaste! El número era {numero_aleatorio}. Intentos: {intentos}")
            break
        elif intento < numero_aleatorio:
            print("El número es mayor, intenta de nuevo.")
        else:
            print("El número es menor, intenta de nuevo.")

# Ejercicio 6: Imprimir números pares entre 0 y 100 en orden decreciente
def ejercicio_6():
    for i in range(100, -1, -2):  # Empezamos desde 100 y decrementamos de 2 en 2
        print(i)

# Ejercicio 7: Sumar todos los números entre 0 y un número dado por el usuario
def ejercicio_7():
    numero = int(input("Ingrese un número entero positivo: "))
    suma = sum(range(numero + 1))  # Sumar desde 0 hasta el número incluido
    print(f"La suma de los números de 0 a {numero} es: {suma}")

# Ejercicio 8: Contar pares, impares, negativos y positivos de 100 números
def ejercicio_8():
    pares, impares, negativos, positivos = 0, 0, 0, 0
    for _ in range(100):  # Podemos cambiar el rango a un número menor para probar
        numero = int(input("Ingrese un número entero: "))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        if numero < 0:
            negativos += 1
        elif numero > 0:
            positivos += 1
    print(f"Pares: {pares}, Impares: {impares}, Negativos: {negativos}, Positivos: {positivos}")

# Ejercicio 9: Calcular la media de 100 números ingresados
def ejercicio_9():
    suma = 0
    for _ in range(100):  # Podemos cambiar el rango a un número menor para probar
        numero = int(input("Ingrese un número entero: "))
        suma += numero
    media = suma / 100
    print(f"La media de los números ingresados es: {media}")

# Ejercicio 10: Invertir el orden de los dígitos de un número
def ejercicio_10():
    numero = input("Ingrese un número: ")
    invertido = numero[::-1]  # Usamos slicing para invertir la cadena
    print(f"El número invertido es: {invertido}")

# Bloque para ejecutar funciones
if __name__ == "__main__":
    print("Ejercicios disponibles del 1 al 10")
    while True:
        ejercicio = input("Ingrese el número del ejercicio que desea probar: ")
        funciones = {
            '1': ejercicio_1,
            '2': ejercicio_2,
            '3': ejercicio_3,
            '4': ejercicio_4,
            '5': ejercicio_5,
            '6': ejercicio_6,
            '7': ejercicio_7,
            '8': ejercicio_8,
            '9': ejercicio_9,
            '10': ejercicio_10
        }

        if ejercicio in funciones:
            funciones[ejercicio]()  # Ejecuta la función correspondiente
        else:
            print("Número de ejercicio inválido.")
