# Informe de Errores por Alumno y Ejercicio — Parcial 1 Python 2026

**Materia:** Python  
**Repositorio:** `cursos-uai/python2026_parcial1_uai`  
**Fecha:** 28/06/2026  
**Total alumnos:** 16  
**Ejercicios obligatorios:** 1, 2, 3, 5, 6, 7, 8

---

## Tabla resumen de errores

| Alumno | Ej | Nota | Categoría |
|--------|----|----|-----------|
| Lucas Calvo Coltro | (entrega ok) | 70/70 | Archivos en raíz |
| Franco Terrazzino | 3, 7, 8 | 38/70 | Estructura + Conceptual |
| Fernando Almansa | (entrega ok) | 70/70 | — |
| Mateo Dip | 2, 6 | 68/70 | Detalle |
| Ulises Sosa | 3, 6, 8 | 61/70 | Naming + Detalle |
| Perez Carlos | 3, 5 | 55/70 | Conceptual |
| Gallaretto Leonel | 8 | 67/70 | Naming |
| Sebastian Cordoba | 1, 3, 5, 6, 7 | 22/70 | Estructura + Conceptual grave |
| Lucas Jaime | 7 | 69/70 | Detalle |
| Mateo Duran | 1 | 69/70 | Detalle |
| Pares JuanCruz | 1, 6, 7 | 66/70 | Detalle |
| David Carletta | 1, 2, 3, 5, 6, 7, 8 | 3/70 | Conceptual grave |
| Leandro Montenegro | 1, 2, 3, 6, 8 | 47/70 | Estructura + Conceptual |
| Agustin Aguero | 1, 3, 5, 8 | 39/70 | Estructura + Conceptual |
| Federico Riquelme | 1, 2, 7 | 49/70 | Conceptual |
| Nicolás Andrade | 1, 3, 5, 6, 7 | 24/70 | Conceptual grave |

---

## 1. Lucas Calvo Coltro — 70/70

**Estructura:** Envió todos los archivos `.py` en la **raíz del repo** en lugar de su carpeta `Lucas_Calvo_Coltro/`.

| Campo | Detalle |
|-------|---------|
| **Ejercicio** | Estructura del repo |
| **Error cometido** | `ejercicio_1.py`, `ejercicio_2.py`, ..., `ejercicio_10.py` en la raíz del repositorio |
| **Cómo debería hacerlo** | Crear carpeta `Lucas_Calvo_Coltro/` y colocar todos los `.py` adentro |
| **Comentario para el docente** | A pesar del error de estructura, **entregó todos los 7 ejercicios requeridos con código correcto**. Los 70 puntos se mantienen porque el contenido de cada archivo es el esperado. El repositorio fue refactorizado por el corrector para normalizar la estructura. |

---

## 2. Franco Terrazzino — 38/70

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Estructura** | Usó subdirectorios `EJERCICIO 1/`, `EJERCICIO 2/` y nombres `ejercicio1.py` (sin guión bajo) | Carpeta `Franco_Terrazzino/` con archivos `ejercicio_1.py` (con guión bajo) | Refactorizado por el corrector |
| **Ej3** (Lista de comprensión) | Usó bucle `for` con `.append()` y lo envolvió en una función externa | Una sola línea: `[palabra.upper() for palabra in palabras]` | El enunciado pide "en una sola línea" explícitamente |
| **Ej7** (sys.argv) | **No entregó** | `if len(sys.argv) != 2: sys.exit("Error")` con uso de `sys.argv[1]` | No presentó archivo `ejercicio_7.py` |
| **Ej8** (POO) | `__str__` usa `print()` en vez de `return` | `def __str__(self): return f"{self.titulo} por {self.autor}"` | Error conceptual grave: `__str__` debe devolver string, no imprimir |

---

## 3. Fernando Almansa — 70/70

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| (entrega correcta) | — | — | Incluyó un archivo extra `calculadora.py` no solicitado |

**Comentario docente:** Nota perfecta. Solo detalle menor: entregó un archivo `calculadora.py` no requerido (no afecta la nota). No entregó `ejercicio_4.py` ni `ejercicio_9.py` (los 7 obligatorios los resolvió todos).

---

## 4. Mateo Dip — 68/70

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Ej2** (Excepciones) | Mensaje: `"El numero ingresado es: {numero}"` en vez del esperado | Mensaje: `"Edad registrada: {edad}"` (sin tilde en "número" para evitar caracteres especiales) | Detalle menor, lógica correcta |
| **Ej6** (Regex) | Mensaje `"Correco electronico es valido"` (typo "Correco") | Mensaje: `"Correo válido"` o `"El correo es válido"` | Detalle ortográfico |

**Comentario docente:** Código sólido, solo errores de detalle. Nota: **9/10 en ej2** y **9/10 en ej6**.

---

## 5. Ulises Sosa — 61/70

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Estructura** | Usó `problema1.py` a `problema10.py` (prefijo `problema`) en vez de `ejercicio_X.py` | `ejercicio_1.py` a `ejercicio_10.py` | Naming incorrecto. Refactorizado por el corrector (los archivos renombrados) |
| **Ej3** (Lista de comprensión) | Usó bucle `for` con `.append()` | Una sola línea: `[palabra.upper() for palabra in palabras]` | Incumple requisito de "una sola línea" |
| **Ej6** (Regex) | Usó `^\w+@uai\.edu\.ar$` con `\w+` y `^` innecesarios | `re.search(r"@uai\.edu\.ar$", correo)` con `$` y `\.` | Funciona pero es más complejo de lo necesario |
| **Ej8** (POO) | `__str__` devuelve `"{titulo} de {autor}"` en vez de `"por"` | `return f"{self.titulo} por {self.autor}"` | Formato incorrecto |

**Comentario docente:** A pesar del error de naming, **entregó los 7 archivos requeridos**. El corrector los renombró y calificó el contenido.

---

## 6. Perez Carlos — 55/70

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Ej3** (Lista de comprensión) | Usó bucle `for` con `palabras_mayus.append(palabra.upper())`. Variable `palabras_mayus` no inicializada → `NameError`. `append()` retorna `None` | `mayusculas = [p.upper() for p in palabras]` en una línea | Código roto, no funciona |
| **Ej4** | **Confundido con ej5**: el archivo `ejercicio_4.py` contiene código de CSV (ej5) | `ejercicio_4.py` debe tener `for alumno in sorted(alumnos, key=lambda x: x["nombre"])` | Confusión grave entre ejercicios |
| **Ej5** | **No entregado** como `ejercicio_5.py` (está en `ejercicio_4.py`) | Crear `ejercicio_5.py` con `csv.DictReader` | Ej5 nota: 4/10 por lógica correcta pero archivo mal nombrado |

**Comentario docente:** El alumno mezcló ejercicios 4 y 5. Si reorganiza los archivos sin cambiar contenido, podría recuperar ~6 puntos.

---

## 7. Gallaretto Leonel — 67/70

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Ej2** (Excepciones) | Agregó validación de rango (1-99) que **no fue pedida** | Solo validar que sea entero; usar `try/except ValueError` sin rango | Funcional pero excede el alcance del enunciado |
| **Ej8** (POO) | Archivo nombrado `ejercicio.8.py` (con punto en vez de guión bajo) | `ejercicio_8.py` | Error de naming. Contenido correcto. Refactorizado |

**Comentario docente:** Buen trabajo general. Solo detalle de naming en ej8 y validación extra no solicitada en ej2.

---

## 8. Sebastian Cordoba — 22/70

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Estructura** | Carpeta `Sebastian Cordoba/` con espacio en el nombre en vez de `Sebastian_Cordoba/` | `Sebastian_Cordoba/` (con guión bajo) | Incumple instrucción explícita del enunciado |
| **Ej1** | Usó `.capitalize()` (solo primera letra), no `print()` del f-string, faltó coma en "Hola, Nombre" | `nombre = nombre.strip().title(); print(f"Hola, {nombre}")` | Tres errores en 4 líneas |
| **Ej3** | **No entregado** | Lista de comprensión | — |
| **Ej5** (CSV) | `row.split()` — `row` es dict (DictReader), no string → `AttributeError` | `print(row["nombre"])` | Error conceptual grave |
| **Ej6** (Regex) | `correo.replace(".", "\.")` modifica el input. Sin `$`, sin `\.` escapados | `re.search(r"@uai\.edu\.ar$", correo)` | Regex mal implementada, no valida |
| **Ej7** | **No entregado** | `if len(sys.argv) != 2: sys.exit(...)` | — |
| **General** | Copy-paste del enunciado completo como comentarios en todos los archivos | Solo el código, comentarios solo si aportan | Ruido innecesario |

**Comentario docente:** El alumno evidenció no comprender varios conceptos. Errores conceptuales en regex, DictReader, `.title()` vs `.capitalize()`. Solo entregó 5 de 10 ejercicios.

---

## 9. Lucas Jaime — 69/70

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Ej7** (sys.argv) | No imprime confirmación cuando el argumento es válido | Después del check, agregar `print(f"Archivo: {sys.argv[1]}")` | Detalle de usabilidad |

**Comentario docente:** Código impecable en los 7 ejercicios entregados. No entregó ej4, ej9, ej10.

---

## 10. Mateo Duran — 69/70

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Ej1** | `print(f"Hola {nombre_final}")` sin coma después de "Hola" | `print(f"Hola, {nombre_final}")` | Formato: el ejemplo espera "Hola, Juan Perez" con coma |

**Comentario docente:** Excelente código, solo faltó la coma.

---

## 11. Pares JuanCruz — 66/70

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Ej1** | `print(f"¡Hola, {nombre}!")` con signos `¡...!` | `print(f"Hola, {nombre}")` (sin signos) | Ejemplo no usa signos de exclamación |
| **Ej6** (Regex) | `re.search(r"\@uai\.edu\.ar$", correo)` — escapó `@` innecesariamente | `re.search(r"@uai\.edu\.ar$", correo)` | `@` no es metacaracter, no necesita escape |
| **Ej7** | Mensaje del else dice "Falta un argumento" aunque podría sobrar también | Mensaje que cubra ambos casos | Detalle |

**Comentario docente:** Muy buen trabajo. Detalles menores solo.

---

## 12. David Carletta — 3/70 ⚠️ CASO CRÍTICO

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Ej1** | Definió función `llamarse(nombre, apellido)` con parámetros no usados. Pide nombre y apellido por separado. Usó `.capitalize()` y concatenación `+` en vez de f-string | `nombre = input("Nombre: ").strip().title(); print(f"Hola, {nombre}")` | Múltiples errores conceptuales |
| **Ej2** | `int(input(...))` **fuera del `try`** → crashea con texto. `edad == int()` no asigna nada | `try: edad = int(input(...))` dentro del bloque try | El error más grave: input fuera del try hace que el programa se caiga |
| **Ej3** | Bucle `for` con `.append()` en vez de comprensión | `[p.upper() for p in palabras]` | No entendió el concepto |
| **Ej4** | **No entregado** | sorted + lambda | — |
| **Ej5** | `csv.DictReader("nombre")` no itera. `open(estudiantes.csv, ...)` sin comillas (NameError) | `with open("estudiantes.csv") as f: csv.DictReader(f)` | Múltiples errores: nombre sin comillas, DictReader mal usado |
| **Ej6** | **No entregado** | `re.search(...)` con regex | — |
| **Ej7** | `if (sys.argv) == 1:` compara lista con int → siempre False | `if len(sys.argv) != 2: sys.exit(...)` | Lógica invertida |
| **Ej8** | **No entregado** | Clase `Libro` con `__init__` y `__str__` | — |

**Comentario docente:** ⚠️ El alumno requiere **recuperación obligatoria**. Errores conceptuales graves en estructuras básicas. Recomiendo revisión de:
- Input/Output y formato de strings
- Try/except y manejo de errores
- Listas de comprensión
- Módulo sys y argumentos CLI

---

## 13. Leandro Montenegro — 47/70

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Estructura** | Carpeta `LeandroMontenegro/` (sin guión bajo) en vez de `Leandro_Montenegro/` | Carpeta con guión bajo entre nombre y apellido | Incumple formato |
| **Ej1** | Pidió nombre **y apellido** por separado cuando el enunciado pide solo "nombre" | `input("Ingrese su nombre: ")` único | Sobreinterpretación del enunciado |
| **Ej2** | Mensaje distinto: `"la edad ingresada es:"` (minúscula, distinto texto) | `"Edad registrada: {edad}"` | Detalle |
| **Ej3** | Lista de comprensión correcta pero **no imprime el resultado** | `print([p.upper() for p in palabras])` | El programa no muestra nada |
| **Ej6** (Regex) | `re.search(r"@uai.edu.ar$", correo)` — **no escapó los puntos** | `re.search(r"@uai\.edu\.ar$", correo)` con `\.` | Error conceptual: `.` en regex matchea cualquier carácter |
| **Ej8** | `f"'{self.titulo}' por {self.autor}"` agrega comillas extra | `f"{self.titulo} por {self.autor}"` | Formato incorrecto |

**Comentario docente:** Tuvo ej7 perfecto (10/10) pero **lo borró en un commit "fixed"**. Si el alumno puede recuperar ese archivo del historial, recupera +10 puntos → 57/70. Recomendable revisar git basics.

---

## 14. Agustin Aguero — 39/70

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Estructura** | Archivos `Ejercicio_01.py`, `Ejercicio_02.py`... con mayúscula y dos dígitos en vez de `ejercicio_x.py` | `ejercicio_1.py`, `ejercicio_2.py`... con guión bajo y un dígito | Naming incorrecto |
| **Ej1** | `print("Hola,", nombre)` con concatenación por coma en vez de f-string | `print(f"Hola, {nombre}")` | El enunciado pide explícitamente f-strings |
| **Ej3** | Bucle `for` con `.append()` | `[p.upper() for p in palabras]` en una línea | No entendió listas de comprensión |
| **Ej5** | Ruta hardcodeada de Windows: `C:\Users\Navegador\Downloads\estudiantes.csv` | `open("estudiantes.csv", ...)` (ruta relativa) | No portable, no funciona en otros entornos |
| **Ej8** | **No entregado** | Clase Libro | — |

**Comentario docente:** Errores conceptuales en f-strings y comprensión. No entregó ej8.

---

## 15. Federico Riquelme — 49/70

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Ej1** | Usó `.strip()` pero **omitió `.title()`** | `nombre.strip().title()` | El enunciado pide "Convertir la primera letra de cada palabra a mayúscula" |
| **Ej2** | `input()` **fuera del `while`**, `break` dentro del `except` (sale del bucle ante error) | `while True: try: edad = int(input(...))` con `continue` o nuevo `input` en except | Lógica invertida: sale ante error en vez de reintentar |
| **Ej7** | Verifica `len(sys.argv) < 3` y `> 3`, esperando 2 argumentos. El enunciado pide exactamente **1** argumento (total 2) | `if len(sys.argv) != 2: sys.exit(...)` | Cuenta mal los argumentos |

**Comentario docente:** Buenos ejercicios 3, 4, 5, 6 y 8. Errores conceptuales en ej1, ej2, ej7. No entregó ej9.

---

## 16. Nicolás Andrade — 24/70 ⚠️ CASO CRÍTICO

| Ejercicio | Error cometido | Cómo debería hacerlo | Comentario docente |
|-----------|----------------|----------------------|---------------------|
| **Ej1** | `split(" ")` + bucle `for` con `.capitalize()` que imprime cada palabra por separado | `nombre.strip().title()` y `print(f"Hola, {nombre}")` | Lógica rota, imprime "Tu nombre es X" / "Tu nombre es Y" separado |
| **Ej3** | Bucle `for` con `.append()` y `range(len(...))` | `[p.upper() for p in palabras]` | No entendió listas de comprensión |
| **Ej4** | `sorted(alumnos["nombre"])` — opera sobre la clave, no la lista de dicts | `sorted(alumnos, key=lambda x: x["nombre"])` | Código no ejecutable (TypeError) |
| **Ej5** | Mezcló código de **ej7** (sys.argv) con ej5. `for filas in file:` itera sobre el string (path), no el reader | `with open(file) as f: csv.DictReader(f)` separado de la lógica de sys.argv | Confusión grave entre ejercicios |
| **Ej6** | Usó `correo.split("@")` en vez de regex. Funcional pero no cumple "usar `re.search`" | `re.search(r"@uai\.edu\.ar$", correo)` | El enunciado pide explícitamente regex |
| **Ej7** | `if q >= 2:` (debería ser `== 2`). No usa `sys.exit()` | `if len(sys.argv) != 2: sys.exit("Error")` | Validación incorrecta: acepta múltiples argumentos |

**Comentario docente:** ⚠️ **Entregó los 7 archivos pero con errores graves en todos**. Conceptos no internalizados. Recomiendo repaso de:
- Strings: split vs strip vs title
- Listas de comprensión
- Lambda + sorted
- Regex vs manipulación de strings
- sys.argv

---

## Resumen de errores recurrentes (todos los alumnos)

| Error | Frecuencia | Ejercicios afectados |
|-------|------------|----------------------|
| No usar lista de comprensión | 5 alumnos | Ej3 |
| `__str__` con `print` en vez de `return` | 2 alumnos | Ej8 |
| Regex sin escapar puntos `\.` | 2 alumnos | Ej6 |
| `input()` fuera del `try` | 2 alumnos | Ej2 |
| `sys.argv` con condición incorrecta (`==` vs `>=` o `<`) | 2 alumnos | Ej7 |
| `.capitalize()` en vez de `.title()` | 2 alumnos | Ej1 |
| No usar f-string | 2 alumnos | Ej1 |
| Mensaje distinto al esperado | 4 alumnos | Varios |
| Estructura de archivos/carpeta incorrecta | 6 alumnos | General |

## Recomendaciones pedagógicas

1. **Reforzar listas de comprensión** — Es el error conceptual más recurrente (5 alumnos). Agregar ejercicios adicionales antes del parcial.
2. **`__str__` debe retornar, no imprimir** — Error conceptual de POO. Practicar con más ejemplos de métodos mágicos.
3. **Regex: escapar metacaracteres** — Hacer ejercicios específicos de regex antes del parcial.
4. **`try/except`: estructura completa** — Practicar el patrón `while True: try ... except ...` múltiples veces.
5. **Convenciones de naming** — Recordar al inicio: `snake_case`, guiones bajos, sin espacios, prefijos consistentes.
6. **f-strings vs concatenación** — Ejercicio específico solo de formato de strings.

---

*Documento generado por Hermes Agent. Detalles por alumno en `correcciones_nota/`.*