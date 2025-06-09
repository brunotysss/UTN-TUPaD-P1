
# Práctico 2: Funciones en Python

# 1. Función imprimir_hola_mundo
# Enunciado: Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”.
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Función saludar_usuario(nombre)
# Enunciado: Recibe como parámetro un nombre y devuelve un saludo personalizado.
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Función informacion_personal(nombre, apellido, edad, residencia)
# Enunciado: Imprime “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Funciones calcular_area_circulo y calcular_perimetro_circulo
# Enunciado: Devuelven el área y el perímetro de un círculo, respectivamente.
import math
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Función segundos_a_horas
# Enunciado: Recibe segundos y devuelve la cantidad de horas.
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Función tabla_multiplicar(numero)
# Enunciado: Imprime la tabla de multiplicar del 1 al 10 del número recibido.
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Función operaciones_basicas(a, b)
# Enunciado: Devuelve una tupla con suma, resta, multiplicación y división de dos números.
def operaciones_basicas(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else 'Indefinido'

# 8. Función calcular_imc(peso, altura)
# Enunciado: Devuelve el índice de masa corporal (IMC) con dos decimales.
def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

# 9. Función celsius_a_fahrenheit(celsius)
# Enunciado: Convierte una temperatura de Celsius a Fahrenheit.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Función calcular_promedio(a, b, c)
# Enunciado: Devuelve el promedio de tres números.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# Programa principal de prueba
if __name__ == "__main__":
    imprimir_hola_mundo()

    nombre = input("Ingresa tu nombre: ")
    print(saludar_usuario(nombre))

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    radio = float(input("Radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

    segundos = int(input("Segundos: "))
    print(f"Horas: {segundos_a_horas(segundos):.2f}")

    numero_tabla = int(input("Número para tabla de multiplicar: "))
    tabla_multiplicar(numero_tabla)

    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    suma, resta, mult, div = operaciones_basicas(a, b)
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")

    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en metros: "))
    print(f"IMC: {calcular_imc(peso, altura)}")

    celsius = float(input("Temperatura en Celsius: "))
    print(f"Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")

    a = float(input("Primer número para promedio: "))
    b = float(input("Segundo número: "))
    c = float(input("Tercer número: "))
    print(f"Promedio: {calcular_promedio(a, b, c):.2f}")