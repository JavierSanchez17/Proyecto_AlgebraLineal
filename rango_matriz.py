class RangoMatriz:

    @staticmethod
    def obtener_rango(matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        rango = 0

        print("Procedimiento de cálculo del rango:")

        for i in range(filas):
            # Verificar si todas las entradas en la fila son cero
            if all(elemento == 0 for elemento in matriz[i]):
                continue

            rango += 1

            # Hacer cero los elementos debajo de la entrada pivote
            for j in range(i + 1, filas):
                print(f'Pivote: {matriz[i][i]}')
                factor = matriz[j][i] / matriz[i][i]
                print(f'\nFactor de multiplicacion:\n{matriz[j][i]} / {matriz[i][i]} = {factor}')
                print('\nProcedimiento:')
                for k in range(columnas):
                    num_resta = matriz[j][k]
                    matriz[j][k] -= factor * matriz[i][k]
                    print(f'{factor} * {matriz[i][k]} = {factor * matriz[i][k]}')
                    print(f'{num_resta} - {factor * matriz[i][k]} = {matriz[j][k]}\n')

                for fila in matriz:
                    print(fila)
                print()

        return rango
