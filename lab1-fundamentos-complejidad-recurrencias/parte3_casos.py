"""Experimento de Insertion Sort para los escenarios de Tamiza."""

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso
import time
import matplotlib.pyplot as plt

def main() -> None:
    """Ejecuta el experimento de la Parte 3."""

    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    comparaciones_a = []
    comparaciones_b = []
    comparaciones_c = []

    tiempos_a = []
    tiempos_b = []
    tiempos_c = []

    for n in tamanos:

        datos_a = generar_aleatorio(n, 42)
        datos_b = generar_casi_ordenado(n, 42)
        datos_c = generar_inverso(n)

        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos_a)
        fin = time.perf_counter()

        comparaciones_a.append(comparaciones)
        tiempos_a.append(fin - inicio)

        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos_b)
        fin = time.perf_counter()

        comparaciones_b.append(comparaciones)
        tiempos_b.append(fin - inicio)

        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos_c)
        fin = time.perf_counter()

        comparaciones_c.append(comparaciones)
        tiempos_c.append(fin - inicio)

    # Grafica de comparaciones
    plt.figure()

    plt.plot(tamanos, comparaciones_a, marker="o",
             label="Escenario A - Aleatorio")
    plt.plot(tamanos, comparaciones_b, marker="o",
             label="Escenario B - Casi ordenado")
    plt.plot(tamanos, comparaciones_c, marker="o",
             label="Escenario C - Inverso")

    plt.title("Comparaciones de Insertion Sort")
    plt.xlabel("Tamaño de entrada")
    plt.ylabel("Comparaciones")
    plt.legend()
    plt.grid()

    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()

    # Grafica de tiempo
    plt.figure()

    plt.plot(tamanos, tiempos_a, marker="o",
             label="Escenario A - Aleatorio")
    plt.plot(tamanos, tiempos_b, marker="o",
             label="Escenario B - Casi ordenado")
    plt.plot(tamanos, tiempos_c, marker="o",
             label="Escenario C - Inverso")

    plt.title("Tiempo de ejecución de Insertion Sort")
    plt.xlabel("Tamaño de entrada")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid()

    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()


if __name__ == "__main__":
    main()