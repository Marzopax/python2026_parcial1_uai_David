# Notas — Parcial 1 Python 2026

**Materia:** Python  
**Repositorio:** `cursos-uai/python2026_parcial1_uai`  
**Fecha:** 27/06/2026  
**Total alumnos:** 16  
**Ejercicios obligatorios:** 1, 2, 3, 5, 6, 7, 8 (7 ejercicios — nota = suma / 70)

---

| # | Alumno | Nota | Ej1 | Ej2 | Ej3 | Ej5 | Ej6 | Ej7 | Ej8 | Tipo de error |
|---|--------|------|-----|-----|-----|-----|-----|-----|-----|---------------|
| 1 | Lucas Calvo Coltro | **70/70** | 10 | 10 | 10 | 10 | 10 | 10 | 10 | Estructura (archivos en raíz) |
| 2 | Franco Terrazzino | **36/70** | 9 | 4 | 2 | 9 | 10 | 0 | 2 | Estructura (subdirectorios EJERCICIO 1/, naming), Conceptual (ej3: bucle en vez de comprensión, ej8: print en __str__), No entregado (ej7) |
| 3 | Fernando Almansa | **70/70** | 10 | 10 | 10 | 10 | 10 | 10 | 10 | CSV fuera del directorio |
| 4 | Mateo Dip | **68/70** | 10 | 9 | 10 | 10 | 9 | 10 | 10 | Detalle (ej2: "numero" sin tilde, ej6: typo "Correco") |
| 5 | Ulises Sosa | **0/70** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | No entregado (ej1-8) |
| 6 | Perez Carlos | **55/70** | 10 | 10 | 1 | 4 | 10 | 10 | 10 | Conceptual (ej3: bucle for + .append roto en vez de comprensión), Confusión (ej5 entregado como ej4) |
| 7 | Gallaretto Leonel | **67/70** | 10 | 9 | 10 | 10 | 10 | 10 | 8 | Naming (ejercicio.8.py con punto), Detalle (ej2: validación de rango no pedida) |
| 8 | Sebastian Cordoba | **22/70** | 4 | 5 | 0 | 4 | 2 | 0 | 7 | Estructura (carpeta con espacio), Conceptual (ej1: .capitalize() en vez de .title(), sin print, ej5: .split() en dict, ej6: regex sin escapes ni $), No entregado (ej3, ej7), Copy-paste del enunciado como comentarios |
| 9 | Lucas Jaime | **69/70** | 10 | 10 | 10 | 10 | 10 | 9 | 10 | Detalle (ej7: no imprime confirmación), Falta estudiantes.csv |
| 10 | Mateo Duran | **69/70** | 9 | 10 | 10 | 10 | 10 | 10 | 10 | Detalle (ej1: falta coma en "Hola, Nombre") |
| 11 | Pares JuanCruz | **66/70** | 8 | 10 | 10 | 10 | 9 | 9 | 10 | Detalle (ej1: "¡Hola!" con signos extra, ej6: @ escapado innecesario, ej7: mensaje del else impreciso) |
| 12 | David Carletta | **3/70** | 2 | 1 | 0 | 0 | 0 | 0 | 0 | Conceptual (ej1: .capitalize() y concatenación en vez de f-string, ej2: input() fuera del try, ej3: bucle for, ej5: DictReader mal usado, ej7: sys.argv==1 siempre False), No entregado (ej6, ej8), Sintaxis (ej5: open sin comillas) |
| 13 | Leandro Montenegro | **37/70** | 5 | 7 | 6 | 10 | 4 | 0 | 5 | Estructura (directorio sin guion bajo), Conceptual (ej6: regex sin escapar puntos, ej8: comillas extra en __str__), Detalle (ej1: nombre+apellido separados, ej2: mensaje distinto, ej3: no imprime), No entregado (ej7) |
| 14 | Agustin Aguero | **39/70** | 6 | 8 | 0 | 5 | 10 | 10 | 0 | Estructura (Ejercicio_01.py con mayúscula), Conceptual (ej1: print con coma en vez de f-string, ej3: bucle for en vez de comprensión), No entregado (ej8), Portabilidad (ej5: ruta hardcodeada C:\Users\...) |
| 15 | Federico Riquelme | **49/70** | 5 | 2 | 10 | 10 | 10 | 2 | 10 | Conceptual (ej1: falta .title(), ej2: input() fuera del while y break en except, ej7: espera 2 argumentos en vez de 1) |
| 16 | Nicolás Andrade | **22/70** | 2 | 5 | 3 | 1 | 1 | 3 | 7 | Conceptual (ej3: bucle en vez de comprensión, ej5 y ej7: confundidos) |

---

## Estadísticas

| Métrica | Valor |
|---------|-------|
| Promedio | **45.1 / 70** |
| Mediana | **52.0 / 70** |
| Nota más alta | **70/70** (Lucas Calvo Coltro, Fernando Almansa) |
| Nota más baja | **0/70** (Ulises Sosa) |
| Aprobados (≥42/70) | **9 / 16** (56%) |
| Desaprobados (<42/70) | **7 / 16** (44%) |

### Rendimiento por ejercicio

| Ej | Tema | Promedio | Entregado |
|----|------|----------|-----------|
| 1 | Cadenas (input, strip, title, f-string) | 7.1 | 16/16 |
| 2 | Excepciones (while True, try/except) | 7.0 | 16/16 |
| 3 | Lista de comprensión | 5.6 | 14/16 |
| 5 | CSV con DictReader | 6.1 | 14/16 |
| 6 | Regex (re.search, anclaje $) | 6.9 | 14/16 |
| 7 | sys.argv | 5.6 | 12/16 |
| 8 | POO básico (Libro, __init__, __str__) | 6.1 | 13/16 |

### Errores más frecuentes

1. **Lista de comprensión (ej3)** — Error conceptual más común: usar bucle `for` en vez de `[... for ... in ...]`.
2. **sys.argv (ej7)** — Varios confundieron la cantidad de argumentos.
3. **Estructura de archivos** — Directorios con espacios, archivos en raíz, nombres incorrectos.
4. **Regex (ej6)** — No escapar los puntos del dominio.
5. **`__str__` con `print` en vez de `return` (ej8)** — Error conceptual recurrente.

---

*Documento generado automáticamente por Hermes Agent. Las correcciones detalladas por alumno están en `correcciones_nota/`.*