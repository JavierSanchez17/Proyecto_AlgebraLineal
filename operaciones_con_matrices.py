class OperacionesConMatrices:

    @staticmethod
    def crear_matriz_ceros(filas, columnas):
        matriz_ceros = []
        for _ in range(filas):
            fila = [0] * columnas
            matriz_ceros.append(fila)
        return matriz_ceros

    def sumar_matrices(self, matriz1, matriz2):
        filas1 = len(matriz1)
        columnas1 = len(matriz1[0])
        filas2 = len(matriz2)
        columnas2 = len(matriz2[0])
        if filas1 != filas2 or columnas1 != columnas2:
            raise ValueError('Las matrices deben tener las mismas dimensiones para realizar la suma.')

        suma = self.crear_matriz_ceros(filas1, columnas1)

        for i in range(filas1):
            for j in range(columnas1):
                suma[i][j] = matriz1[i][j] + matriz2[i][j]

                # Imprimir el proceso paso a paso
                print('Sumando elementos:')
                print(f'Elemento de matriz1[{i}][{j}]: {matriz1[i][j]}')
                print(f'Elemento de matriz2[{i}][{j}]: {matriz2[i][j]}')
                print(f'Suma: {matriz1[i][j]} + {matriz2[i][j]} = {suma[i][j]}\n')

        return suma

    # Función para restar dos matrices
    def restar_matrices(self, matriz1, matriz2):
        filas1 = len(matriz1)
        columnas1 = len(matriz1[0])
        filas2 = len(matriz2)
        columnas2 = len(matriz2[0])

        if filas1 != filas2 or columnas1 != columnas2:
            raise ValueError("Las matrices deben tener las mismas dimensiones para realizar la resta.")

        resta = self.crear_matriz_ceros(filas1, columnas1)

        for i in range(filas1):
            for j in range(columnas1):
                resta[i][j] = matriz1[i][j] - matriz2[i][j]

                # Imprimir el proceso paso a paso
                print("Restando elementos:")
                print(f"Elemento de matriz1[{i}][{j}]: {matriz1[i][j]}")
                print(f"Elemento de matriz2[{i}][{j}]: {matriz2[i][j]}")
                print(f"Resta: {matriz1[i][j]} - {matriz2[i][j]} = {resta[i][j]}\n")

        return resta

    @staticmethod
    def multiplicar_matrices(matriz1, matriz2):
        filas_matriz1 = len(matriz1)
        columnas_matriz1 = len(matriz1[0])
        filas_matriz2 = len(matriz2)
        columnas_matriz2 = len(matriz2[0])

        # Verificar si las matrices son multiplicables
        if columnas_matriz1 != filas_matriz2:
            raise ValueError("Las matrices no son multiplicables.")

        # Crear una matriz resultante llena de ceros
        matriz_resultante = [[0] * columnas_matriz2 for _ in range(filas_matriz1)]

        # Imprimir las matrices originales
        print("Matriz 1:")
        for fila in matriz1:
            print(fila)

        print("\nMatriz 2:")
        for fila in matriz2:
            print(fila)

        # Calcular la multiplicación de las matrices
        for i in range(filas_matriz1):
            for j in range(columnas_matriz2):
                for k in range(columnas_matriz1):
                    matriz_resultante[i][j] += matriz1[i][k] * matriz2[k][j]

        # Imprimir el proceso paso a paso
        print("\nProceso de multiplicación:")
        for i in range(filas_matriz1):
            for j in range(columnas_matriz2):
                print(f"\nMultiplicación de elementos:")
                for k in range(columnas_matriz1):
                    print(f"{matriz1[i][k]} * {matriz2[k][j]} = {matriz1[i][k] * matriz2[k][j]}")
                print(f"\nSuma de los productos:")
                print(
                    f"{'+'.join([str(matriz1[i][k] * matriz2[k][j]) for k in range(columnas_matriz1)])} = {matriz_resultante[i][j]}")

        return matriz_resultante
