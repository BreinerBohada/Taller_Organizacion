# 5. Ordenación de productos por fecha de caducidad: Dado un conjunto de productos con fechas de
#  caducidad, ordénalos utilizando el método de heapsort

import heapq
from datetime import datetime

num_productos = int(input("¿Cuántos productos deseas ingresar? "))

productos = []

for _ in range(num_productos):
    nombre = input("Ingrese el nombre del producto: ")
    fecha_caducidad = input("Ingrese la fecha de caducidad (en formato YYYY-MM-DD): ")

    try:
        fecha = datetime.strptime(fecha_caducidad, "%Y-%m-%d")
        productos.append((nombre, fecha))
    except ValueError:
        print("Formato de fecha incorrecto. Intenta nuevamente.")
        break

heapq.heapify(productos)

productos_ordenados = []
while productos:
    productos_ordenados.append(heapq.heappop(productos))

print("\nProductos ordenados por fecha de caducidad:")
for producto in productos_ordenados:
    print(f"{producto[0]} - {producto[1].strftime('%Y-%m-%d')}")
