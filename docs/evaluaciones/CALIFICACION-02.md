# Retroalimentación — Laboratorio 02 Dividir y vencer

**Estudiante:** Erian Jose Serna Marin · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `109d104`

Muy buen trabajo: el código es correcto y el informe sigue el orden pedido.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 15 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **90 / 100** |
| **Nota (0–5)** | **4.50** |

## 1. Corrección conceptual (15 / 20)
**Lo que hizo bien:**
- En la pregunta 4 explica bien que dividir para hallar el máximo no mejora el recorrido simple: la recurrencia `T(n) = 2T(n/2) + Θ(1)` también da `Θ(n)` y solo añade llamadas recursivas.
- En la pregunta 5 recomienda divide y vencerás, da estimaciones para 1.000.000 de registros (unas 5 horas contra 1,5 segundos), dice que son estimaciones y no usa una regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 3 afirma que divide y vencerás gana desde los tamaños más pequeños, pero no lo respalda con valores medidos: en la gráfica las dos curvas se ven pegadas a cero en n pequeño y no se puede comprobar. Una tabla con los tiempos de cada tamaño le habría permitido señalar con precisión desde qué n empieza a ganar (o si con n muy pequeño la fuerza bruta es más rápida) y explicarlo.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` explicando de dónde sale cada término y lo resuelve con el método maestro (caso 2, comparando `n^(log₂ 2) = n` con `f(n)`), llegando a `Θ(n log n)`.
- Explica que la fuerza bruta acumula la suma pero aun así revisa un número cuadrático de pares.

**Lo que puede mejorar:**
- Para el `Θ(n²)` de la fuerza bruta, muestre el conteo de pares (`n(n+1)/2`) en vez de solo decir que "es cuadrático".

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en listas aleatorias; no modifican la lista recibida.
- `subarreglo_maximo` resuelve los tres casos y no llama a la fuerza bruta.
- Hay `assert` para la serie de ocho días, un elemento, todo negativo, todo positivo, caso cruzado y veinte listas aleatorias. Tiene type hints y docstrings.

**Lo que puede mejorar:**
- Las listas aleatorias de las pruebas son todas de tamaño 10; variar el tamaño probaría mejor la recursión.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y siete tamaños.
- En la pregunta 2 calcula el factor al duplicar n (4000 a 8000): unas 3,5 veces para la fuerza bruta y unas 2 para divide y vencerás, y lo contrasta con `Θ(n²)` y `Θ(n log n)`. Los valores coinciden con lo que muestra la gráfica.

**Lo que puede mejorar:**
- Analiza un solo par de tamaños; un segundo par daría más confianza.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada, el orden del informe, enlaces al código en cada parte, la gráfica visible, instrucciones para reproducir y varios commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos coinciden con un cálculo de referencia en listas aleatorias y `medicion.py` se ejecuta y genera la gráfica.

## Para el próximo laboratorio
- Incluya una tabla con los tiempos medidos de cada tamaño para respaldar lo que afirma sobre n pequeño.
- Muestre el conteo de operaciones al justificar una complejidad.
- Pruebe con listas de tamaños variados.
