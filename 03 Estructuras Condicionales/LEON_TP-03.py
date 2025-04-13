# ejercicios.py

import random
from statistics import mean, median, mode


# 1) Edad del usuario
def ejercicio_1():
    edad = int(input("Ingrese su edad: "))
    if edad > 18:
        print("Es mayor de edad")


# 2) Nota del usuario
def ejercicio_2():
    nota = float(input("Ingrese su nota: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")


# 3) Ingreso de número par
def ejercicio_3():
    numero = int(input("Ingrese un número par: "))
    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")


# 4) Categoría según edad
def ejercicio_4():
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        print("Niño/a")
    elif edad < 18:
        print("Adolescente")
    elif edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")


# 5) Validación de contraseña por longitud
def ejercicio_5():
    password = input("Ingrese una contraseña: ")
    if 8 <= len(password) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) Estadística: media, mediana, moda y sesgo
def ejercicio_6():
    numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
    m_mean = mean(numeros_aleatorios)
    m_median = median(numeros_aleatorios)
    m_mode = mode(numeros_aleatorios)

    print(f"Media: {m_mean}, Mediana: {m_median}, Moda: {m_mode}")
    if m_mean > m_median > m_mode:
        print("Sesgo positivo o a la derecha")
    elif m_mean < m_median < m_mode:
        print("Sesgo negativo o a la izquierda")
    elif m_mean == m_median == m_mode:
        print("Sin sesgo")
    else:
        print("No se puede determinar el sesgo claramente")


# 7) Añadir signo de exclamación si termina en vocal
def ejercicio_7():
    texto = input("Ingrese una frase o palabra: ")
    if texto[-1].lower() in 'aeiou':
        print(texto + "!")
    else:
        print(texto)


# 8) Transformación de nombre
def ejercicio_8():
    nombre = input("Ingrese su nombre: ")
    print("Opciones:\n1. Mayúsculas\n2. Minúsculas\n3. Capitalizado")
    opcion = input("Seleccione una opción (1, 2 o 3): ")
    if opcion == '1':
        print(nombre.upper())
    elif opcion == '2':
        print(nombre.lower())
    elif opcion == '3':
        print(nombre.title())
    else:
        print("Opción inválida")


# 9) Clasificación de terremoto
def ejercicio_9():
    magnitud = float(input("Ingrese la magnitud del terremoto: "))
    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif magnitud < 7:
        print("Muy fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")


# 10) Determinación de estación del año
def ejercicio_10():
    hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
    mes = int(input("Ingrese el mes (1-12): "))
    dia = int(input("Ingrese el día (1-31): "))

    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno" if hemisferio == 'N' else "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera" if hemisferio == 'N' else "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano" if hemisferio == 'N' else "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño" if hemisferio == 'N' else "Primavera"
    else:
        estacion = "Fecha inválida"

    print(f"Estación: {estacion}")


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
            funciones[ejercicio]()
        else:
            print("Número de ejercicio inválido.")