# 3. Lista de números aleatorios: Genera una lista de 20 números aleatorios y ordénalos con el
#  algoritmo de mergesort

import random

numeros = [random.randint(1, 100) for _ in range(20)]

mitad = len(numeros) // 2
izquierda = numeros[:mitad]
derecha = numeros[mitad:]

while len(izquierda) > 1:
    mitad_izq = len(izquierda) // 2
    izquierda = izquierda[:mitad_izq]
while len(derecha) > 1:
    mitad_der = len(derecha) // 2
    derecha = derecha[:mitad_der]

resultado = []
while izquierda and derecha:
    if izquierda[0] < derecha[0]:
        resultado.append(izquierda.pop(0))
    else:
        resultado.append(derecha.pop(0))

resultado += izquierda
resultado += derecha

numeros = resultado
numeros
