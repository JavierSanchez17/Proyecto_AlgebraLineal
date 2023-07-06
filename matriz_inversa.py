class MatrizInversa:

    @staticmethod
    def crear_matriz_identidad(n):
        matriz_identidad = []
        for i in range(n):
            fila = [0] * n
            fila[i] = 1
            matriz_identidad.append(fila)
        return matriz_identidad

    @staticmethod
    # Función para intercambiar dos filas de una matriz
    def intercambiar_filas(matriz, fila1, fila2):
        matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]
        print(f'La matriz {matriz[fila1]} sera {matriz[fila2]}\nLa matriz {matriz[fila2]} = {matriz[fila1]}')

    @staticmethod
    # Función para multiplicar una fila de una matriz por un escalar
    def multiplicar_fila_por_escalar(matriz, fila, escalar):
        for i in range(len(matriz[fila])):
            print(f'{matriz[fila][i]} * {escalar} = {matriz[fila][i] * escalar}')
            matriz[fila][i] *= escalar

    @staticmethod
    # Función para restar una fila multiplicada por un escalar a otra fila
    def restar_fila_multiplicada(matriz, fila1, fila2, escalar):
        for i in range(len(matriz[fila1])):
            print(f'{escalar} * {matriz[fila1][i]} = {escalar * matriz[fila1][i]}')
            print(f'{matriz[fila2][i]} - {escalar * matriz[fila1][i]} = {matriz[fila2][i] - (escalar * matriz[fila1][i])}\n')
            matriz[fila2][i] -= escalar * matriz[fila1][i]

    # Función para encontrar la inversa de una matriz
    def calcular_inversa(self, matriz):
        n = len(matriz)
        matriz_aumentada = [fila + self.crear_matriz_identidad(n)[i] for i, fila in enumerate(matriz)]

        # Imprimir la matriz original
        print("Matriz original:")
        for fila in matriz:
            print(fila)

        # Imprimir la matriz aumentada
        print("\nMatriz aumentada:")
        for fila in matriz_aumentada:
            print(fila)

        print('\nCalculo de la inversa:')

        for i in range(n):
            if matriz_aumentada[i][i] == 0:
                fila_no_cero = next((fila for fila in range(i + 1, n) if matriz_aumentada[fila][i] != 0), None)
                if fila_no_cero is None:
                    raise ValueError("La matriz no tiene inversa.")
                self.intercambiar_filas(matriz_aumentada, i, fila_no_cero)

            multiplicador = 1 / matriz_aumentada[i][i]
            print(f'\nMultiplicador para hacer el elemento igual a uno: 1/{matriz_aumentada[i][i]}')
            self.multiplicar_fila_por_escalar(matriz_aumentada, i, multiplicador)
            print('\nSe multiplica la fila completa')

            for fila in matriz_aumentada:
                print(fila)
            print()

            for j in range(i + 1, n):
                multiplicador = matriz_aumentada[j][i]
                print('Multiplicador para hacer cero el elemento debajo de la diagonal: ', multiplicador)
                self.restar_fila_multiplicada(matriz_aumentada, i, j, multiplicador)

                for fila in matriz_aumentada:
                    print(fila)
                print()

        for i in range(n - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                multiplicador = matriz_aumentada[j][i]
                print('Multiplicador para volver a la matriz de identidad: ', multiplicador)
                self.restar_fila_multiplicada(matriz_aumentada, i, j, multiplicador)

            for fila in matriz_aumentada:
                print(fila)
            print()

        inversa = [fila[n:] for fila in matriz_aumentada]

        return inversa
