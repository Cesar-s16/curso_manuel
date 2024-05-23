def reloj_de_arena(n):
    # Crear una matriz de nxn llena de ceros
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        matriz.append(fila)

    # Llenar la matriz en forma de reloj de arena
    medio = n // 2
    for i in range(n):
        if i <= medio:
            for j in range(i, n - i):
                matriz[i][j] = 1
        else:
            for j in range(n - i - 1, i + 1):
                matriz[i][j] = 1

    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=' ')
        print()

# Tamaño de la matriz (debe ser impar)
while True:
    n = int(input("Ingrese el tamaño de la matriz (un número impar y positivo): "))
    if n > 0 and n % 2 != 0:
        break
    print("El número debe ser impar y positivo. Intente nuevamente.")

matriz = reloj_de_arena(n)
imprimir_matriz(matriz)
