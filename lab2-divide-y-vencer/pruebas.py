"""Pruebas de los algoritmos de subarreglo máximo."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

# 1. Serie de ocho días de la situación problema.
serie = [-3, 5, -2, 8, -6, 3, 9, -4]

resultado_fuerza = subarreglo_fuerza_bruta(serie)
resultado_divide = subarreglo_maximo(serie, 0, len(serie) - 1)

assert resultado_fuerza[2] == 17
assert resultado_divide[2] == 17

# 2. Serie de un solo elemento.
serie = [7]

resultado_fuerza = subarreglo_fuerza_bruta(serie)
resultado_divide = subarreglo_maximo(serie, 0, len(serie) - 1)

assert resultado_fuerza[2] == 7
assert resultado_divide[2] == 7

# 3. Serie con todos los valores negativos.
serie = [-8, -3, -10, -5]

resultado_fuerza = subarreglo_fuerza_bruta(serie)
resultado_divide = subarreglo_maximo(serie, 0, len(serie) - 1)

assert resultado_fuerza[2] == -3
assert resultado_divide[2] == -3

# 4. Serie con todos los valores positivos.
serie = [2, 4, 1, 5]

resultado_fuerza = subarreglo_fuerza_bruta(serie)
resultado_divide = subarreglo_maximo(serie, 0, len(serie) - 1)

assert resultado_fuerza[2] == 12
assert resultado_divide[2] == 12

# 5. Caso donde la mejor racha cruza el punto medio.
serie = [-4, 5, 2, -3, 6, -10]

resultado_fuerza = subarreglo_fuerza_bruta(serie)
resultado_divide = subarreglo_maximo(serie, 0, len(serie) - 1)

assert resultado_fuerza[2] == 10
assert resultado_divide[2] == 10

# 6. Veinte listas aleatorias.
random.seed(42)

for _ in range(20):
    serie = [random.randint(-20, 20) for _ in range(10)]

    resultado_fuerza = subarreglo_fuerza_bruta(serie)
    resultado_divide = subarreglo_maximo(
        serie, 0, len(serie) - 1
    )
    assert resultado_fuerza[2] == resultado_divide[2]

print("Todas las pruebas pasaron correctamente.")