import pygame

bordes_negro = (0, 0, 0)
casilla_blancas= (255, 255, 255)
posible_numero_verde= (0, 255, 0)
posible_mina_rojo = (255, 0, 0)

largo = 20
alto = 20

# Establecemos el margen entre las celdas.
MARGEN = 5

# Creamos un array bidimensional. Un array bidimensional
# no es más que una lista de listas.
grid = []
for fila in range(10):
    # Añadimos un array vacío que contendrá cada celda
    # en esta fila
    grid.append([])
    for columna in range(10):
        grid[fila].append(0)  # Añade una celda

# Establecemos la fila 1, celda 5 a uno. (Recuerda, los números de las filas y
# columnas empiezan en cero.)
grid[1][5] = 1

# Inicializamos pygame
pygame.init()

# Establecemos el LARGO y ALTO de la pantalla
DIMENSION_VENTANA = [255, 255]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)

# Establecemos el título de la pantalla.
pygame.display.set_caption("Retículas y Matrices")

# Iteramos hasta que el usuario pulse el botón de salir.
hecho = False

# Lo usamos para establecer cuán rápido de refresca la pantalla.
reloj = pygame.time.Clock()

# -------- Bucle Principal del Programa-----------
while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # El usuario presiona el ratón. Obtiene su posición.
            pos = pygame.mouse.get_pos()
            # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
            columna = pos[0] // (largo + MARGEN)
            fila = pos[1] // (largo + MARGEN)
            # Establece esa ubicación a cero
            grid[fila][columna] = 1
            print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)

    # Establecemos el fondo de pantalla.
    pantalla.fill(bordes_negro)

    for fila in range(10):
        for columna in range(10):
            color = casilla_blancas
            if grid[fila][columna] == 1:
                color = posible_numero_verde
            pygame.draw.rect(pantalla,
                             color,
                             [(MARGEN + largo) * columna + MARGEN,
                              (MARGEN + alto) * fila + MARGEN,
                              largo,
                              alto])

    reloj.tick(60)

    pygame.display.flip()

pygame.quit()