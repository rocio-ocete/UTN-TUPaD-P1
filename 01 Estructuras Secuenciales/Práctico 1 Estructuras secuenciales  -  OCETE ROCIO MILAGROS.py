#Práctico 1: Estructuras secuenciales
#Alumna: Ocete Rocio Milagros 

#1- Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

#2- Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

#3- Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

#4- Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

#5- Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

#6- Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

#7- Crear un programa que pida al u suario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

#8- Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
            #IMC=( peso en kg)/((altura en m))  2
#C9- rear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:    
            #𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9 / 5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
#10- Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
#Respuestas:

#Ejercicio 1
print ("Hola mundo!")

#Ejercicio 2
nombre = str (input ("Ingrese su nombre ") )
print (f"Hola {nombre}!")

#Ejercicio 3
nombre = str(input ("Ingrese su nombre ") )
apellido = str(input ("Ingrese su apellido "))
edad = int(input("Ingrese su edad "))
Lugar_Residencia = str(input ("Ingrese su lugar de residencia "))	
print (f"Hola soy {nombre }{apellido} tengo {edad } años y soy de {Lugar_Residencia}")

#Ejercicio 4
radio = int(input("Cual es el radio?"))
area = 3.14 * radio**2
perimetro = 2 * radio * 3.14
print (f"Si el radio del circulo es {radio} entonces su area es {area} y su perimetro es {perimetro}")

#Ejercicio 5
segundos = int(input("ingresa una cantidad de segundos "))
horas = segundos / 3600
print (f"{segundos} segundos equivalen a {horas} horas")

#Ejercicio 6
num1 = int(input("ingresar numero "))
print(f"tabla de {num1}")	
for x in range(1, 11):
	result = int(num1 * x)
print(f"{num1} * {x} = {result}")

#Ejercicio 7
while True:
    try:
     n1 = int(input("Introduce el primer número entero (distinto de 0): "))
     n2 = int(input("Introduce el segundo número entero (distinto de 0): ")) 
     if n1 == 0 or n2 == 0:
      print("Los números deben ser distintos de 0. Inténtalo de nuevo.\n")
     else: 
         break
    except ValueError:
        print("Por favor, introduce solo números enteros.\n")

suma= n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

print("\nResultados:")
print(f"Suma: {n1} + {n2} = {suma}")
print(f"Resta: {n1} - {n2} = {resta}")
print(f"Multiplicación: {n1} * {n2} = {multiplicacion}")
print(f"División: {n1} / {n2} = {division:.2f}")

#Ejercicio 8
kg = float(input("Introduce tu peso en KG "))
altura = float(input("Introduce tu altura en metros "))
imc = kg /(altura ** 2)
print(f"Tu indice de masa corporal es: {imc:.2f}")

#Ejercicio 9
temperatura = float(input("Ingrese una temperatura en grados Celcius "))
fahrenheit = 9 / 5 * temperatura + 32
print(f"El equivalente en fahrenheit de {temperatura} es: {fahrenheit}")

#Ejercicio 10
n1 = float(input("ingrese el primer numero "))
n2 = float(input("ingrese el segundo numero "))
n3 = float(input("ingrese el tercer numero "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio entre los datos ingresados es: {promedio:.2f}") 


