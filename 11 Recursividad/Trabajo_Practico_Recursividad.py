#1-Crea una función recursiva que calcule el factorial de un numero. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario un numero entero positivo
numero = int(input("Introduce un número entero positivo: "))

# Verificación de que el numero sea valido
if numero < 1:
    print("Por favor, introduce un número entero mayor o igual a 1.")
else:
    print(f"Factoriales desde 1 hasta {numero}:")
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")

#//////////////////////////////////////////////////////////////////////////

#2-Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# Función recursiva para calcular el numero de Fibonacci en la posición n
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar al usuario la cantidad de términos de la serie de Fibonacci
posicion = int(input("Introduce la posición hasta la cual quieres ver la serie de Fibonacci: "))

# Verificamos que el numero sea válido
if posicion < 0:
    print("Por favor, introduce un numero entero mayor o igual a 0.")
else:
    print(f"Serie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion + 1):
        print(f"F({i}) = {fibonacci(i)}")

#//////////////////////////////////////////////////////////////////////////

#3- Crea una función recursiva que calcule la potencia de un numero base elevado a un exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1). Prueba esta función en un algoritmo general.

# Función recursiva para calcular n^m
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Solicitar base y exponente al usuario
base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente (entero no negativo): "))

# Verificamos que el exponente sea válido
if exponente < 0:
    print("Por favor, introduce un exponente entero no negativo.")
else:
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")

#//////////////////////////////////////////////////////////////////////////

#4- Crear una función recursiva en Python que reciba un numero entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Solicitar número al usuario
numero = int(input("Introduce un numero entero positivo: "))

# Verificamos que sea válido
if numero < 0:
    print("Por favor, introduce un numero entero positivo.")
elif numero == 0:
    print("Binario: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")

#//////////////////////////////////////////////////////////////////////////

#5- Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

#//////////////////////////////////////////////////////////////////////////

#6- Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
#Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#suma_digitos(9) → 9
#suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Solicitar al usuario un número entero positivo
numero = int(input("Introduce un numero entero positivo: "))

# Verificar que el numero sea válido
if numero < 0:
    print("Por favor, introduce un numero positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")

#//////////////////////////////////////////////////////////////////////////

#7- Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Solicitar al usuario el número de bloques en el nivel más bajo
nivel_base = int(input("Introduce el número de bloques en el nivel más bajo: "))

# Verificar que el número sea válido
if nivel_base < 1:
    print("Por favor, introduce un número entero mayor o igual a 1.")
else:
    total = contar_bloques(nivel_base)
    print(f"Se necesitan {total} bloques para construir la pirámide.")

#//////////////////////////////////////////////////////////////////////////

#8- Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# Pedir datos al usuario
numero = int(input("Introduce un número entero positivo: "))
digito = int(input("Introduce el dígito que deseas contar (0-9): "))

# Verificar que los datos sean válidos
if numero < 0 or digito < 0 or digito > 9:
    print("Datos inválidos. Asegúrate de ingresar un número positivo y un dígito entre 0 y 9.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")

