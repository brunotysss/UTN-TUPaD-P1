#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Práctico 4: Estructuras repetitivas
Objetivo:
  Implementar ciclos para resolver problemas que requieran repetición de acciones.
"""

import random

while True:
    # Menú interactivo
    print("\n=== Práctico 4: Estructuras repetitivas ===")
    print("1) Ejercicio 1 – Imprimir números del 0 al 100")
    print("2) Ejercicio 2 – Contar dígitos de un entero")
    print("3) Ejercicio 3 – Sumar enteros entre dos valores (excluyendo extremos)")
    print("4) Ejercicio 4 – Sumar hasta ingresar 0")
    print("5) Ejercicio 5 – Juego: adivina un número (0–9)")
    print("6) Ejercicio 6 – Números pares de 100 a 0")
    print("7) Ejercicio 7 – Sumar de 0 a un entero positivo")
    print("8) Ejercicio 8 – Clasificar 100 números")
    print("9) Ejercicio 9 – Media de 100 números")
    print("10) Ejercicio 10 – Invertir dígitos de un número")
    print("0) Salir")
    elec = input("→ ")

    if elec == '1':
        # Ejercicio 1: Imprimir los enteros de 0 a 100
        print("\nEjercicio 1:")
        for i in range(0, 101):
            print(i)

    elif elec == '2':
        # Ejercicio 2: Contar la cantidad de dígitos
        n = int(input("\nEjercicio 2 – Ingresa un entero: "))
        n_abs = abs(n)
        if n_abs == 0:
            count = 1
        else:
            count = 0
            while n_abs:
                n_abs //= 10
                count += 1
        print(f"El número {n} tiene {count} dígito(s).")

    elif elec == '3':
        # Ejercicio 3: Sumar enteros entre A y B (sin incluir A ni B)
        a = int(input("\nEjercicio 3 – Valor A: "))
        b = int(input("Ejercicio 3 – Valor B: "))
        inicio = min(a, b) + 1
        fin    = max(a, b)
        total = 0
        for i in range(inicio, fin):
            total += i
        print(f"La suma entre {a} y {b} (sin extremos) es: {total}")

    elif elec == '4':
        # Ejercicio 4: Sumar en secuencia hasta que el usuario ingrese 0
        print("\nEjercicio 4 – Ingresa números (0 para detener):")
        total = 0
        while True:
            n = int(input("  Número: "))
            if n == 0:
                break
            total += n
        print(f"Total acumulado: {total}")

    elif elec == '5':
        # Ejercicio 5: Adivinar un número aleatorio entre 0 y 9
        target = random.randint(0, 9)
        intentos = 0
        print("\nEjercicio 5 – Adivina el número (0–9):")
        while True:
            guess = int(input("  Tu intento: "))
            intentos += 1
            if guess == target:
                print(f"¡Correcto! Lo lograste en {intentos} intento(s).")
                break
            else:
                print("  Incorrecto, sigue intentando 😉")

    elif elec == '6':
        # Ejercicio 6: Imprimir pares de 100 a 0
        print("\nEjercicio 6:")
        for i in range(100, -1, -1):
            if i % 2 == 0:
                print(i)

    elif elec == '7':
        # Ejercicio 7: Sumar todos los números de 0 a N
        n = int(input("\nEjercicio 7 – Ingresa un entero positivo: "))
        total = 0
        for i in range(0, n + 1):
            total += i
        print(f"Suma de 0 a {n}: {total}")

    elif elec == '8':
        # Ejercicio 8: Clasificar 100 números en pares, impares, negativos y positivos
        print("\nEjercicio 8 – Ingresa 100 números:")
        pares = impares = negativos = positivos = 0
        for idx in range(1, 101):
            n = int(input(f"  Número {idx}/100: "))
            if n % 2 == 0:
                pares += 1
            else:
                impares += 1
            if n < 0:
                negativos += 1
            elif n > 0:
                positivos += 1
        print(f"\nResumen:")
        print(f"  Pares: {pares}")
        print(f"  Impares: {impares}")
        print(f"  Negativos: {negativos}")
        print(f"  Positivos: {positivos}")

    elif elec == '9':
        # Ejercicio 9: Calcular la media de 100 números
        print("\nEjercicio 9 – Ingresa 100 números para la media:")
        total = 0
        for idx in range(1, 101):
            n = int(input(f"  Número {idx}/100: "))
            total += n
        media = total / 100
        print(f"Media de los 100 números: {media}")

    elif elec == '10':
        # Ejercicio 10: Invertir el orden de los dígitos de un número
        n = int(input("\nEjercicio 10 – Ingresa un número: "))
        invertido = 0
        temp = abs(n)
        while temp:
            invertido = invertido * 10 + (temp % 10)
            temp //= 10
        if n < 0:
            invertido = -invertido
        print(f"Número invertido: {invertido}")

    elif elec == '0':
        # Salir del programa
        print("\n¡Hasta luego! 👋")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
