from matrices import genera_tablero, imprimir_tablero
from aleatorio import coloca_barcos
import pygame

def inicializar_pygame():
    pygame.init()
    pygame.display.set_caption("Hundir la Flota")
    return pygame.display.set_mode([1024, 768])


def preparar_juego():
    barcos = ((1, 4), (2, 3), (3, 2), (4, 1))
    # Crear tablero
    tablero = genera_tablero()
    # Colocar barcos
    coloca_barcos(tablero, barcos)
    return tablero

def dibujar_tablero(tablero, screen):
    coordenadas = [10, 10]
    
    for i, linea in enumerate(tablero):
        for j, celda in enumerate(linea):
            if celda.strip() != "":
                imagen = load_image(celda)
                screen.blit(imagen, [coordenadas[0]+j*75, coordenadas[1]+i*75])

    for i in range(len(tablero)+1):
        pygame.draw.line(screen, pygame.Color("white"),
                        [coordenadas[0], coordenadas[1]+i*75], 
                        [coordenadas[0]+75*len(tablero), coordenadas[1]+i*75],
                        5)

    for j in range(len(tablero[0])+1):
        pygame.draw.line(screen, pygame.Color("white"),
                        [coordenadas[0]+j*75, coordenadas[1]], 
                        [coordenadas[0]+j*75, coordenadas[1]+len(tablero[0])*75],
                        5)


def load_image(filename, with_alpha=True):
    image = pygame.image.load("images/" + filename + ".png")
    return image.convert_alpha() if with_alpha else image.convert()

def solicita_entrada():
    # fila
    fila = 0
    columna = 0
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYUP:
                if(event.key>=ord("a") and event.key<=ord("j")):
                    fila = event.key - ord("a")
                    fin = True
                    break
    #columna
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYUP:
                if(event.key>=ord("0") and event.key<=ord("9")):
                    columna = event.key - ord("0")
                    fin = True
                    break
    return (fila, columna)

def actualiza_tablero(tablero, entrada):
    fila, columna = entrada
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = "A"
    elif tablero[fila][columna] >= "1" and tablero[fila][columna] <= "4":
        tablero[fila][columna] = "D"

if __name__ == "__main__":
    # Inicializar pygame
    mi_screen = inicializar_pygame()
    # Preparar el juego
    tablero = preparar_juego()
    #imprimir_tablero(tablero)
    # Game loop: juego
    while True:
        dibujar_tablero(tablero, mi_screen)
        pygame.display.flip()
        entrada = solicita_entrada()        
        actualiza_tablero(tablero, entrada)
        # if compreba_fin(tablero):
        #     mensaje_fin(mi_screen)
        #     pulsa_tecla(mi_screen)
        #     break

