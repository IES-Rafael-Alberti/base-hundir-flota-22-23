import random

from matrices import tablero, imprimir_tablero

barcos = ((1, 4), (2, 3), (3, 2), (4, 1))

miTablero = tablero()

for numero_barcos, posiciones in barcos:
    for _ in numero_barcos:
        while True:
            fila = random.randint(1,10)
            columna = random.randint(1,10)
            orientacion = random.randint(0,1)
            if comprueba_barco(tablero, fila, columna, orientacion, posiciones):
                break
        coloca_barco(tablero, fila, columna, orientacion, posiciones)
