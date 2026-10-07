"""Medición de tiempos para los algoritmos de subarreglo máximo."""

import random
import time

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def main() -> None:
    """Mide los tiempos de ejecución y genera una gráfica comparativa.

    Genera arreglos aleatorios de varios tamaños, ejecuta los algoritmos
    de fuerza bruta y divide y vencerás para medir su rendimiento promedio,
    valida la consistencia entre sus resultados y guarda/muestra la
    gráfica correspondiente.

    Args:
        None

    Returns:
        None
    """
    tamanos: list[int] = [10, 50, 100, 500, 1000, 4000, 8000]
    repeticiones: int = 5

    tiempos_fuerza: list[float] = []
    tiempos_divide: list[float] = []

    random.seed(42)

    for n in tamanos:
        datos: list[int] = [random.randint(-100, 100) for _ in range(n)]

        mediciones_fuerza: list[float] = []
        mediciones_divide: list[float] = []

        for _ in range(repeticiones):
            inicio: float = time.perf_counter()
            resultado_fuerza = subarreglo_fuerza_bruta(datos)
            fin: float = time.perf_counter()

            mediciones_fuerza.append(fin - inicio)

            inicio = time.perf_counter()
            resultado_divide = subarreglo_maximo(
                datos, 0, len(datos) - 1
            )
            fin = time.perf_counter()

            mediciones_divide.append(fin - inicio)

            assert resultado_fuerza[2] == resultado_divide[2]

        tiempo_fuerza: float = sum(mediciones_fuerza) / repeticiones
        tiempo_divide: float = sum(mediciones_divide) / repeticiones

        tiempos_fuerza.append(tiempo_fuerza)
        tiempos_divide.append(tiempo_divide)

        print(
            f"n={n}: "
            f"fuerza bruta={tiempo_fuerza:.6f}s, "
            f"divide y vencerás={tiempo_divide:.6f}s"
        )

    plt.plot(
        tamanos,
        tiempos_fuerza,
        marker="o",
        label="Fuerza bruta",
    )
    plt.plot(
        tamanos,
        tiempos_divide,
        marker="o",
        label="Divide y vencerás",
    )

    plt.title("Tiempo de ejecución vs. tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig("graficas/tiempo_vs_n.png")
    plt.show()


if __name__ == "__main__":
    main()