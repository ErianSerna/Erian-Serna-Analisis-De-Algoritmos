# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Erian Jose Serna Marin · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `54f76c1`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 21 / 25 |
| Corrección de la implementación | 16 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 5 / 10 |
| **Total** | **79 / 100** |
| **Nota (0–5)** | **3.95** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el algoritmo sea correcto y que llegue a tiempo, y nombra la ventana de cuatro horas como la restricción que se incumple.
- Explica que comprar un servidor más rápido solo da alivio temporal si los datos siguen creciendo.
- En la parte ética identifica dos afectados (operador y paciente) y dice quién asume el costo en cada caso.
- Explica la obligación de que la lista esté realmente ordenada por riesgo, no solo a tiempo.

**Lo que puede mejorar:**
- El segundo ejemplo (conteo de vehículos del ITM) tiene datos y restricción, pero no explica por qué ese algoritmo se vuelve inviable al crecer los datos.
- La respuesta sobre el servidor no usa un número que muestre por qué el doble de velocidad no alcanza.
- La parte ambiental queda general: faltó ligar el tiempo de ejecución con un consumo de energía acumulado más concreto.

## 2. Calidad de la explicación teórica (21 / 25)
**Lo que hizo bien:**
- Define peor, mejor y caso promedio sobre las entradas de un tamaño fijo, y justifica que usaría el peor caso por la ventana estricta.
- Dejó la predicción antes del experimento y la contrastó después.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con el método maestro, verificando el caso 2.
- Incluye la tabla de complejidades.

**Lo que puede mejorar:**
- El análisis línea a línea de insertion sort deja la línea más importante (el `while`) como "depende del caso"; debía contar cuántas veces se ejecuta en cada caso y sumar.
- El caso promedio de insertion sort se afirma sin justificarlo.

## 3. Corrección de la implementación (16 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien los tres escenarios, no cambian la lista original y cuentan comparaciones entre elementos.
- No usa `sorted()` ni `sort()`; la mezcla de merge sort es propia y recursiva.
- Los generadores producen listas con valores distintos y usan semilla.
- Hay *type hints* y *docstrings* en las funciones.

**Lo que puede mejorar:**
- Faltan líneas en blanco entre algunas funciones (se piden dos).
- En `algoritmos.py` hay textos sueltos entre funciones ("Algoritmo punto #3") que no son documentación válida.
- En el escenario B el 2 % final son justamente los valores más pequeños, así que el lote queda casi trivialmente ordenado; mezclar valores de todo el rango daría un escenario más realista.

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, se ven, tienen título, ejes y leyenda, y los escenarios comparten ejes.
- Identifica bien el peor caso (C), el mejor (B) y el promedio (A), y lo contrasta con su predicción.
- Concluye con su gráfica que merge sort conviene y lo relaciona con Θ(n log n) frente a Θ(n²).
- Recomienda una sola implementación de merge sort y declara que la extrapolación es una estimación.

**Lo que puede mejorar:**
- Los datos citados no coinciden del todo con la gráfica: dice que insertion sort tarda 1,27 s con 6.400 registros en el escenario C, pero la gráfica publicada de la Parte 3 muestra cerca de 1,36 s. La estimación de 12,4 horas se apoya en el dato del texto, así que conviene recalcularla con el valor de la gráfica.
- La estimación para merge sort se da sin mostrar el cálculo.
- No describe qué se ve con tamaños pequeños, y la consideración distinta del tiempo no menciona memoria extra ni estabilidad.
- Los ejes no indican la unidad del tamaño (registros).

## 5. Documentación y organización del informe (5 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio, los archivos y las gráficas tienen los nombres pedidos.
- El informe está en el orden de las partes, con gráficas incrustadas y enlaces al código.
- Incluye instrucciones para reproducir el experimento.

**Lo que puede mejorar:**
- Solo hay 2 commits del laboratorio, hechos con un minuto de diferencia; se piden al menos cinco que muestren el avance.
- Las instrucciones usan rutas con `\` que solo sirven en Windows.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, generan las gráficas y los algoritmos ordenan bien de mayor a menor.

## Para el próximo laboratorio
- Haga commits pequeños y frecuentes mientras avanza, con mensajes que describan cada paso.
- Cuente en el análisis línea a línea todas las líneas, incluido el ciclo interno.
- Copie los números del informe directamente de sus gráficas o salidas y muestre el cálculo de las estimaciones.
- Revise las líneas en blanco entre funciones y quite los textos sueltos del código.
- Indique las unidades en los ejes (por ejemplo, "registros").
