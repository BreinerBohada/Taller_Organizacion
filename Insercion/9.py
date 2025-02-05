#  4. Ordenación de ventas diarias: Se registraron ventas diarias de una tienda. Ordénalas en orden
#  ascendente con inserción.

num_dias = int(input("Ingrese el numero de dias para registrar las ventas: "))

ventas = []

for i in range(num_dias):
    venta = float(input(f"Ingrese la venta del dia {i+1}: "))
    ventas.append(venta)

for i in range(1, len(ventas)):
    clave = ventas[i]
    j = i - 1
    while j >= 0 and ventas[j] > clave:
        ventas[j + 1] = ventas[j]
        j -= 1
    ventas[j + 1] = clave

print("Ventas ordenadas en orden ascendente:")
for venta in ventas:
    print(f"${venta:.2f}")
