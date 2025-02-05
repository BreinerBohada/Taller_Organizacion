# 5. Ordenación de distancia entre ciudades: Dado un arreglo con distancias entre ciudades,
#  ordénalas de menor a mayor usando inserción

num_ciudades = int(input("Ingrese el número de ciudades: "))

ciudades = []
distancias = []

for i in range(num_ciudades):
    ciudad = input(f"Ingrese el nombre de la ciudad {i+1}: ")
    distancia = float(input(f"Ingrese la distancia de {ciudad} en km: "))
    ciudades.append(ciudad)
    distancias.append(distancia)

for i in range(1, len(distancias)):
    clave_distancia = distancias[i]
    clave_ciudad = ciudades[i]
    j = i - 1
    while j >= 0 and distancias[j] > clave_distancia:
        distancias[j + 1] = distancias[j]
        ciudades[j + 1] = ciudades[j]
        j -= 1
    distancias[j + 1] = clave_distancia
    ciudades[j + 1] = clave_ciudad

print("\nCiudades ordenadas por su distancia:")
for i in range(num_ciudades):
    print(f"{ciudades[i]}: {distancias[i]:.2f} km")
