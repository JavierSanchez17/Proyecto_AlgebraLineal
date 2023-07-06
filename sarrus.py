class Sarrus:

    @staticmethod
    def imprimir_matriz(matriz):
        for fila in matriz:
            print(fila)

    def calcular_sistema(self, matriz):
        print("Procedimiento de cálculo del determinante:")

        print("Matriz original:")
        self.imprimir_matriz(matriz)

        # Sarrus
        al = matriz[0][0]
        bl = matriz[0][1]
        cl = matriz[0][2]
        dl = matriz[1][0]
        el = matriz[1][1]
        fl = matriz[1][2]
        gl = matriz[2][0]
        hl = matriz[2][1]
        il = matriz[2][2]

        ax = matriz[0][3]
        bx = matriz[0][1]
        cx = matriz[0][2]
        dx = matriz[1][3]
        ex = matriz[1][1]
        fx = matriz[1][2]
        gx = matriz[2][3]
        hx = matriz[2][1]
        ix = matriz[2][2]

        ay = matriz[0][0]
        by = matriz[0][3]
        cy = matriz[0][2]
        dy = matriz[1][0]
        ey = matriz[1][3]
        fy = matriz[1][2]
        gy = matriz[2][0]
        hy = matriz[2][3]
        iy = matriz[2][2]

        az = matriz[0][0]
        bz = matriz[0][1]
        cz = matriz[0][3]
        dz = matriz[1][0]
        ez = matriz[1][1]
        fz = matriz[1][3]
        gz = matriz[2][0]
        hz = matriz[2][1]
        iz = matriz[2][3]

        print('Procedimiento: ')
        detl = (al * el * il) + (bl * fl * gl) + (cl * dl * hl) - (cl * el * gl) - (bl * dl * il) - (al * fl * hl)
        print(f'Delta: ({al} * {el} * {il}) + ({bl} * {fl} * {gl}) + ({cl} * {dl} * {hl}) - ({cl} * {el} * {gl}) - ('
              f'{bl} * {dl} * {il}) - ({al} * {fl} * {hl})')

        detx = (ax * ex * ix) + (bx * fx * gx) + (cx * dx * hx) - (cx * ex * gx) - (bx * dx * ix) - (ax * fx * hx)
        print(f'Delta x: ({ax} * {ex} * {ix}) + ({bx} * {fx} * {gx}) + ({cx} * {dx} * {hx}) - ({cx} * {ex} * {gx}) - ('
              f'{bx} * {dx} * {ix}) - ({ax} * {fx} * {hx})')

        dety = (ay * ey * iy) + (by * fy * gy) + (cy * dy * hy) - (cy * ey * gy) - (by * dy * iy) - (ay * fy * hy)
        print(f'Delta y: ({ay} * {ey} * {iy}) + ({by} * {fy} * {gy}) + ({cy} * {dy} * {hy}) - ({cy} * {ey} * {gy}) - ('
              f'{by} * {dy} * {iy}) - ({ay} * {fy} * {hy})')

        detz = (az * ez * iz) + (bz * fz * gz) + (cz * dz * hz) - (cz * ez * gz) - (bz * dz * iz) - (az * fz * hz)
        print(f'Delta z: ({az} * {ez} * {iz}) + ({bz} * {fz} * {gz}) + ({cz} * {dz} * {hz}) - ({cz} * {ez} * {gz}) - ('
              f'{bz} * {dz} * {iz}) - ({az} * {fz} * {hz})')

        # Imprimir el resultado del determinante
        print("\nDeterminante delta:", detl)
        print("\nDeterminante delta x:", detx)
        print("\nDeterminante delta y:", dety)
        print("\nDeterminante delta z:", detz)

        resultx = detx/detl
        resulty = dety/detl
        resultz = detz/detl

        return resultx, resulty, resultz
