#  4. Orden de llegada de corredores: Dado un listado de tiempos de llegada en una carrera,
#  ordénalos de menor a mayor usando burbuja

timend = input("Ingrese los tiempos de llegada de los primeros 10 corredores: ").split()

for i in range (len(timend)):
    timend[i] = float(timend[i])

n = len(timend)

for i in range (n):
    for j in range (0, n - 1 - i):
        if timend[j] > timend[j+1]:
            timend[j], timend[j+1] = timend[j+1], timend[j]

print (f"Los tiempos de llegada de los corredores son de: {timend:.2f}")