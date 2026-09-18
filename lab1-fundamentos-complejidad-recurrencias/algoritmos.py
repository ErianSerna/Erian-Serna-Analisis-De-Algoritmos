"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""
 
"""Algoritmo punto #3"""
 
def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    copia = datos.copy()
    comparaciones = 0

    for i in range(1, len(copia)):
        actual = copia[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if copia[j] >= actual:
                break

            copia[j + 1] = copia[j]
            j -= 1

        copia[j + 1] = actual

    return copia, comparaciones
    
"""Algoritmo punto #4"""

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    copia = datos.copy()

    if len(copia) <= 1:
        return copia, 0

    mitad = len(copia) // 2

    izquierda, comparaciones_izquierda = merge_sort(copia[:mitad])
    derecha, comparaciones_derecha = merge_sort(copia[mitad:])

    resultado = []
    i = 0
    j = 0
    comparaciones = comparaciones_izquierda + comparaciones_derecha

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1

        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado, comparaciones