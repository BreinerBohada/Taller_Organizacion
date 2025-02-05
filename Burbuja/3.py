#  3. Temperaturas diarias: Un sensor registra las temperaturas de una semana. Ordena los valores
#  de mayor a menor utilizando burbuja

temp = input("Ingrese las temperaturas de esta semana separadas por un espacio: ").split()

for i in range (len(temp)):
    temp[i] = int(temp[i])

n = len(temp)

for i in range (n):
    for j in range(0, n-1-i):
        if temp[j] > temp[j+1]:
            temp[j], temp[j+1] = temp[j+1], temp[j]

print (f"Las temperaturas de esta semana son de: {temp}")