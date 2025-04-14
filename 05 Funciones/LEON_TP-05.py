import math


# Actividad 1: Función imprimir_hola_mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")


# Actividad 2: Función saludar_usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"


# Actividad 3: Función informacion_personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# Actividad 4: Funciones calcular_area_circulo y calcular_perimetro_circulo
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


# Actividad 5: Función segundos_a_horas
def segundos_a_horas(segundos):
    return segundos / 3600


# Actividad 6: Función tabla_multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# Actividad 7: Función operaciones_basicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Error: División por cero"
    return suma, resta, multiplicacion, division


# Actividad 8: Función calcular_imc
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


# Actividad 9: Función celsius_a_fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Actividad 10: Función calcular_promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# Función principal
if __name__ == "__main__":
    # Actividad 1
    imprimir_hola_mundo()

    # Actividad 2
    nombre_usuario = input("Ingresa tu nombre: ")
    print(saludar_usuario(nombre_usuario))

    # Actividad 3
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    residencia = input("Ingresa tu residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    # Actividad 4
    radio = float(input("Ingresa el radio del círculo: "))
    print(f"Área del círculo: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio):.2f}")

    # Actividad 5
    segundos = int(input("Ingresa la cantidad de segundos: "))
    print(f"Cantidad de horas: {segundos_a_horas(segundos):.2f}")

    # Actividad 6
    numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

    # Actividad 7
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    suma, resta, multiplicacion, division = operaciones_basicas(a, b)
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

    # Actividad 8
    peso = float(input("Ingresa tu peso (kg): "))
    altura = float(input("Ingresa tu altura (m): "))
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")

    # Actividad 9
    celsius = float(input("Ingresa la temperatura en Celsius: "))
    print(f"La temperatura en Fahrenheit es: {celsius_a_fahrenheit(celsius):.2f}")

    # Actividad 10
    a = float(input("Ingresa el primer número para el promedio: "))
    b = float(input("Ingresa el segundo número para el promedio: "))
    c = float(input("Ingresa el tercer número para el promedio: "))
    print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")
