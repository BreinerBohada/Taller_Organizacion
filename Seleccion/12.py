#  2. Ordenación de puntajes deportivos: Ordena una lista de puntajes deportivos utilizando el método
#  de quicksort

puntajes = input("Ingrese los puntajes separados por un espacio: ").split()

for i in range(len(puntajes)):
    puntajes[i] = int(puntajes[i])
i = 0
j = len(puntajes) - 1
pivote = puntajes[len(puntajes) // 2]

while i <= j:
    while puntajes[i] < pivote:
        i += 1
    while puntajes[j] > pivote:
        j -= 1
    if i <= j:
        puntajes[i], puntajes[j] = puntajes[j], puntajes[i]
        i += 1
        j -= 1

sublista_izquierda = puntajes[:j+1]
sublista_derecha = puntajes[i:]

print("Puntajes ordenados:", sorted(puntajes))
