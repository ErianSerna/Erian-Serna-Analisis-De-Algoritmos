"""Subarreglo maximo: fuerza bruta y divide y venceras."""
 
 
def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).

    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = valores[0]

    for inicio in range(len(valores)):
        suma = 0

        for fin in range(inicio, len(valores)):
            suma += valores[fin]

            if suma > mejor_suma:
                mejor_suma = suma
                mejor_inicio = inicio
                mejor_fin = fin

    return mejor_inicio, mejor_fin, mejor_suma

 
def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    suma = 0
    mejor_suma_izquierda = float("-inf")
    mejor_inicio = medio

    for i in range(medio, inicio - 1, -1):
        suma += valores[i]

        if suma > mejor_suma_izquierda:
            mejor_suma_izquierda = suma
            mejor_inicio = i

    suma = 0
    mejor_suma_derecha = float("-inf")
    mejor_fin = medio + 1

    for i in range(medio + 1, fin + 1):
        suma += valores[i]

        if suma > mejor_suma_derecha:
            mejor_suma_derecha = suma
            mejor_fin = i

    return (
        mejor_inicio,
        mejor_fin,
        mejor_suma_izquierda + mejor_suma_derecha,
    )
 
 
def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    izquierda = subarreglo_maximo(valores, inicio, medio)
    derecha = subarreglo_maximo(valores, medio + 1, fin)
    cruzada = suma_cruzada(valores, inicio, medio, fin)

    mejor = izquierda

    if derecha[2] > mejor[2]:
        mejor = derecha

    if cruzada[2] > mejor[2]:
        mejor = cruzada

    return mejor