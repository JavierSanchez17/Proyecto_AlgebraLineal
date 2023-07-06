class DeterminanteMatriz:

    @staticmethod
    def imprimir_matriz(matriz):
        for fila in matriz:
            print(fila)

    def calcular_determinante(self, matriz):
        n = len(matriz)

        if n != len(matriz[0]):
            print("Error: La matriz debe ser cuadrada.")
            return None

        if n == 1:
            det = matriz[0][0]
            print("Procedimiento de cálculo del determinante:")
            print(f"Matriz 1x1:")
            self.imprimir_matriz(matriz)
            print(f"Determinante: {det}")
            return det

        det = 0
        signo = 1

        # Expandir a lo largo de la primera fila
        for j in range(n):
            submatriz = []
            for i in range(1, n):
                fila = matriz[i][0:j] + matriz[i][j + 1:]
                submatriz.append(fila)

            subdet = self.calcular_determinante(submatriz)
            det += signo * matriz[0][j] * subdet

            print(f"\nSubmatriz {1}x{1}:")
            self.imprimir_matriz(submatriz)
            print(f"Determinante de la submatriz: {subdet}")
            print(f"Producto parcial: {signo} * {matriz[0][j]} * {subdet}")

            signo *= -1

        print("\nMatriz original:")
        self.imprimir_matriz(matriz)
        print(f"\nDeterminante final: {det}")

        return det
