# Informe Ejecutivo — Parcial 1 Python 2026

**Materia:** Python  
**Profesor:** Alejandro Sartorio  
**Fecha de publicación:** 28/06/2026  
**Repositorio:** `cursos-uai/python2026_parcial1_uai`

---

## Introducción

¡Hola! Este informe contiene toda la información que necesitás sobre el **Parcial 1 de Python**. Está organizado en 8 secciones, pero **no tenés que leerlo todo**: solo lo que corresponda a tu situación. Te explico qué leer según tu caso:

- **Si tu nota es ≥ 6 (Base 10) o tu nota suma es ≥ 42/70:** Aprobaste el parcial. Leé la **Sección 1** para ver tu nota desglosada y los comentarios, y la **Sección 2** para conocer los errores más comunes de la clase (útil para no repetirlos en próximos parciales). **No debés hacer la actividad de recuperación.**
- **Si tu nota es < 6 (Base 10) o tu nota suma es < 42/70:** No aprobaste. Leé **todo el informe**, en especial:
  - **Sección 3** para confirmar tu condición.
  - **Sección 4** con las instrucciones generales de la actividad de recuperación.
  - **Sección 5** con el enunciado particular que armé para vos: te dice exactamente qué ejercicios rehacer, qué errores tuviste y cómo resolverlos.
  - **Sección 6** con el formato exacto que debe tener tu archivo `video_transcripcion.md`.
  - **Sección 7** con los pasos para armar el Pull Request de la entrega.

El objetivo de la recuperación es que demuestres que **entendiste los conceptos** que fallaron en el parcial: por eso la actividad pide un video explicativo y una transcripción, no solo el código. Si tenés dudas, contactame por los canales habituales.

---

## 1. Notas del parcial

Cada ejercicio obligatorio se califica de 0 a 10. La **nota final** es la suma de los 7 ejercicios obligatorios sobre un total de **70 puntos**. La columna **Base 10** es la nota equivalente en escala 0-10.

### 1.1 Notas y errores por alumno

| # | Alumno | Nota | Base 10 | Ej1 | Ej2 | Ej3 | Ej5 | Ej6 | Ej7 | Ej8 | Error principal |
|---|--------|------|---------|-----|-----|-----|-----|-----|-----|-----|------------------|
| 1 | Lucas Calvo Coltro | **70/70** | **10.0** | 10 | 10 | 10 | 10 | 10 | 10 | 10 | Archivos en raíz |
| 2 | Franco Terrazzino | **38/70** | **5.4** | 9 | 6 | 2 | 9 | 10 | 0 | 2 | Estructura, conceptual (ej3, ej8) |
| 3 | Fernando Almansa | **70/70** | **10.0** | 10 | 10 | 10 | 10 | 10 | 10 | 10 | CSV fuera del directorio |
| 4 | Mateo Dip | **68/70** | **9.7** | 10 | 9 | 10 | 10 | 9 | 10 | 10 | Mensajes distintos (ej2, ej6) |
| 5 | Ulises Sosa | **61/70** | **8.7** | 10 | 10 | 5 | 10 | 8 | 10 | 8 | Naming de archivos, detalles |
| 6 | Perez Carlos | **55/70** | **7.9** | 10 | 10 | 1 | 4 | 10 | 10 | 10 | Conceptual (ej3), confusión (ej4↔ej5) |
| 7 | Gallaretto Leonel | **67/70** | **9.6** | 10 | 9 | 10 | 10 | 10 | 10 | 8 | Naming (ej8), validación extra (ej2) |
| 8 | Sebastian Cordoba | **22/70** | **3.1** | 4 | 5 | 0 | 4 | 2 | 0 | 7 | Errores conceptuales múltiples |
| 9 | Lucas Jaime | **69/70** | **9.9** | 10 | 10 | 10 | 10 | 10 | 9 | 10 | Sin confirmación en ej7 |
| 10 | Mateo Duran | **69/70** | **9.9** | 9 | 10 | 10 | 10 | 10 | 10 | 10 | Falta coma en ej1 |
| 11 | Pares JuanCruz | **66/70** | **9.4** | 8 | 10 | 10 | 10 | 9 | 9 | 10 | Detalles en formato de salida |
| 12 | David Carletta | **3/70** | **0.4** | 2 | 1 | 0 | 0 | 0 | 0 | 0 | Errores conceptuales graves |
| 13 | Leandro Montenegro | **47/70** | **6.7** | 5 | 7 | 6 | 10 | 4 | 10 | 5 | Estructura, regex sin escapar |
| 14 | Agustin Aguero | **39/70** | **5.6** | 6 | 8 | 0 | 5 | 10 | 10 | 0 | Naming, lista de comprensión |
| 15 | Federico Riquelme | **49/70** | **7.0** | 5 | 2 | 10 | 10 | 10 | 2 | 10 | Conceptual (ej1, ej2, ej7) |
| 16 | Nicolás Andrade | **24/70** | **3.4** | 2 | 5 | 3 | 3 | 1 | 3 | 7 | Errores conceptuales múltiples |

### 1.2 Estadísticas generales

| Métrica | Valor |
|---------|-------|
| Promedio | **51.1 / 70** (7.3 / 10) |
| Mediana | **58.0 / 70** |
| Nota más alta | **70/70** (Calvo Coltro, Almansa) |
| Nota más baja | **3/70** (Carletta) |
| Aprobados (≥42/70 = 6/10) | **11 / 16** (69%) |
| Desaprobados (<42/70) | **5 / 16** (31%) |

---

## 2. Errores comunes de la clase

| # | Error | Frecuencia | Ejercicios |
|---|-------|------------|------------|
| 1 | No usar lista de comprensión (usar `for` + `.append()`) | 5 alumnos | Ej3 |
| 2 | Mensaje de salida distinto al esperado por el enunciado | 4 alumnos | Ej1, Ej2, Ej7 |
| 3 | `.capitalize()` en lugar de `.title()` | 2 alumnos | Ej1 |
| 4 | `print(...)` en vez de f-string | 2 alumnos | Ej1 |
| 5 | `input()` fuera del bloque `try` | 2 alumnos | Ej2 |
| 6 | `break` dentro del `except` (sale en lugar de reintentar) | 1 alumno | Ej2 |
| 7 | Regex sin escapar los puntos `\.` | 2 alumnos | Ej6 |
| 8 | No usar `re.search()` cuando se pide regex | 1 alumno | Ej6 |
| 9 | `sys.argv` con condición incorrecta (`>=` o `<` en lugar de `==`) | 2 alumnos | Ej7 |
| 10 | `__str__` con `print()` en vez de `return` | 2 alumnos | Ej8 |
| 11 | `DictReader` mal usado (`row.split()` sobre dict, etc.) | 2 alumnos | Ej5 |
| 12 | Estructura de archivos incorrecta (nombres, mayúsculas, dos dígitos) | 5 alumnos | General |
| 13 | Confundir ejercicios entre sí (ej4 con ej5, ej5 con ej7) | 2 alumnos | Ej4, Ej5, Ej7 |
| 14 | Ruta absoluta hardcodeada (`C:\Users\...`) | 1 alumno | Ej5 |

---

## 3. Alumnos que deben recuperar (nota menor a 6 base 10)

Los siguientes **5 alumnos** no alcanzaron el mínimo de 6/10 y deben realizar la actividad de recuperación:

| # | Alumno | Nota | Base 10 | Estado |
|---|--------|------|---------|--------|
| 12 | David Carletta | 3/70 | **0.4** | ⚠️ Recuperación obligatoria |
| 8 | Sebastian Cordoba | 22/70 | **3.1** | ⚠️ Recuperación obligatoria |
| 16 | Nicolás Andrade | 24/70 | **3.4** | ⚠️ Recuperación obligatoria |
| 2 | Franco Terrazzino | 38/70 | **5.4** | ⚠️ Recuperación obligatoria |
| 14 | Agustin Aguero | 39/70 | **5.6** | ⚠️ Recuperación obligatoria |

Los 11 alumnos restantes (**Calvo Coltro, Almansa, Dip, Sosa, Perez, Gallaretto, Jaime, Duran, Pares, Montenegro, Riquelme**) **aprueban el parcial** y no deben hacer la actividad.

---

## 4. Actividad de recuperación — Instrucciones generales

Para los 5 alumnos que no aprobaron:

### ¿Qué tienen que hacer?

1. **Resolver nuevamente los ejercicios que les salieron mal** (ver enunciado particular en la sección 5).
2. **Grabar un video** de entre 5 y 15 minutos donde expliquen:
   - Por qué la versión original estaba mal (qué concepto no entendieron).
   - Cómo resolvieron la nueva versión paso a paso.
   - Cualquier duda que les haya surgido.
3. **Hacer un nuevo Pull Request** al repositorio `cursos-uai/python2026_parcial1_uai` desde su fork, con:
   - Los ejercicios corregidos en sus archivos correspondientes (`ejercicio_X.py` con guión bajo y minúscula).
   - Un archivo llamado **`video_transcripcion.md`** dentro de su carpeta que contenga:
     - Link al video (YouTube, Drive, Loom, etc. — debe ser accesible sin login).
     - Transcripción completa del video (lo que dijeron, escrito).
     - Fecha de grabación.
4. **Plazo de entrega:** [FECHA A DEFINIR POR EL DOCENTE]

### Criterios de aprobación de la recuperación

- La nueva versión de los ejercicios debe **funcionar correctamente** (ejecutable sin errores).
- El video debe **explicar los conceptos** correctamente (no solo leer el código).
- La transcripción debe estar **completa y ser coherente** con el video.
- Se valorará que el alumno demuestre comprensión, no solo que el código funcione.

### Nota máxima de la recuperación

La nota final del parcial, con la recuperación aprobada, será **6/10 (42/70)**. Esto es así para todos los casos: la recuperación permite **aprobar** pero no mejora la nota por encima del mínimo.

---

## 5. Enunciados particulares por alumno

A continuación el detalle específico de qué debe rehacer cada alumno.

---

### 5.1 David Carletta — Enunciado particular

**Tu nota fue 3/70 (0.4).** Tuviste errores conceptuales graves en 5 de los 7 ejercicios obligatorios. Esta es tu oportunidad de demostrar que ahora los entendés.

#### Ejercicios a rehacer (TODOS los obligatorios)

| Ej | Tu error | Lo que debés resolver |
|----|----------|------------------------|
| **Ej1** | Usaste `.capitalize()` (solo primera letra), pediste nombre + apellido, concatenación en vez de f-string | Pedí solo el nombre, usá `.title()`, imprimí con f-string: `Hola, Juan Perez` |
| **Ej2** | `input()` estaba **fuera** del `try`, no detectaba texto | El `try` debe envolver al `int(input(...))` y volver a pedir hasta que sea válido |
| **Ej3** | Usaste bucle `for` con `.append()` | Una sola línea con lista de comprensión: `[p.upper() for p in palabras]` |
| **Ej5** | `csv.DictReader("nombre")` mal usado, `open(estudiantes.csv)` sin comillas | `with open("estudiantes.csv") as f:` + `csv.DictReader(f)` + `print(row["nombre"])` |
| **Ej6** | **No entregado** | `re.search(r"@uai\.edu\.ar$", correo)` con `\.` escapados y `$` |
| **Ej7** | `if (sys.argv) == 1:` compara lista con int | `if len(sys.argv) != 2: sys.exit("Error")` + usar `sys.argv[1]` |
| **Ej8** | **No entregado** | Clase `Libro` con `__init__(self, titulo, autor)` y `__str__` que **retorne** `f"{titulo} por {autor}"` |

**Pista:** Estudiá especialmente la diferencia entre `.capitalize()` y `.title()`. La primera convierte solo la primera letra de toda la cadena; la segunda convierte la primera letra de **cada palabra**.

---

### 5.2 Sebastian Cordoba — Enunciado particular

**Tu nota fue 22/70 (3.1).** Solo entregaste 5 de los 7 ejercicios obligatorios y los que entregaste tenían errores conceptuales serios.

#### Ejercicios a rehacer

| Ej | Tu error | Lo que debés resolver |
|----|----------|------------------------|
| **Ej1** | Usaste `.capitalize()`, no usaste `print()`, faltó coma | `nombre.strip().title()` + `print(f"Hola, {nombre}")` con coma |
| **Ej3** | **No entregado** | `[p.upper() for p in palabras]` en una línea |
| **Ej5** | `row.split()` sobre DictReader (row es dict, no string) | `print(row["nombre"])` directo, sin split |
| **Ej6** | Regex sin `$` ni `\.`, además modificaba el input con `.replace()` | `re.search(r"@uai\.edu\.ar$", correo)` — **sin modificar el input** |
| **Ej7** | **No entregado** | `len(sys.argv) != 2` + `sys.exit("Error")` |

#### Recordatorio de estructura

- Tu carpeta debe llamarse `Sebastian_Cordoba/` (con guión bajo, **sin espacio**).
- Los archivos son `ejercicio_1.py`, `ejercicio_2.py`, etc. (con guión bajo).
- **Eliminá los comentarios con el enunciado** que pegaste en todos tus archivos.

---

### 5.3 Nicolás Andrade — Enunciado particular

**Tu nota fue 24/70 (3.4).** Entregaste los 7 archivos, pero todos tenían errores conceptuales. Esto sugiere que **entendiste la estructura** (cómo entregar) pero **no los conceptos**. La recuperación es importante para cimentar las bases.

#### Ejercicios a rehacer (TODOS los obligatorios)

| Ej | Tu error | Lo que debés resolver |
|----|----------|------------------------|
| **Ej1** | `split(" ")` + bucle con `.capitalize()` imprime cada palabra separada | Una sola línea: `print(f"Hola, {input('Nombre: ').strip().title()}")` |
| **Ej3** | Bucle `for` con `.append()` y `range(len(...))` | `[p.upper() for p in palabras]` en una línea |
| **Ej4** | `sorted(alumnos["nombre"])` opera sobre la clave, no la lista | `sorted(alumnos, key=lambda x: x["nombre"])` |
| **Ej5** | Mezclaste lógica de ej7 con ej5. `for filas in file:` itera sobre el string path | `ejercicio_5.py` debe tener **solo** el código de CSV, sin sys.argv |
| **Ej6** | Usaste `correo.split("@")` en vez de regex | `re.search(r"@uai\.edu\.ar$", correo)` con regex |
| **Ej7** | `if q >= 2:` permite más argumentos. No usaste `sys.exit()` | `if len(sys.argv) != 2: sys.exit("Error")` |
| **Ej8** | `__str__` agrega prefijo "El" | `return f"{self.titulo} por {self.autor}"` (sin "El") |

**Pista importante:** El enunciado de **cada ejercicio** está en el archivo `Enunciado_Parcial_1.md` del repo. Releelo con atención antes de resolver cada uno. Tu confusión entre ej5 y ej7 sugiere que no leíste bien los enunciados por separado.

---

### 5.4 Franco Terrazzino — Enunciado particular

**Tu nota fue 38/70 (5.4).** Estuviste muy cerca del 6. Solo necesitás corregir 3 ejercicios y la estructura.

#### Ejercicios a rehacer

| Ej | Tu error | Lo que debés resolver |
|----|----------|------------------------|
| **Estructura** | Usaste subdirectorios `EJERCICIO 1/` y nombres `ejercicio1.py` (sin guión bajo) | Todo en una carpeta `Franco_Terrazzino/` con archivos `ejercicio_1.py`, `ejercicio_2.py`, etc. |
| **Ej3** | Usaste bucle `for` con `.append()` + función externa | `[p.upper() for p in palabras]` en una sola línea |
| **Ej7** | **No entregado** | `if len(sys.argv) != 2: sys.exit("Error")` |
| **Ej8** | `__str__` con `print()` en vez de `return` | `return f"{self.titulo} por {self.autor}"` |

**Pista:** Tu código de ej1, ej2, ej5 y ej6 es muy bueno. Reentregá esos sin cambios y agregá solo lo que falta.

---

### 5.5 Agustin Aguero — Enunciado particular

**Tu nota fue 39/70 (5.6).** Muy cerca del 6. Necesitás corregir 4 ejercicios y el naming.

#### Ejercicios a rehacer

| Ej | Tu error | Lo que debés resolver |
|----|----------|------------------------|
| **Estructura** | `Ejercicio_01.py` con mayúscula y dos dígitos | `ejercicio_1.py` con minúscula, guión bajo y un dígito |
| **Ej1** | `print("Hola,", nombre)` con concatenación por coma | `print(f"Hola, {nombre}")` con f-string |
| **Ej3** | Bucle `for` con `.append()` | `[p.upper() for p in palabras]` en una línea |
| **Ej5** | Ruta hardcodeada de Windows: `C:\Users\Navegador\Downloads\estudiantes.csv` | `open("estudiantes.csv", ...)` ruta relativa |
| **Ej8** | **No entregado** | Clase `Libro` con `__init__` y `__str__` que retorne `f"{titulo} por {autor}"` |

**Pista:** Tu código de ej2, ej6 y ej7 es muy bueno. Reentregá esos sin cambios.

---

## 6. Formato del archivo `video_transcripcion.md`

Dentro de la carpeta del alumno (ej: `David_Carletta/video_transcripcion.md`), el archivo debe verse así:

```markdown
# Video de recuperación — [Nombre Apellido]

**Fecha:** [DD/MM/AAAA]  
**Link al video:** [URL accesible, ej: https://youtu.be/...]  
**Duración:** [X minutos]

---

## Transcripción

[Escribir textualmente lo que se dice en el video. Puede ser literal o un resumen
pormenorizado. Mínimo 500 palabras.]

**Ejemplo de inicio:**

"En este video voy a explicar cómo resolví nuevamente el Ejercicio 3 del parcial.
La primera vez lo hice con un bucle for tradicional..."

[Continuar con la explicación de cada ejercicio que se reentrega.]
```

---

## 7. Pasos para hacer el Pull Request de recuperación

1. **Forkear** el repositorio (si ya lo tenés forkado, saltá este paso).
2. **Crear una rama nueva** en tu fork: `git checkout -b recuperacion-parcial1`
3. **Modificar/crear los archivos** correspondientes en tu carpeta personal.
4. **Crear el archivo `video_transcripcion.md`** con la estructura de la sección 6.
5. **Commit** con mensaje descriptivo: `git commit -m "Recuperación Parcial 1"`
6. **Push** a tu fork: `git push origin recuperacion-parcial1`
7. **Abrir Pull Request** desde GitHub apuntando a `cursos-uai/python2026_parcial1_uai`, rama `main`. Título sugerido: `Recuperación Parcial 1 — [Nombre Apellido]`.

---

## 8. Consultas

Cualquier duda sobre la corrección, los errores específicos o la actividad de recuperación, contactarme por los canales habituales.

Saludos,  
**Prof. Alejandro Sartorio**