# 1. Ordenación de salarios: Dado un conjunto de salarios de empleados, ordénalos utilizando el
# método de selección.

salarios = input("Ingrese los salarios que desea ordenar separados por un espacio: ").split()

for i in range(len(salarios)):
    salarios[i] = float(salarios[i])

for i in range(len(salarios)):
    for j in range(0, len(salarios)-i-1):
        if salarios[j] > salarios[j+1]:
            salarios[j], salarios[j+1] = salarios[j+1], salarios[j]

print("Salarios ordenados:")
for salario in salarios:
    print(f"{salario:.2f}")
