
"""Pruebas para la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_lista_enlazada() -> None:
    """Verifica las operaciones basicas de la lista enlazada."""
    lista = ListaEnlazada()

    assert lista.buscar(1000000010) is None

    lista.insertar(1000000010, "en bodega")
    lista.insertar(1000000024, "en reparto")

    assert lista.tamano == 2
    assert lista.buscar(1000000010) == "en bodega"
    assert lista.buscar(1000000024) == "en reparto"
    assert lista.buscar(9999999999) is None


def probar_tabla_hash() -> None:
    """Verifica busquedas, colisiones y factor de carga."""
    tabla = TablaHash(7)

    assert tabla.buscar(99) is None

    tabla.insertar(10, "en bodega")
    tabla.insertar(24, "en reparto")
    tabla.insertar(17, "entregado")

    assert tabla.hash(10) == 3
    assert tabla.hash(24) == 3
    assert tabla.hash(17) == 3

    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en reparto"
    assert tabla.buscar(17) == "entregado"
    assert tabla.buscar(99) is None

    assert tabla.casillas[3].tamano == 3
    assert tabla.tamano == 3
    assert tabla.factor_carga() == 3 / 7


def probar_colecciones_aleatorias() -> None:
    """Compara ambas estructuras en veinte colecciones aleatorias."""
    azar = random.Random(42)

    for _ in range(20):
        cantidad = azar.randint(20, 100)
        guias = azar.sample(
            range(1_000_000_000, 10_000_000_000),
            cantidad,
        )

        lista = ListaEnlazada()
        tabla = TablaHash(101)
        estados = {}

        for guia in guias:
            estado = azar.choice(
                ["en bodega", "en reparto", "entregado"]
            )
            estados[guia] = estado
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        # Verificar todas las guias existentes.
        for guia in guias:
            esperado = estados[guia]
            assert lista.buscar(guia) == esperado
            assert tabla.buscar(guia) == esperado
            assert lista.buscar(guia) == tabla.buscar(guia)

        # Verificar guias que no existen.
        inexistentes = azar.sample(
            [
                guia
                for guia in range(1_000_000_000, 1_000_000_200)
                if guia not in estados
            ],
            10,
        )

        for guia in inexistentes:
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None
            assert lista.buscar(guia) == tabla.buscar(guia)


def main() -> None:
    """Ejecuta todas las pruebas."""
    probar_lista_enlazada()
    probar_tabla_hash()
    probar_colecciones_aleatorias()

    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    main()
