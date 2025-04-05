#Fernandez Paolini,Carlos Bruno - Comision 25

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.")
print("Hola Mundo!")

'''
2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.
'''
print("Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.”.")

nombre = input("¿Cuál es tu nombre? ")

print(f"Hola {nombre}!")

'''
3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
'''
nombre = str(input("¿Cuál es tu nombre? "))
apellido = str(input("¿Cuál es tu apellido? "))
edad = int(input("¿Cuál es tu edad? "))
residencia  = str(input("¿Cuál es tu residencia? "))

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

'''
4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.
'''
pi = 3.1416  # Valor aproximado de pi

radio = float(input("Ingrese el radio del círculo: "))

area = pi * radio ** 2
perimetro = 2 * pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

'''
5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.
'''
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = float(segundos/3600)
print(f"Equivale a {horas:.2f} horas.")

'''
6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.
'''

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")


'''
7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
'''
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2  # Python hace división flotante

print(f"\nSuma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division:.2f}")
'''
8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:
𝐼𝑀𝐶 =
𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)
2
'''

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print(f"\nSu Índice de Masa Corporal (IMC) es: {imc:.2f}")

'''
9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =
9
5
. 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
'''
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = (9 / 5) * celsius + 32

print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")

'''
10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.

'''

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los tres números es: {promedio:.2f}")