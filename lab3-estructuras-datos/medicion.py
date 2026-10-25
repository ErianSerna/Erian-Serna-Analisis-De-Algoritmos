
"""Experimentos de tiempo para la lista enlazada y la tabla hash."""

import os
import random
import time

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador para reproducir la medicion.

    Returns:
        Una lista con las guias que no pertenecen a existentes.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []

    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)

    return inexistentes


def es_primo(numero: int) -> bool:
    """Indica si un numero es primo."""
    if numero < 2:
        return False

    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


def primo_cercano(numero: int) -> int:
    """Busca un numero primo cercano al valor recibido."""
    candidato = numero

    while not es_primo(candidato):
        candidato += 1

    return candidato


def medir_busquedas(estructura, guias: list[int]) -> float:
    """Calcula el tiempo medio por busqueda en segundos."""
    inicio = time.perf_counter()

    for guia in guias:
        estructura.buscar(guia)

    fin = time.perf_counter()

    return (fin - inicio) / len(guias)


def construir_estructuras(
    guias: list[int], estados: list[str], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye la lista y la tabla con las mismas guias."""
    lista = ListaEnlazada()
    tabla = TablaHash(m)

    for guia, estado in zip(guias, estados):
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    return lista, tabla


def verificar_resultados(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int],
) -> None:
    """Comprueba que ambas estructuras devuelvan los mismos estados."""
    for guia in guias[:20]:
        assert lista.buscar(guia) == tabla.buscar(guia)


def experimento_a() -> None:
    """Compara los tiempos de ambas estructuras frente al numero de guias."""
    azar = random.Random(123)
    cantidades = [100, 500, 1000, 5000, 20000, 50000]

    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    for n in cantidades:
        guias = azar.sample(
            range(10**9, 10**10),
            n,
        )
        estados = [
            azar.choice(["en bodega", "en reparto", "entregado"])
            for _ in range(n)
        ]

        # Se elige un primo cercano a n / 2.
        m = primo_cercano(max(2, n // 2))

        # La construccion ocurre fuera del cronometro.
        lista, tabla = construir_estructuras(guias, estados, m)

        verificar_resultados(lista, tabla, guias)

        inexistentes = generar_guias_inexistentes(
            set(guias), 200, semilla=7
        )

        tiempo_lista = medir_busquedas(lista, inexistentes)
        tiempo_tabla = medir_busquedas(tabla, inexistentes)

        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)

        print(
            f"n={n:>6}, m={m:>6}, "
            f"alfa={tabla.factor_carga():.2f}, "
            f"lista={tiempo_lista:.8f} s, "
            f"tabla={tiempo_tabla:.8f} s"
        )

    os.makedirs("graficas", exist_ok=True)

    plt.figure()
    plt.plot(
        cantidades,
        tiempos_lista,
        marker="o",
        label="Lista enlazada",
    )
    plt.plot(
        cantidades,
        tiempos_tabla,
        marker="o",
        label="Tabla hash",
    )
    plt.title("Tiempo de busqueda frente al numero de guias")
    plt.xlabel("Numero de guias (n)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/lista_vs_tabla.png", dpi=150)
    plt.close()


def experimento_b() -> None:
    """Mide el tiempo de la tabla hash con distintos factores de carga."""
    azar = random.Random(456)
    n = 20000
    factores = [0.5, 1, 4, 10]

    guias = azar.sample(range(10**9, 10**10), n)
    estados = [
        azar.choice(["en bodega", "en reparto", "entregado"])
        for _ in range(n)
    ]

    # Se generan una sola vez y se reutilizan en todas las tablas.
    inexistentes = generar_guias_inexistentes(
        set(guias), 200, semilla=7
    )

    tiempos: list[float] = []
    factores_reales: list[float] = []

    for alfa_objetivo in factores:
        m = round(n / alfa_objetivo)

        lista, tabla = construir_estructuras(guias, estados, m)
        verificar_resultados(lista, tabla, guias)

        tiempo = medir_busquedas(tabla, inexistentes)
        alfa_real = tabla.factor_carga()

        tiempos.append(tiempo)
        factores_reales.append(alfa_real)

        print(
            f"alfa={alfa_real:.2f}, m={m}, "
            f"tiempo={tiempo:.8f} s"
        )

    os.makedirs("graficas", exist_ok=True)

    plt.figure()
    plt.plot(
        factores_reales,
        tiempos,
        marker="o",
        label="Tabla hash",
    )
    plt.title("Tiempo de busqueda frente al factor de carga")
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/tiempo_vs_alfa.png", dpi=150)
    plt.close()


def main() -> None:
    """Ejecuta los dos experimentos y genera las graficas."""
    experimento_a()
    experimento_b()

    print("\nExperimentos terminados.")
    print("Graficas guardadas en la carpeta graficas/.")


if __name__ == "__main__":
    main()
