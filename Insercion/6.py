#  1. Ordenación de edades: Un grupo de personas tiene diferentes edades. Utiliza inserción para
#  ordenarlas de menor a mayor

edades = input("Ingrese las edades a ordenar separadas por un espacio: ").split()

for i in range(len(edades)):
    edades[i] = int(edades[i])

for i in range (1, len(edades)):
    clave = edades[i]
    j = i - 1
    while j >= 0 and clave < edades[j]:
        edades[j+1] = edades[j]
        j -= 1
    edades[j+1] = clave

print (f"Edades ordenadas: {edades}")