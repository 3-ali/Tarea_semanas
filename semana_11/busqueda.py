# Definimos una matriz 3x3 con números
lista = [
    [6, 5, 4],
    [8, 9, 11],
    [14, 3, 7]
]

# Función que busca un número en la matriz y devuelve su posición
def buscar_numero(numero, matriz):
    for fila in range(len(matriz)):              # Recorremos cada fila
        for columna in range(len(matriz[fila])): # Recorremos cada columna de la fila actual
            if matriz[fila][columna] == numero:  # Si encontramos el número
                return fila, columna              # Retornamos la posición como (fila, columna)
    return None  # Si no se encuentra, retornamos None

# Mostrar la matriz
print(" MATRIZ:")
for f in lista:
    print(f)

# Número a buscar
numero_buscado = 6

# Buscar el número y mostrar el resultado
posicion = buscar_numero(numero_buscado, lista)

if posicion:
    print(f"\n El número {numero_buscado} está en la posición: fila {posicion[0]}, columna {posicion[1]}")
else:
    print(f"\n El número {numero_buscado} no se encuentra en la matriz.")