# 3. Ordenación de caracteres en una palabra: Dada una palabra, ordénala alfabéticamente utilizando
#  el método de inserción.

palabra = input("Ingrese una palabra: ")

lista_caracteres = list(palabra)

for i in range(1, len(lista_caracteres)):
    clave = lista_caracteres[i]
    j = i - 1
    while j >= 0 and lista_caracteres[j] > clave:
        lista_caracteres[j + 1] = lista_caracteres[j]
        j -= 1
    lista_caracteres[j + 1] = clave

palabra_ordenada = ''.join(lista_caracteres)
print("Palabra ordenada alfabeticamente:", palabra_ordenada)