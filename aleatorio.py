import random

from matrices import tablero, imprimir_tablero

def comprueba_barco(tablero, fila, columna, orientacion, posiciones):
    for i in range(posiciones):
        if columna+i*(orientacion==0) >= len(tablero[0]):
            return False
        if fila+i*orientacion >= len(tablero):
            return False
        if tablero[fila+i*orientacion][columna+i*(orientacion==0)] != " ":
            return False
    return True

def coloca_barco(tablero, fila, columna, orientacion, posiciones):
    for i in range(posiciones):
        tablero[fila+i*orientacion][columna+i*(orientacion==0)] = str(posiciones)

if __name__ == "__main__":
    barcos = ((1, 4), (2, 3), (3, 2), (4, 1))

    miTablero = tablero()

    for numero_barcos, posiciones in barcos:
        for _ in range(numero_barcos):
            while True:
                fila = random.randint(1,10)
                columna = random.randint(1,10)
                orientacion = random.randint(0,1)
                if comprueba_barco(miTablero, fila, columna, orientacion, posiciones):
                    break
            coloca_barco(miTablero, fila, columna, orientacion, posiciones)
    imprimir_tablero(miTablero)