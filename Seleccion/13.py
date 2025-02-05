# 3. Lista de números aleatorios: Genera una lista de 20 números aleatorios y ordénalos con el
#  algoritmo de mergesort

import random

numeros = [random.randint(1, 100) for _ in range(20)]

def merge_sort(numeros):
    if len(numeros) <= 1:
        return numeros
    
    medio = len(numeros) // 2
    izquierda = merge_sort(numeros[:medio])
    derecha = merge_sort(numeros[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

numeros_ordenados = merge_sort(numeros)

print("Lista de números aleatorios ordenada:", numeros_ordenados)
