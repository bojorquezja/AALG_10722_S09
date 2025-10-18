def merge_sort(array):
    if len(array) <= 1:
        return array

    # Dividir el arreglo en dos mitades
    mid = len(array) // 2
    array_one = array[:mid]
    array_two = array[mid:]

    array_one = merge_sort(array_one)
    array_two = merge_sort(array_two)
    # Combinar las dos mitades ordenadas
    return merge(array_one, array_two)

def merge(a, b):
    c = []

    while a and b:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])

    while len(a) > 0:
        c.append(a[0])
        a.remove(a[0])

    while len(b) > 0:
        c.append(b[0])
        b.remove(b[0])

    return c

# Números a ordenar 
numeros = [38, 27, 43, 3, 9, 82, 10, 45]
print("Lista original:", numeros)
resultado = merge_sort(numeros)
print("Lista ordenada:", resultado)