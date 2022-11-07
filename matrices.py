import random

def imprimir_tablero():
    columnas = " ABCDEFGHIJ"
    print(" ", end="")
    for letra in columnas:
        print(letra, end=" ")
    #for i in range(10):
    #    print(chr(65+i), end=" ")
    print()
    for orden, fila in enumerate(tablero):
        #print(orden+1, end=" "+(" " if orden+1<10 else ""))
        print(orden+1, end=" ")
        if orden+1<10:
            print(" ", end="")
        for celda in fila:
            print(celda, end=" ")
        print()

# Crea tablero 10x10
# versión con listas por comprensión
#tablero = [ [ "V" for _ in range(10) ] for _ in range(10) ]
# versión loser
tablero = []
for _ in range(10):
    fila = []
    for _ in range(10):
        fila.append("V")
    tablero.append(fila)


imprimir_tablero()
