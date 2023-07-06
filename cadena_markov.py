import numpy as np


class CadenaMarkov:

    @staticmethod
    def cadena(matriz, x):
        veces = int(input('Ingresa los ciclos a repetir: '))

        resultado = np.dot(matriz, x)

        print(f'\nCiclo 1\n{resultado}')

        for i in range(veces-1):
            resultado = np.dot(matriz, resultado)
            print(f'\nCiclo {i+2}:\n{resultado}')
        print()

        porcentaje = []
        for i in resultado:
            num = i.round(2)
            porcentaje.append(num*100)

        for i in range(len(porcentaje)):
            print(f'Estado {i}: {round(porcentaje[i][0])}%')
