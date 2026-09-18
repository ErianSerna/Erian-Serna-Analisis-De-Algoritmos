"""Experimento de complejidad para Merge Sort e Insertion Sort."""

import time
import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from algoritmos import merge_sort
from datos import generar_aleatorio


def main() -> None:
    """Ejecuta el experimento de la Parte 4."""

    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    tiempos_insertion = []
    tiempos_merge = []

    for n in tamanos:
        datos = generar_aleatorio(n, 42)

        inicio = time.perf_counter()
        insertion_sort(datos)
        fin = time.perf_counter()
        tiempos_insertion.append(fin - inicio)

        inicio = time.perf_counter()
        merge_sort(datos)
        fin = time.perf_counter()
        tiempos_merge.append(fin - inicio)

    plt.figure()

    plt.plot(
        tamanos,
        tiempos_insertion,
        marker="o",
        label="Insertion Sort",
    )

    plt.plot(
        tamanos,
        tiempos_merge,
        marker="o",
        label="Merge Sort",
    )

    plt.title("Tiempo de ejecución de Insertion Sort y Merge Sort")
    plt.xlabel("Tamaño de entrada")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid()

    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()

    print("Experimento de la Parte 4 terminado.")


if __name__ == "__main__":
    main()