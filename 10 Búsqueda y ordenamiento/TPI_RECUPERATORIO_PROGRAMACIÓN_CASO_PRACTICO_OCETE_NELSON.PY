#Este archivo de Python corresponde al caso práctico comentado en nuestro trabajo práctico
#Alumnos: Ocete Rocio Milagros y Nelson Cristhian Alejandro
#Comisión 18


#Comensamos definiendo las funciones que vamos a usar

def ordenar_por_precio(lista):                                      #función llamada ordenar_por_precio toma una lista de productos 
    for i in range(1, len(lista)):                                  #Recorremos la lista desde el segundo elemento hasta el final
        actual = lista[i]                                           # Guardamos el producto actual
        j = i - 1                                                   # Desplazamos los productos mayores hacia la derecha
        while j >= 0 and lista[j]['precio'] > actual['precio']:     # Mover producto más caro hacia la derecha
            lista[j + 1] = lista[j]                                
            j -= 1
        lista[j + 1] = actual                                       # Insertamos el producto en su posición correcta

def buscar_por_nombre(lista, nombre_producto):
    for producto in lista:                                          
        if producto["nombre"].lower() == nombre_producto.lower():   # Comparamos los nombres en minúsculas para evitar errores por mayúsculas
            return producto                                         # Si lo encontramos, lo devolvemos
    return None                                                     # Si no se encuentra, devolvemos None

# Creamos una lista de productos, cada uno representado como un diccionario con nombre y precio
productos = [
    {"nombre": "Teclado", "precio": 1500},
    {"nombre": "Mouse", "precio": 1000},
    {"nombre": "Monitor", "precio": 20000},
    {"nombre": "Auriculares", "precio": 2500},
    {"nombre": "Webcam", "precio": 3000}
]

# Ordenamos productos por precio antes de mostrarlos
ordenar_por_precio(productos)
print("Productos ordenados por precio:")                            # Mostramos la lista ordenada
for p in productos:
    print(f"{p['nombre']} - ${p['precio']}")                        # Imprimimos nombre y precio de cada producto

# Pedimos al usuario que ingrese el nombre del producto que quiere buscar
busqueda = input("\nIngrese el nombre del producto que desea buscar: ")

# Llamamos a la función de búsqueda con el nombre ingresado
resultado = buscar_por_nombre(productos, busqueda)

# Mostramos el resultado de la búsqueda
if resultado:                                                       # si lo encontramos
    print(f"Producto encontrado: {resultado['nombre']} - ${resultado['precio']}")
else:                                                               # si no lo encontramos
    print("Producto no encontrado.")