# 4. Ordenación de nombres por orden alfabético inverso: Usa el método de shell sort para ordenar
#  una lista de nombres en orden descendente

nombres = input("Ingrese los nombres separados por un espacio: ").split()

gap = len(nombres) // 2

while gap > 0:
    for i in range(gap, len(nombres)):
        temp = nombres[i]
        j = i
        while j >= gap and nombres[j - gap] < temp:
            nombres[j] = nombres[j - gap]
            j -= gap
        nombres[j] = temp
    
    gap //= 2  
print("Nombres ordenados de Z a A:", nombres)
