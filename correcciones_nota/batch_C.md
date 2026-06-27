# Corrección Batch C — PRs #11 al #15

**Examen:** Parcial 1 de Python 2026
**Repositorio:** python2026_parcial1_uai
**Fecha de corrección:** 27 de junio de 2026

---

## Criterios de corrección

Cada ejercicio se califica de 0 a 10. Se valora:
- Cumplimiento estricto de lo pedido en el enunciado.
- Uso correcto de las estructuras y librerías indicadas.
- Claridad y buenas prácticas.
- Nombres de archivo correctos (`ejercicio_X.py`).

---

## PR #11 — Pares JuanCruz (`Pares_JuanCruz/`)

| Ej | Puntaje | Observaciones |
|----|---------|---------------|
| 1  | **8** | `input()`, `strip()`, `title()` y f-string correctos. Pero el formato imprime `"¡Hola, ...!"` en vez del exacto `"Hola, ..."` (signos de exclamación extra). |
| 2  | **10** | `while True`, `try/except ValueError`, `return`. Mensaje correcto. Perfecto. |
| 3  | **10** | Lista de comprensión en UNA sola línea: `[palabra.upper() for palabra in palabras]`. Correcto. |
| 4  | **10** | `for alumno in sorted(alumnos, key=lambda x: x["nombre"])`. Correcto. |
| 5  | **10** | `with open`, `csv.DictReader`, imprime columna `"nombre"`. Correcto. |
| 6  | **9** | `re.search(r"\@uai\.edu\.ar$", correo)`. Escapó puntos y usó `$`. Escapó `@` innecesariamente (`\@`) pero funciona igual. |
| 7  | **9** | `len(sys.argv) != 2` cubre ambos casos (menos y más argumentos). `sys.exit(1)`. El mensaje del else dice solo "Falta un argumento" aunque podría sobrar también. |
| 8  | **10** | Clase `Libro` con `__init__`, `__str__` que devuelve `"Título por Autor"`. Perfecto. |
| 9  | **0** | ❌ **No entregado.** El archivo `ejercicio_9.py` no existe en el PR. |
| 10 | **10** | `calcular_cuadrado(n)` y `test_calcular_cuadrado()` con `assert` para 4 y 0. Correcto. |

**Total: 86/100**

---

## PR #12 — David Carletta (`David_Carletta/`)

| Ej | Puntaje | Observaciones |
|----|---------|---------------|
| 1  | **2** | ❌ Define función `llamarse(nombre, apellido)` con parámetros que no usa. Pide nombre y apellido por separado (el enunciado pide solo "nombre"). Usa `.capitalize()` en vez de `.title()` (solo capitaliza la primera letra de toda la cadena, no cada palabra). Usa concatenación `+` en vez de f-string. Solo acierta en `strip()`. |
| 2  | **1** | ❌ `int(input(...))` está **fuera** del `try`, por lo que crashea si el usuario ingresa texto. `edad == int()` no tiene sentido. Mensajes distintos a los pedidos. Solo acierta en la estructura `while True` con `try/except`. |
| 3  | **0** | ❌ No usa lista de comprensión. Usa un bucle `for` tradicional con `.append()`. Incumple el requisito de "una sola línea". |
| 4  | **0** | ❌ **No entregado.** El archivo `ejercicio_4.py` no existe. |
| 5  | **0** | ❌ `csv.DictReader("nombre")` está mal usado (no itera sobre el archivo). `open(estudiantes.csv, ...)` sin comillas en el nombre del archivo. No funciona. |
| 6  | **0** | ❌ **No entregado.** El archivo `ejercicio_6.py` no existe. |
| 7  | **0** | ❌ `if (sys.argv) == 1` compara una lista con un entero: siempre es `False`. La lógica está invertida (dice "argumentos suficientes" cuando no hay). No usa `sys.exit()` correctamente. |
| 8  | **0** | ❌ **No entregado.** El archivo `ejercicio_8.py` no existe. |
| 9  | **0** | ❌ **No entregado.** El archivo `ejercicio_9.py` no existe. |
| 10 | **3** | Solo define `calcular_cuadrado(n)` correctamente. **Falta** la función `test_calcular_cuadrado()` con los `assert`. |

**Total: 6/100**

---

## PR #13 — Leandro Montenegro (`LeandroMontenegro/`)

⚠️ El directorio se llama `LeandroMontenegro/` (sin guion bajo), no `Leandro_Montenegro/` como pide el enunciado.

| Ej | Puntaje | Observaciones |
|----|---------|---------------|
| 1  | **5** | `strip()`, `title()` y f-string correctos. Pero pide nombre **y apellido** por separado cuando el enunciado solo pide "nombre". La lógica de formateo está bien pero no cumple exactamente lo pedido. |
| 2  | **7** | `while True`, `try/except ValueError`, `break`. Correcto en esencia pero: el mensaje dice `"la edad ingresada es:"` en vez de `"Edad registrada:"`, hay un `;` innecesario, y la indentación del `while` es doble (estilo extraño). |
| 3  | **6** | La lista de comprensión `[palabra.upper() for palabra in palabras]` es correcta. Pero: usa `def main()` y no imprime el resultado (no se ve nada al ejecutar). Usa `;` innecesario. |
| 4  | **10** | `for alumno in sorted(alumnos, key=lambda x: x["nombre"])`. Correcto. |
| 5  | **10** | `with open`, `csv.DictReader`, imprime `fila["nombre"]`. Correcto. |
| 6  | **4** | ❌ `re.search(r"@uai.edu.ar$", correo)` — **NO escapó los puntos**. En regex, `.` matchea cualquier carácter, por lo que `@uaiXeduYar` también pasaría la validación. Debía usar `@uai\.edu\.ar$`. |
| 7  | **0** | ❌ **No entregado.** El archivo `ejercicio_7.py` no existe. |
| 8  | **5** | Clase `Libro` con `__init__` y `__str__` pero el formato es incorrecto: `f"'{self.titulo}' por {self.autor}"` agrega comillas simples alrededor del título (`'El Aleph' por ...` en vez de `El Aleph por ...`). |
| 9  | **0** | ❌ **No entregado.** El archivo `ejercicio_9.py` no existe. |
| 10 | **3** | Solo define `calcularCuadrado(numero)` (con camelCase, no `calcular_cuadrado`). **Falta** `test_calcular_cuadrado()`. |

**Total: 50/100**

---

## PR #14 — Agustín Aguero (`Agustin_Aguero/`)

⚠️ Nombres de archivo incorrectos: usa `Ejercicio_0X.py` (mayúscula, dos dígitos) en vez de `ejercicio_x.py`.
⚠️ Faltan los ejercicios 4, 8, 9 y 10.

| Ej | Puntaje | Observaciones |
|----|---------|---------------|
| 1  | **6** | `input()`, `strip()`, `title()` correctos. Pero usa `print("Hola,", nombre)` con concatenación por comas en vez de **f-string**, que era un requisito explícito del enunciado. |
| 2  | **8** | `while True`, `try/except ValueError`, `return`. Correcto. Pero el mensaje final dice `"Tu edad es {edad} años."` en vez de `"Edad registrada: {edad}"`. |
| 3  | **0** | ❌ No usa lista de comprensión. Usa un bucle `for` tradicional con `.append()`. Incumple el requisito de "una sola línea". |
| 4  | **0** | ❌ **No entregado.** |
| 5  | **5** | La lógica con `csv.DictReader` es correcta, pero usa una ruta **hardcodeada de Windows** (`C:\Users\Navegador\Downloads\estudiantes.csv`) que no funcionará en ningún otro entorno. Debía usar una ruta relativa `estudiantes.csv`. |
| 6  | **10** | `re.search(r"@uai\.edu\.ar$", correo)`. Puntos escapados, `$` al final. Perfecto. |
| 7  | **10** | `len(sys.argv) != 2`, `sys.exit("Error: ...")`. Correcto. |
| 8  | **0** | ❌ **No entregado.** |
| 9  | **0** | ❌ **No entregado.** |
| 10 | **0** | ❌ **No entregado.** |

**Total: 39/100**

---

## PR #15 — Federico Riquelme (`federico_riquelme/`)

| Ej | Puntaje | Observaciones |
|----|---------|---------------|
| 1  | **5** | Usa `strip()` y f-string correctos. Pero **falta `.title()`**: solo elimina espacios, no capitaliza cada palabra. El enunciado pide explícitamente "Convertir la primera letra de cada palabra a mayúscula". |
| 2  | **2** | ❌ El `input()` está **fuera** del `while True`, por lo que si el usuario ingresa texto no válido, el programa termina en vez de volver a pedir. Además el `except ValueError` tiene un `break` que haría salir del bucle ante un error, en vez de reintentar. |
| 3  | **10** | Lista de comprensión `[palabra.upper() for palabra in palabras]`. Correcto. |
| 4  | **10** | Una sola línea: `for alumno in sorted(alumnos, key=lambda x: x["nombre"]): print(alumno["nombre"])`. Correcto. |
| 5  | **10** | `with open`, `csv.DictReader`, imprime `registro['nombre']`. Correcto. |
| 6  | **10** | `re.search(r"@uai\.edu\.ar$", correo)`. Puntos escapados, `$` al final. Perfecto. |
| 7  | **2** | ❌ Verifica `len(sys.argv) < 3` y `> 3`, esperando **2 argumentos adicionales** (total 3). El enunciado pide exactamente **1 argumento adicional** (total 2, `sys.argv` de longitud 2). Lógica incorrecta. |
| 8  | **10** | Clase `Libro` con `__init__`, `__str__` que devuelve `"Título por Autor"`. Perfecto. |
| 9  | **0** | ❌ **No entregado.** El archivo `ejercicio_9.py` no existe. |
| 10 | **3** | Solo define `calcular_cuadrado(n)` correctamente. **Falta** la función `test_calcular_cuadrado()` con los `assert`. |

**Total: 62/100**

---

## Resumen final

| # | Alumno | Puntaje | Observaciones generales |
|---|--------|---------|------------------------|
| 11 | Pares JuanCruz | **86/100** | Muy buen trabajo. Solo falló el ejercicio 9 (no entregado) y detalles menores en ejercicios 1, 6 y 7. |
| 12 | David Carletta | **6/100** | Entregó 6 de 10 ejercicios y la mayoría con errores graves. No usó lista de comprensión (ej. 3), el manejo de excepciones está mal implementado (ej. 2), varios ejercicios directamente no existen. |
| 13 | Leandro Montenegro | **50/100** | Nombre de directorio incorrecto (sin guion bajo). Buenos ejercicios 4 y 5. Faltan ejercicios 7 y 9. Error conceptual en regex (ej. 6, no escapó puntos). El ejercicio 3 no imprime resultado. |
| 14 | Agustín Aguero | **39/100** | Nombres de archivo incorrectos (`Ejercicio_01.py`). Faltan 4 ejercicios (4, 8, 9, 10). No usó lista de comprensión (ej. 3). Ruta hardcodeada de Windows (ej. 5). Buenos ejercicios 6 y 7. |
| 15 | Federico Riquelme | **62/100** | Buenos ejercicios 3, 4, 5, 6 y 8. Fallas importantes: falta `.title()` (ej. 1), `input` fuera del while (ej. 2), `sys.argv` con cantidad incorrecta (ej. 7), falta ejercicio 9 y test del 10. |

---

## Estadísticas del batch

- **Promedio del batch:** 48.6/100
- **Ejercicio más fallado:** Ejercicio 9 (POO avanzado con @property) — solo 0 de 5 alumnos lo entregaron.
- **Ejercicio mejor resuelto:** Ejercicio 5 (CSV) — 3 de 5 lo hicieron perfecto (PRs 11, 13 y 15).
- **Errores recurrentes:**
  - No usar lista de comprensión (PRs 12 y 14).
  - `input()` fuera del bloque `try` (PRs 12 y 15).
  - No entregar ejercicios 9 y 10 completos.
  - Nombres de archivo incorrectos (PRs 13 y 14).
  - No escapar puntos en regex (PR 13).