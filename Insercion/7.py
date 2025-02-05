#  2. Ranking de puntuaciones: Un juego guarda las puntuaciones de jugadores. Ordena las
#  puntuaciones en orden descendente usando inserción

jugadores = []
puntajes = []

num_jugadores = int(input("Ingrese la cantidad de jugadores para clasificar: "))

for i in range (num_jugadores):
    nom_player = input(f"Ingrese el nombre del jugador {i+1}: ")
    score = int(input(f"Ahora ingrese el puntaje de {nom_player} para clasificarlo: "))
    jugadores.append(nom_player)
    puntajes.append(score)

for i in range (1, num_jugadores):
    clave = puntajes[i]
    jugad_clave = jugadores[i]
    j = i - 1
    while j >= 0 and clave > puntajes[j]:
        jugadores[j+1] = jugadores[j]
        puntajes[j+1] = puntajes[j]
        j -= 1
    puntajes[j+1] = clave
    jugadores[j+1] = jugad_clave


print ("Tabla de clasificacion:")

for i in range(num_jugadores):
    print (f"{i+1}. {jugadores[i]} {puntajes[i]}")