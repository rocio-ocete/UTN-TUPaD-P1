#Práctico 3: Estructuras condicionales
#Actividades
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("porfavor, ingrese su edad: "))

if edad < 0:
    print("la edad no puede ser negativa")
elif edad >= 18:
    print("usted es mayor de edad")
else:
    print("usted es menor de edad")


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”.
#En caso contrario deberá mostrar el mensaje “Desaprobado”.

nota=float(input("Porfavor, ingrese su nota: "))

if nota < 0:
    print("la calificación no es valida")
elif nota <= 6:
    print("Desaprobado")
else:
    print("Aprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"
#en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
#Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar

numero = int(input("Porfavor, ingrese un numero par "))
if numero % 2 == 0 :
    print ("Ha ingresado un numero par")
else:
    print("porfavor, ingrese un numero par ")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese una edad: "))

if edad <= 0:
    print("ingrese una edad valida")
elif edad < 12:
    print("eres un niño")
elif edad >= 12 and edad < 18:
    print("eres un adolescente")
elif edad >= 18 and edad < 30:
    print("eres un adulto joven")
else:
    print("eres un adulto")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = input("Ingrese una contraseña que tenga entre 8 y 14 caracteres: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números.
#escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

import random
from statistics import mode, median, mean, StatisticsError

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
try:
    moda = mode(numeros_aleatorios)
except StatisticsError:
    moda = "No única"  

print("Lista de números:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if isinstance(moda, str):
    print("No se puede determinar el sesgo porque no hay una única moda.")
else:
    if media > mediana > moda:
        print("Distribución con sesgo positivo (a la derecha).")
    elif media < mediana < moda:
        print("Distribución con sesgo negativo (a la izquierda).")
    elif media == mediana == moda:
        print("Distribución sin sesgo.")
    else:
        print("No se puede determinar claramente el sesgo con los datos actuales.")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,
#añadir un signo de exclamación al final e imprimir el string resultante por pantalla;
#en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = str(input("Ingrasar una palabra o frase: "))

if frase[-1].lower() in "aeiou":
    frase = frase + "!"
print ("resultado", frase )

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.

nombre = input("porfavor, ingrese su nombre: ")

print("Seleccione una opción:")
print("1. MAYÚSCULAS")
print("2. minúsculas")
print("3. Primer letra en mayuscula")
opcion = input("Ingrese 1, 2 o 3: ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = int(input("Porfavor ingrese la magnitud del terremoto: "))

if magnitud <= 0:
    print("la magnitud no puede ser negativa")
elif magnitud < 3:
    print ("muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print ("leve (ligeramente perceptible)")
elif magnitud >=4 and magnitud < 5:
    print ("moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >=5 and magnitud <6:
    print ("fuerte (puede causar daños en estructuras débiles)")
elif magnitud >=6 and magnitud <7:
    print("muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Periodo del año: Desde el 21 de diciembre hasta el 20 de marzo (incluidos);Desde el 21 de marzo hasta el 20 de junio (incluidos); Desde el 21 de junio hasta el 20 de septiembre (incluidos); Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)
#Estación en el hemisferio norte: Invierno; Primavera; Verano; Otoño 
#Estación en el hemisferio sur: Verano; Otoño; Invierno; Primavera
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano

print("NORTE")
print("SUR")
hemisferio = str(input("¿En que hemisferio se encuentra?: "))

if hemisferio == "SUR" or hemisferio == "Sur" or hemisferio == "sur":
    print("1. ENERO")
    print("2. FEBRERO")
    print("3. MARZO")
    print("4. ABRIL")
    print("5. MAYO")
    print("6. JUNIO")
    print("7. JULIO")
    print("8. AGOSTO")
    print("9. SEPTIEMBRE")
    print("10. OCTUBRE")
    print("11. NOVIEMBRE")
    print("12. DICIEMBRE")

    mes = int(input("¿que mes es? porfavor elija una opción NUMERICA (1 - 12): "))
    if mes == 1 :
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en verano")
    if mes == 2 :
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=29:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en verano")
    if mes == 3 :
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        elif dia >= 1 and dia <=20:
            print("usted se encuentra en verano")
        else:
            print("usted se encuentra en otoño")
    if mes == 4:
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=31:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en otoño")
    if mes == 5:
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en otoño")
    if mes == 6 :
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=31:
            print("porfavor, escoja un día valido")
        elif dia >= 1 and dia <=20:
            print("usted se encuentra en otoño")
        else:
            print("usted se encuentra en invierno")
    if mes == 7:
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en invierno")
    if mes == 8:
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en invierno")
    if mes == 9 :
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=31:
            print("porfavor, escoja un día valido")
        elif dia >= 1 and dia <=20:
            print("usted se encuentra en invierno")
        else:
            print("usted se encuentra en primavera")
    if mes == 10:
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en primavera")
    if mes == 11:
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=31:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en primavera")
    if mes == 12 :
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        elif dia >= 1 and dia <=20:
            print("usted se encuentra en primavera")
        else:
            print("usted se encuentra en verano")
if hemisferio == "NORTE" or hemisferio == "Norte" or hemisferio == "norte":
    print("1. ENERO")
    print("2. FEBRERO")
    print("3. MARZO")
    print("4. ABRIL")
    print("5. MAYO")
    print("6. JUNIO")
    print("7. JULIO")
    print("8. AGOSTO")
    print("9. SEPTIEMBRE")
    print("10. OCTUBRE")
    print("11. NOVIEMBRE")
    print("12. DICIEMBRE")

    mes = int(input("¿que mes es? porfavor elija una opción NUMERICA (1 - 12): "))
    if mes == 1 :
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en invierno")
    if mes == 2 :
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=29:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en invierno")
    if mes == 3 :
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        elif dia >= 1 and dia <=20:
            print("usted se encuentra en invierno")
        else:
            print("usted se encuentra en primavera")
    if mes == 4:
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=31:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en primavera")
    if mes == 5:
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en primavera")
    if mes == 6 :
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=31:
            print("porfavor, escoja un día valido")
        elif dia >= 1 and dia <=20:
            print("usted se encuentra en primavera")
        else:
            print("usted se encuentra en verano")
    if mes == 7:
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en verano")
    if mes == 8:
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en verano")
    if mes == 9 :
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=31:
            print("porfavor, escoja un día valido")
        elif dia >= 1 and dia <=20:
            print("usted se encuentra en verano")
        else:
            print("usted se encuentra en otoño")
    if mes == 10:
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en otoño")
    if mes == 11:
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=31:
            print("porfavor, escoja un día valido")
        else:
            print("usted se encuentra en otoño")
    if mes == 12 :
        dia = int(input("¿que día es?: "))
        if dia <= 0 and dia >=32:
            print("porfavor, escoja un día valido")
        elif dia >= 1 and dia <=20:
            print("usted se encuentra en otoño")
        else:
            print("usted se encuentra en invierno")
