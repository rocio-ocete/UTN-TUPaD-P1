# =========================
# Algoritmos de BÚSQUEDA
# =========================

def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

def busqueda_binaria(lista, valor):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# =========================
# Algoritmos de ORDENAMIENTO
# =========================

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)


if __name__ == "__main__":
    datos = [5, 2, 9, 1, 7]
    valor = 7

    print("Lista original:", datos)
    print("Burbuja:", bubble_sort(datos.copy()))
    print("Insertion:", insertion_sort(datos.copy()))
    print("Quicksort:", quick_sort(datos.copy()))

    print("\nBúsqueda lineal de", valor, "-> posición:", busqueda_lineal(datos, valor))
    ordenada = quick_sort(datos.copy())  # usamos quick_sort para preparar la lista
    print("Búsqueda binaria de", valor, "-> posición:", busqueda_binaria(ordenada, valor))