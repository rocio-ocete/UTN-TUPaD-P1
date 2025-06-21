
# TP Programación I – Algoritmos de Búsqueda y Ordenamiento
# Alumnos: Ocete Rocío Milagros y Nelson Cristhian Alejandro
# Comisión 18

# Importamos módulos que vamos a usar: time para medir tiempos y random para generar listas aleatorias
import time
import random

# ==========================
#       ALGORITMOS DE BÚSQUEDA
# ==========================

# Búsqueda Lineal (también llamada secuencial)
# Va recorriendo toda la lista hasta encontrar el objetivo o llegar al final
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # devuelve la posición si lo encuentra
    return -1  # devuelve -1 si no lo encuentra

# Búsqueda Binaria
# Solo funciona con listas ordenadas
# Va dividiendo la lista a la mitad y descartando la parte donde no puede estar el objetivo
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# ==========================
#       ALGORITMOS DE ORDENAMIENTO
# ==========================

# Burbuja (Bubble Sort)
# Compara elementos adyacentes y los va intercambiando si están desordenados
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # swap

# Inserción (Insertion Sort)
# Toma un elemento y lo coloca en el lugar correcto comparando con los anteriores
def insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

# Quicksort
# Algoritmo recursivo que divide la lista en menores, iguales y mayores según un pivote
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)

# ==========================
#       FUNCIONES PARA PRUEBAS DE EJECUCIÓN
# ==========================

# Genera una lista aleatoria de un tamaño dado
def generar_lista(tamaño):
    return [random.randint(1, 10000) for _ in range(tamaño)]

# Mide el tiempo promedio que tarda un algoritmo de ordenamiento
# Se repite varias veces para tener una mejor estimación
def medir_tiempo_ordenamiento(algoritmo, lista, repeticiones=100):
    total = 0
    for _ in range(repeticiones):
        copia = lista.copy()  # usamos copia para no modificar la original
        inicio = time.time()
        if algoritmo == quicksort:
            algoritmo(copia)  # quicksort devuelve una nueva lista
        else:
            algoritmo(copia)  # los otros modifican en el lugar
        fin = time.time()
        total += (fin - inicio)
    return total / repeticiones  # devolvemos el promedio

# Mide el tiempo promedio que tarda un algoritmo de búsqueda
# Repite muchas veces porque el tiempo es muy corto en listas chicas
def medir_tiempo_busqueda(algoritmo, lista, objetivo, repeticiones=10000):
    inicio = time.time()
    for _ in range(repeticiones):
        algoritmo(lista, objetivo)
    fin = time.time()
    return (fin - inicio) / repeticiones

# ==========================
#       PRUEBAS DE ORDENAMIENTO
# ==========================

print("\n===== COMPARACIÓN DE TIEMPOS DE ORDENAMIENTO =====")
for tamaño in [10, 100, 1000]:
    lista = generar_lista(tamaño)
    print(f"\n--- Lista de {tamaño} elementos ---")
    for nombre, algoritmo in [("Burbuja", burbuja), ("Inserción", insercion), ("Quicksort", quicksort)]:
        tiempo = medir_tiempo_ordenamiento(algoritmo, lista)
        print(f"{nombre}: {tiempo:.8f} segundos")

# ==========================
#       PRUEBAS DE BÚSQUEDA
# ==========================

print("\n===== COMPARACIÓN DE TIEMPOS DE BÚSQUEDA =====")
for tamaño in [10, 100, 1000]:
    lista = sorted(generar_lista(tamaño))  # importante: lista ordenada para búsqueda binaria
    objetivo = lista[tamaño // 2]  # elegimos un número seguro que está en la lista

    print(f"\n--- Lista de {tamaño} elementos ---")
    tiempo_lineal = medir_tiempo_busqueda(busqueda_lineal, lista, objetivo)
    tiempo_binaria = medir_tiempo_busqueda(busqueda_binaria, lista, objetivo)

    print(f"Búsqueda Lineal:  {tiempo_lineal:.8f} segundos")
    print(f"Búsqueda Binaria: {tiempo_binaria:.8f} segundos")
