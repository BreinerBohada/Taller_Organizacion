#  5. Ordenación de precios de productos: Un sistema de inventario tiene precios desordenados.
#  Ordénalos ascendentemente con burbuja

productos = []

prices = []

cantidad_prod = int(input("Ingrese el numero de productos a organizar: "))

for i in range(cantidad_prod):
    nom_prod = input(f"Ingrese el nombre del producto {i+1}: ")
    prec_prod = float(input(f"Ahora ingrese el valor de {nom_prod}: "))
    productos.append(nom_prod)
    prices.append(prec_prod)

for i in range (cantidad_prod):
    for j in range (0, cantidad_prod - 1 - i):
        if prices[j] > prices[j+1]:
            prices[j], prices[j+1] = prices[j+1], prices[j]
            productos[j], productos[j+1] = productos[j+1], productos[j]
print ("Productos ordenados por su precio:")

for i in range(cantidad_prod):
    print (f"{productos[i]}: ${prices[i]:.2f}")