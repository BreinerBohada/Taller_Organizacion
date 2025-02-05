#  1. Ordenación de notas de estudiantes: Dado un arreglo de calificaciones, ordénalas de menor a
#  mayor usando el método de burbuja.


calif = input("Ingrese 5 calificaciones separadas por espacios: ").split()

for i in range (len(calif)):
    calif[i] = float(calif[i])

n = len(calif)

for i in range(n-1):
    for j in range(n - 1 - i):
        if calif[j] > calif[j+1]:
            calif[j], calif[j+1] = calif[j+1], calif[j]

print (f"Las calificaciones ordenadas de menor a mayor son: {calif}")