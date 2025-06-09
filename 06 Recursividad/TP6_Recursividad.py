
# Práctico 11 - Recursividad
# Autor: ChatGPT - TP Resuelto con comentarios

# 1) Calcular factorial de un número de forma recursiva
def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Paso recursivo
    return n * factorial(n - 1)

# Ejemplo: Mostrar los factoriales desde 1 hasta n
def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")

# 2) Serie de Fibonacci hasta una posición dada
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)

def mostrar_fibonacci(hasta):
    serie = [fibonacci(i) for i in range(hasta + 1)]
    print("Serie de Fibonacci:", serie)

# 3) Calcular potencia usando recursividad
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# 4) Convertir número decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

# 5) Comprobar si una palabra es palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6) Sumar los dígitos de un número sin convertirlo en string
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

# 7) Contar bloques para construir pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# 8) Contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    contador = 1 if numero % 10 == digito else 0
    return contador + contar_digito(numero // 10, digito)
