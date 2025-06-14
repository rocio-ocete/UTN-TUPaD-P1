#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#/////////////////////////////////////////////////////////////////////////////////

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#/////////////////////////////////////////////////////////////////////////////////

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

frutas = list(precios_frutas.keys())
print(frutas)

#/////////////////////////////////////////////////////////////////////////////////

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda = {}
for i in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    telefono = input("Ingresá su número de teléfono: ")
    agenda[nombre] = telefono

consulta = input("Ingresá un nombre para buscar su número: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

#/////////////////////////////////////////////////////////////////////////////////

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresá una frase: ").lower()
palabras = frase.split()
palabras_unicas = set(palabras)

# Mostrar palabras únicas
print("Palabras únicas:", palabras_unicas)

# Contar ocurrencias
contador = {}
for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1

print("Frecuencia de palabras:", contador)

#/////////////////////////////////////////////////////////////////////////////////

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}

for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingresá la nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")

#/////////////////////////////////////////////////////////////////////////////////

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

#/////////////////////////////////////////////////////////////////////////////////

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

stock = {
    'Arroz': 10,
    'Fideos': 15,
    'Aceite': 5
}

producto = input("Ingresá un producto: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar? "))
    stock[producto] += agregar
else:
    unidades = int(input("Producto nuevo. ¿Cuántas unidades querés agregar? "))
    stock[producto] = unidades

print("Stock actualizado:", stock)

#/////////////////////////////////////////////////////////////////////////////////

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

agenda_eventos = {
    ('Lunes', '9:00'): 'Reunión con equipo',
    ('Martes', '14:00'): 'Clase de Python',
}

dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (ej. 14:00): ")

evento = agenda_eventos.get((dia, hora), "No hay eventos programados.")
print("Evento:", evento)

#/////////////////////////////////////////////////////////////////////////////////

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

paises = {
    'Argentina': 'Buenos Aires',
    'Francia': 'París',
    'Japón': 'Tokio',
    'Brasil': 'Brasilia'
}

capitales = {capital: pais for pais, capital in paises.items()}
print(capitales)

