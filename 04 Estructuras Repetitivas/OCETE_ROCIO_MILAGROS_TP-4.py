#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range (101):
    print(numero)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = input("Ingresa un numero entero: ")

if len(numero) > 0 and numero[0] == '-':
    numero = numero[1:]
cant_digitos = len(numero)

print("el numero tiene ", cant_digitos, " digitos ")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingresa el primer numero entero: "))
num2 = int(input("Ingresa el segundo numero entero: "))
suma = 0

if num1 < num2:
    for numero in range(num1 + 1, num2):
        suma += numero
elif num2 < num1:
    for numero in range(num2 + 1, num1):
        suma += numero
else:
    suma = 0
print("La suma de los numeros entre", num1, "y", num2, "es:", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma_total = 0
print("porfavor ingrasa un numero entero (ingresa 0 para terminar).")

while True:
    numero = int(input("Ingresa un numero: "))
    
    if numero == 0:
        break  
    suma_total += numero  
print("el total de la suma es:", suma_total)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
num_aleat = random.randint(0, 9)
intento = 0

print("adivina el numero entre 0 y 9")
while True:
    intento = int(input("ingresa el numero: "))
    intentos += 1
    if intento == num_aleat:
        print("¡Correcto! Adivinaste el numero en", intentos, "intentos.")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for numero in range(100, -1, -1):
    if numero % 2 == 0:
        print(numero)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

num = int(input("Ingresa un numero entero positivo: "))

if num < 0:
    print("El numero debe ser positivo.")
else:
    suma = 0
    for i in range(num + 1):
        suma += i
    print("La suma de los numeros de 0 a", num, "es:", suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cant_numeros = 100
pares = 0
impares = 0
positivos = 0
negativos = 0
print(f"Ingresa {cant_numeros} numeros enteros:")

for i in range(cant_numeros):
    numero = int(input(f"Numero {i + 1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
  
print("\nResultados:")
print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)
print("Cantidad de numeros positivos:", positivos)
print("Cantidad de numeros negativos:", negativos)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

cant_num = 100
suma = 0

print(f"Ingresa {cant_num} numeros enteros:")
for i in range(cant_num):
    numero = int(input(f"Numero {i + 1}: "))
    suma += numero  # Acumula la suma de los números
media = suma / cant_num
print("\nLa media de los numeros ingresados es:", media)


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingresa un numero entero: ")
numero_invertido = numero[::-1]
print("El numero invertido es:", numero_invertido)