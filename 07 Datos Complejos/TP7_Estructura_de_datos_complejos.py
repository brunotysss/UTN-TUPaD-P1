
# TP 6: Estructuras de datos complejas - Resuelto con comentarios

# 1) Añadir frutas al diccionario existente
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar precios de frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Crear lista de solo frutas (sin precios)
solo_frutas = list(precios_frutas.keys())

# 4) Agenda telefónica de 5 contactos
agenda = {}
for _ in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero

buscar = input("Ingresá el nombre para buscar su número: ")
print("Número:", agenda.get(buscar, "No se encontró ese contacto."))

# 5) Frase del usuario -> palabras únicas y conteo
frase = input("Ingresá una frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)
conteo = {}

for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Conteo de palabras:", conteo)

# 6) Tupla de notas de 3 alumnos y promedio
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} - Promedio: {promedio:.2f}")

# 7) Sets con estudiantes que aprobaron cada parcial
parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# 8) Diccionario de stock de productos
stock = {"lapiz": 10, "cuaderno": 5}
producto = input("Ingresá un producto para consultar su stock: ")
if producto in stock:
    print(f"Stock de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades agregar? "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input(f"{producto} no existe. Ingresá el stock inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# 9) Agenda con tuplas (día, hora) como claves
agenda_actividades = {
    ("lunes", "9:00"): "Reunión de equipo",
    ("martes", "10:00"): "Clase de Python"
}

dia = input("Ingresá un día: ")
hora = input("Ingresá una hora (formato 9:00): ")
actividad = agenda_actividades.get((dia.lower(), hora), "Sin actividad asignada.")
print("Actividad:", actividad)

# 10) Invertir diccionario de países y capitales
paises = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Italia": "Roma"
}

capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido:", capitales)
