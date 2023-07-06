import os
import re
import numpy as np
from operaciones_con_matrices import OperacionesConMatrices
from matriz_inversa import MatrizInversa
from rango_matriz import RangoMatriz
from determinante_matriz import DeterminanteMatriz
from sarrus import Sarrus
from cadena_markov import CadenaMarkov

operaciones = OperacionesConMatrices()


while True:
    os.system('cls')
    print('Menu de operaciones')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. Matriz inversa')
    print('5. Rango de una matriz')
    print('6. Determinante de una matriz')
    print('7. Sistema de ecuaciones lineales de 3x3 por Sarrus')
    print('8. Cadena de Markov')
    print('9. Salir')

    opcion = int(input('\nIngrese la opcion que desee: '))

    if opcion == 1:
        os.system('cls')

        print('Suma de matrices')

        print('Ingreso de matrices')
        filas_matriz1 = int(input('Ingrese el número de filas de la matriz 1: '))
        columnas_matriz1 = int(input('Ingrese el número de columnas de la matriz 1: '))
        filas_matriz2 = int(input('Ingrese el número de filas de la matriz 2: '))
        columnas_matriz2 = int(input('Ingrese el número de columnas de la matriz 2: '))

        # Crear la matriz 1 ingresando los elementos
        matriz1 = []
        print('\nIngrese los elementos de la matriz 1:')
        for i in range(filas_matriz1):
            fila = []
            for j in range(columnas_matriz1):
                elemento = int(input(f'Ingrese un elemento de la fila {i + 1}, columna {j + 1}: '))
                fila.append(elemento)
            matriz1.append(fila)

        # Crear la matriz 2 ingresando los elementos
        matriz2 = []
        print('\nIngrese los elementos de la matriz 2:')
        for i in range(filas_matriz2):
            fila = []
            for j in range(columnas_matriz2):
                elemento = int(input(f'Ingrese elemento de la fila {i + 1}, columna {j + 1}: '))
                fila.append(elemento)
            matriz2.append(fila)

        print('\nMatriz 1:')
        for fila in matriz1:
            print(fila)

        print('\nMatriz 2:')
        for fila in matriz2:
            print(fila)

        print('')

        os.system('pause')

        # Verificar que tengan las mismas dimensiones
        if filas_matriz1 != filas_matriz2 or columnas_matriz1 != columnas_matriz2:
            print('Las matrices deben tener las mismas dimensiones para realizar la suma.')
        else:
            # Realizar la suma de las matrices
            resultado = operaciones.sumar_matrices(matriz1, matriz2)

            # Imprimir el resultado
            print('Resultado de la suma:')
            for fila in resultado:
                print(fila)

        os.system('pause')

    elif opcion == 2:
        os.system('cls')

        print('Resta de matrices')

        print('Ingreso de matrices')
        filas_matriz1 = int(input('Ingrese el número de filas de la matriz 1: '))
        columnas_matriz1 = int(input('Ingrese el número de columnas de la matriz 1: '))
        filas_matriz2 = int(input('Ingrese el número de filas de la matriz 2: '))
        columnas_matriz2 = int(input('Ingrese el número de columnas de la matriz 2: '))

        # Crear la matriz 1 ingresando los elementos
        matriz1 = []
        print('\nIngrese los elementos de la matriz 1:')
        for i in range(filas_matriz1):
            fila = []
            for j in range(columnas_matriz1):
                elemento = int(input(f'Ingrese un elemento de la fila {i + 1}, columna {j + 1}: '))
                fila.append(elemento)
            matriz1.append(fila)

        # Crear la matriz 2 ingresando los elementos
        matriz2 = []
        print('\nIngrese los elementos de la matriz 2:')
        for i in range(filas_matriz2):
            fila = []
            for j in range(columnas_matriz2):
                elemento = int(input(f'Ingrese elemento de la fila {i + 1}, columna {j + 1}: '))
                fila.append(elemento)
            matriz2.append(fila)

        print('\nMatriz 1:')
        for fila in matriz1:
            print(fila)

        print('\nMatriz 2:')
        for fila in matriz2:
            print(fila)

        print('')

        os.system('pause')

        # Verificar si las dimensiones son compatibles para la resta
        if filas_matriz1 != filas_matriz2 or columnas_matriz1 != columnas_matriz2:
            print("Las matrices deben tener las mismas dimensiones para realizar la resta.")
        else:
            # Realizar la resta de las matrices
            resultado = operaciones.restar_matrices(matriz1, matriz2)

            # Imprimir las matrices y el resultado
            print("\nMatriz 1:")
            for fila in matriz1:
                print(fila)

            print("\nMatriz 2:")
            for fila in matriz2:
                print(fila)

            print("\nResultado de la resta:")
            for fila in resultado:
                print(fila)

        os.system('pause')

    elif opcion == 3:
        os.system('cls')

        print('Multiplicación de matrices')

        print('Ingreso de matrices')
        filas_matriz1 = int(input('Ingrese el número de filas de la matriz 1: '))
        columnas_matriz1 = int(input('Ingrese el número de columnas de la matriz 1: '))
        filas_matriz2 = int(input('Ingrese el número de filas de la matriz 2: '))
        columnas_matriz2 = int(input('Ingrese el número de columnas de la matriz 2: '))

        # Crear la matriz 1 ingresando los elementos
        matriz1 = []
        print('\nIngrese los elementos de la matriz 1:')
        for i in range(filas_matriz1):
            fila = []
            for j in range(columnas_matriz1):
                elemento = float(input(f'Ingrese un elemento de la fila {i + 1}, columna {j + 1}: '))
                fila.append(elemento)
            matriz1.append(fila)

        # Crear la matriz 2 ingresando los elementos
        matriz2 = []
        print('\nIngrese los elementos de la matriz 2:')
        for i in range(filas_matriz2):
            fila = []
            for j in range(columnas_matriz2):
                elemento = float(input(f'Ingrese elemento de la fila {i + 1}, columna {j + 1}: '))
                fila.append(elemento)
            matriz2.append(fila)

        print('\nMatriz 1:')
        for fila in matriz1:
            print(fila)

        print('\nMatriz 2:')
        for fila in matriz2:
            print(fila)

        print('')

        os.system('pause')

        try:
            resultado = operaciones.multiplicar_matrices(matriz1, matriz2)
            print("\nMatriz Resultante:")
            for fila in resultado:
                print(fila)
        except ValueError as e:
            print(e)

        os.system('pause')

    elif opcion == 4:
        os.system('cls')

        print('Matriz Inversa')

        print('Ingreso de matrices')
        filas_matriz1 = int(input('Ingrese el número de filas de la matriz 1: '))
        columnas_matriz1 = int(input('Ingrese el número de columnas de la matriz 1: '))

        matriz1 = []
        print('\nIngrese los elementos de la matriz 1:')
        for i in range(filas_matriz1):
            fila = []
            for j in range(columnas_matriz1):
                elemento = int(input(f'Ingrese un elemento de la fila {i + 1}, columna {j + 1}: '))
                fila.append(elemento)
            matriz1.append(fila)

        try:
            # Calcular la inversa de la matriz
            inversa = MatrizInversa().calcular_inversa(matriz1)

            # Imprimir la matriz y su inversa
            print("\nMatriz 1:")
            for fila in matriz1:
                print(fila)

            print("\nInversa de la Matriz 1:")
            for fila in inversa:
                print(fila)

        except ValueError as e:
            print("\nError:", str(e))

        os.system('pause')

    elif opcion == 5:
        os.system('cls')

        filas = int(input("Ingrese el número de filas de la matriz: "))
        columnas = int(input("Ingrese el número de columnas de la matriz: "))

        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                elemento = float(input(f"Ingrese el elemento en la posición ({i}, {j}): "))
                fila.append(elemento)
            matriz.append(fila)

        print('\nMatriz ingresada:')
        for fila in matriz:
            print(fila)
        print()
        rango = RangoMatriz().obtener_rango(matriz)
        print("El rango de la matriz es:", rango)
        os.system('pause')

    elif opcion == 6:
        os.system('cls')

        matriz = []
        filas = int(input("Ingrese el número de filas de la matriz: "))
        columnas = int(input("Ingrese el número de columnas de la matriz: "))

        print("Ingrese los elementos de la matriz:")
        for i in range(filas):
            fila = []
            for j in range(columnas):
                elemento = int(input(f"Elemento a({i + 1},{j + 1}): "))
                fila.append(elemento)
            matriz.append(fila)

        # Calcular el determinante y mostrar el procedimiento
        DeterminanteMatriz().calcular_determinante(matriz)
        os.system('pause')

    elif opcion == 7:
        os.system('cls')

        matriz = []
        lista_numeros = []
        numeros_cadena = []
        for i in range(3):
            cadena = input(f'Ingrese la ecuacion {i+1} lineal (signo pegado y separando valores): ')
            numeros_cadena.append(re.findall(r'-?\d+', cadena))

        for filas in numeros_cadena:
            fila_numeros = [int(numero) for numero in filas]
            matriz.append(fila_numeros)

        x, y, z = Sarrus().calcular_sistema(matriz)
        print(f'\nValor de las incognitas:\nx = {x}\ny = {y}\nz = {z}')
        os.system('pause')

    elif opcion == 8:
        os.system('cls')

        n = int(input("Ingrese el número de estados: "))

        matriz = np.zeros((n, n))

        for i in range(n):
            for j in range(n):
                probabilidad = float(
                    input(f"Ingrese la probabilidad de la matriz del estado {i + 1} a estado {j + 1}: "))
                matriz[i][j] = probabilidad

        print(f'\nMatriz original\n{matriz}\n')

        suma_filas = np.sum(matriz, axis=1)

        condicion = False

        cont = 1
        for i in suma_filas:
            if i == 1.0:
                print(f'La fila {cont} suma 1')
                cont += 1

            else:
                condicion = True
                print(f'La fila {cont} no suma 1')

        if condicion:
            break

        print(f'\nMatriz de transición\n{matriz.T}\n')
        os.system('pause')

        matrizx = []
        print('Matriz x')
        for i in range(n):
            fila = []
            for j in range(1):
                elemento = int(input(f'Ingrese elemento de la fila {i + 1}, columna {j + 1}: '))
                fila.append(elemento)
            matrizx.append(fila)

        matrizx_np = np.array(matrizx)

        print()
        for i in matrizx_np:
            print(i)
        print()

        CadenaMarkov().cadena(matriz.T, matrizx_np)
        os.system('pause')

    elif opcion == 9:
        break

    else:
        print('Opcion invalida')
