from random import randint


# Definimos la creacion de la matriz campo_minas del programa
def matriz(filas, columnas, caracter=False):
    campo_minas = []
    for i in xrange(0, filas):
        v = [caracter] * columnas
        campo_minas.append(v)
    return campo_minas


# Definimos los numeros aleatorios que estaran en el campo_minas
def minas(filas, columnas, campo_minas, cantidad_minas):
    mi = 1
    while mi <= cantidad_minas:
        fil = randint(0, filas - 1)
        col = randint(0, columnas - 1)
        if not campo_minas[fil][col]:
            campo_minas[fil][col] = True
            mi += 1
    return campo_minas


# Creación del campo_minas
def campo_minas1():
    opcion = input("¿Desea jugar?(Si = 1 , Personalizable = 0:")
    if opcion:
        while True:
            print("Seleccione la dificultad: \n")
            print("1. Nivel Facil (f).\n")
            print("2. Nivel Intermedio(i).\n")
            opcion = raw_input("Elija una opcion:")
            if opcion.lower() == ("f"):
                campo_minas = matriz(8, 8)
                minas(8, 8, campo_minas, 10)
                return campo_minas, 8, 8
            elif opcion.lower() == ("i"):
                campo_minas = matriz(16, 16)
                minas(16, 16, campo_minas, 40)
                return campo_minas, 16, 16
            else:
                print("debe escoger una de las opciones del menu.")


# Esta funcion establece un orden entre cada uno segun reglas del bscaminas
def numeros(campo_minas, filas, columnas):
    inicio = matriz(filas, columnas, ".")
    for i in xrange(0, filas):
        for j in xrange(0, columnas):
            # restricciones
            n = 0
            if i > 0 and j > 0 and campo_minas[i - 1][j - 1]:
                n += 1
            if j > 0 and campo_minas[i][j - 1]:
                n += 1
            if i < filas - 1 and j > 0 and campo_minas[i + 1][j - 1]:
                n += 1
            if i > 0 and campo_minas[i - 1][j]:
                n += 1
            if i < filas - 1 and campo_minas[i + 1][j]:
                n += 1
            if i > 0 and j < columnas - 1 and campo_minas[i - 1][j + 1]:
                n += 1
            if j < columnas - 1 and campo_minas[i][j + 1]:
                n += 1
            if i < filas - 1 and j < columnas - 1 and campo_minas[i + 1][j + 1]:
                n += 1
            if not campo_minas[i][j]:
                inicio[i][j] = n
            else:
                inicio[i][j] = True
    campo_minas = inicio
    return campo_minas


# Se muestra el campo_minas
def mostrar(campo_minas, filas, columnas, caracter):
    for i in xrange(0, filas):
        for j in xrange(0, columnas):
            if j != columnas - 1:
                if type(campo_minas[i][j]) == (int or str):
                    print
                    campo_minas[i][j],
                elif (type(campo_minas[i][j]) == bool) and (campo_minas[i][j]):
                    print
                    "*",
                else:

                    print
                    caracter,
            else:
                if type(campo_minas[i][j]) == (int or str):
                    print
                    campo_minas[i][j]
                elif (type(campo_minas[i][j]) == bool) and (campo_minas[i][j]):
                    print
                    "*"
                else:

                    print
                    caracter


# esta es la funcion que desapa el campo_minas
def minas_descubiertas(filas, columnas, fila, columna, campo_minas, nuevo):
    nuevo[fila][columna] = campo_minas[fila][columna]
    if campo_minas[fila][columna] == 0:
        if fila > 0:
            if (not campo_minas[fila - 1][columna]) and (nuevo[fila - 1][columna] != 0):
                minas_descubiertas(filas, columnas, fila - 1, columna, campo_minas, nuevo)
            else:
                nuevo[fila - 1][columna] = campo_minas[fila - 1][columna]
        if fila < filas - 1:
            if (not campo_minas[fila + 1][columna]) and (nuevo[fila + 1][columna] != 0):
                minas_descubiertas(filas, columnas, fila + 1, columna, campo_minas, nuevo)
            else:
                nuevo[fila + 1][columna] = campo_minas[fila + 1][columna]
        if columna > 0:
            if (not campo_minas[fila][columna - 1]) and (nuevo[fila][columna - 1] != 0):
                minas_descubiertas(filas, columnas, fila, columna - 1, campo_minas, nuevo)
            else:
                nuevo[fila][columna - 1] = campo_minas[fila][columna - 1]
        if columna < columnas - 1:
            if (not campo_minas[fila][columna + 1]) and (nuevo[fila][columna + 1] != 0):
                minas_descubiertas(filas, columnas, fila, columna + 1, campo_minas, nuevo)
            else:
                nuevo[fila][columna + 1] = campo_minas[fila][columna + 1]


# Funcion para jugar, segun la fila y columna colocada
def jugada(filas, columnas):
    while True:
        fila = input("Ingrese la fila: ")
        columna = input("Ingrese la columna: ")
        if (1 <= fila <= filas) and (1 <= columna <= columnas):
            break
        print
        "debe escoger una ficha que este dentro del rango de fila y columna."
    return fila, columna


# Funcion prinvipal que llama a las funciones anteriores
def jugar(campo_minas, filas, columnas):
    inicio = matriz(filas, columnas, ".")
    while True:
        mostrar(inicio, filas, columnas, ".")
        fila, columna = jugada(filas, columnas)
        if type(campo_minas[fila - 1][columna - 1]) == int:
            inicio[fila - 1][columna - 1] = campo_minas[fila - 1][columna - 1]
            if campo_minas[fila - 1][columna - 1] == 0:
                minas_descubiertas(filas, columnas, fila - 1, columna - 1, campo_minas, inicio)
        else:
            mostrar(campo_minas, filas, columnas, " ")
            print("Perdiste")
            break
        termino = True
        for i in xrange(0, filas):
            for j in range(0, columnas):
                if inicio[i][j] == ".":
                    termino = False
                    break
                if not termino:
                    break
        if termino:
            print("Ganaste")


otra_ronda = True
while otra_ronda:
    campo_minas, filas, columnas = campo_minas1()
    campo_minas = numeros(campo_minas, filas, columnas)
    jugar(campo_minas, filas, columnas)

    otra_ronda = input("¿Desea jugar ora vez?(Si=1)(No=0)")
