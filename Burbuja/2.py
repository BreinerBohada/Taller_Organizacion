# 2. Ordenación de nombres por longitud: Ordena una lista de nombres según la cantidad de
#  caracteres utilizando ordenamiento burbuja.

nom = input("Ingrese 6 nombres que desee organizar, separados por un espacio: ").split()

n = len(nom)

for i in range (n):
    for j in range (0, n-i-1):
        if len(nom[j]) > len(nom[j+1]):
            nom[j], nom[j+1] = nom[j+1], nom[j]

print (f"Nombres ordenados por su numero de caracteres: {nom}")