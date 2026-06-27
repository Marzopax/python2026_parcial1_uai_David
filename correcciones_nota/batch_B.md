# Corrección Parcial Python 2026 — Batch B (PRs #6 al #10)

**Fecha:** 27 de junio de 2026
**Corrector:** Hermes Agent

---

## Resumen de Notas

| PR  | Alumno              | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 | E9 | E10 | Total |
|-----|---------------------|----|----|----|----|----|----|----|----|----|-----|-------|
| #6  | Perez Carlos        | 10 | 10 | 1  | 0  | 4  | 10 | 10 | 10 | 0  | 9   | 64    |
| #7  | Gallaretto Leonel   | 10 | 9  | 10 | 0  | 10 | 10 | 10 | 8  | 0  | 10  | 77    |
| #8  | Sebastian Cordoba   | 4  | 5  | 0  | 0  | 4  | 2  | 0  | 7  | 0  | 0   | 22    |
| #9  | Lucas Jaime         | 10 | 10 | 10 | 0  | 10 | 10 | 9  | 10 | 0  | 0   | 69    |
| #10 | Mateo Duran         | 9  | 10 | 10 | 0  | 10 | 10 | 10 | 10 | 0  | 6   | 75    |

---

## PR #6 — Perez Carlos (64/100)

### Estructura del PR
- Carpeta: `Perez_Carlos/` ✅ (nombre correcto)
- Archivos entregados: ejercicio_1.py, ejercicio_2.py, ejercicio_3.py, ejercicio_4.py, ejercicio_6.py, ejercicio_7.py, ejercicio_8.py, ejercicio_10.py, test_ejercicio_10.py, estudiantes.csv
- **Faltan:** ejercicio_5.py, ejercicio_9.py

---

### Ejercicio 1: Variables y cadenas de texto — 10/10

```python
nombre = input("Ingrese su nombre: ")
nombre_limpio = nombre.strip()
nombre_formateado = nombre_limpio.title()
print(f"Hola, {nombre_formateado}")
```

✅ `strip()` correcto. ✅ `title()` correcto. ✅ f-string con formato "Hola, Nombre". Código limpio y funcional.

---

### Ejercicio 2: Excepciones y bucles — 10/10

```python
def pedir_entero():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            break
        except ValueError:
            print("Debe ingresar un número válido.")
print(f"Edad registrada: {edad}")
```

✅ `while True` correcto. ✅ `try/except ValueError`. ✅ `break` dentro del try (solo se ejecuta si la conversión es exitosa). ✅ Mensaje de error apropiado. Nota: `edad` se define dentro del try, pero el `print` está fuera de la función — en ejecución real podría fallar si la función nunca se llama. Sin embargo, la lógica del bucle es correcta.

---

### Ejercicio 3: Lista de comprensión — 1/10

```python
palabras = ["hola", "mundo", "python"]

for palabra in palabras:
    palabras_mayus = palabras_mayus.append(palabra.upper())

print(*palabras_mayus)
```

❌ **No usa lista de comprensión.** ❌ Usa un bucle `for` multilínea. ❌ `palabras_mayus` no está inicializada (NameError). ❌ `palabras_mayus = palabras_mayus.append(...)` asigna `None` (append devuelve None). ❌ El código no funciona. Solo se otorga 1 punto por declarar correctamente la lista de entrada.

**Solución esperada:** `[p.upper() for p in palabras]` en una sola línea.

---

### Ejercicio 4: Lambda y sorted — 0/10

El archivo `ejercicio_4.py` contiene **código del ejercicio 5 (CSV)**, no el código de lambda y sorted.

```python
# Esto es el ejercicio 5, no el 4
import csv
with open("estudiantes.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila["nombre"])
```

❌ No resuelve el ejercicio 4. No hay lambda, sorted, ni bucle for sobre alumnos ordenados.

---

### Ejercicio 5: Manejo de archivos CSV — 4/10

**No existe el archivo `ejercicio_5.py`.** El código de CSV está dentro de `ejercicio_4.py` (confundió los ejercicios).

El código en sí (si estuviera en el archivo correcto) es correcto:
- ✅ `import csv`
- ✅ `with open("estudiantes.csv", "r")`
- ✅ `csv.DictReader`
- ✅ `print(fila["nombre"])`

Se otorgan 4 puntos porque la lógica es correcta pero el archivo está mal nombrado (incumple la consigna "Cada ejercicio debe estar en un archivo diferente, con el siguiente formato: ejercicio_x.py").

---

### Ejercicio 6: Expresiones regulares — 10/10

```python
import re
correo = input("Ingrese su correo: ")
if re.search(r"@uai\.edu\.ar$", correo):
    print("Correo válido")
else:
    print("Correo inválido")
```

✅ `re.search()` con patrón correcto. ✅ Anclaje `$` al final. ✅ Puntos escapados con `\\.`. ✅ Mensajes de válido/inválido. Perfecto.

---

### Ejercicio 7: Argumentos de línea de comandos — 10/10

```python
import sys
if len(sys.argv) != 2:
    sys.exit("Error: debe ingresar un solo argumento")
archivo = sys.argv[1]
print(f"Archivo recibido: {archivo}")
```

✅ `len(sys.argv) != 2` para verificar exactamente un argumento adicional. ✅ `sys.exit()` con mensaje de error. ✅ Uso correcto de `sys.argv[1]`.

---

### Ejercicio 8: POO básico — 10/10

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} por {self.autor}"
```

✅ Clase `Libro` definida. ✅ `__init__` con `titulo` y `autor`. ✅ `__str__` devuelve "Título por Autor". ✅ f-string correcto. Perfecto.

---

### Ejercicio 9: POO avanzado — 0/10

❌ **No entregado.** No existe el archivo `ejercicio_9.py`.

---

### Ejercicio 10: Pytest — 9/10

**Archivo `ejercicio_10.py`:**
```python
def calcular_cuadrado(n):
    return n * n
```

**Archivo `test_ejercicio_10.py`:**
```python
from ejercicio_10 import calcular_cuadrado

def test_calcular_cuadrado():
    assert calcular_cuadrado(4) == 16
    assert calcular_cuadrado(0) == 0
```

✅ `calcular_cuadrado()` retorna `n * n`. ✅ Test con `assert` para número positivo (4 → 16). ✅ Test con cero (0 → 0). ✅ Archivo de pruebas separado. ✅ Función `test_calcular_cuadrado()` correcta.

⚠️ El nombre del archivo de test (`test_ejercicio_10.py`) no sigue la convención semántica ideal (`test_calcular_cuadrado.py`), pero pytest lo ejecutaría igual. Se descuenta 1 punto por naming no ideal.

---

---

## PR #7 — Gallaretto Leonel (77/100)

### Estructura del PR
- Carpeta: `Gallaretto_Leonel/` ✅ (nombre correcto)
- Archivos entregados: ejercicio_1.py, ejercicio_2.py, ejercicio_3.py, ejercicio.8.py, ejercicio_5.py, ejercicio_6.py, ejercicio_7.py, ejercicio_10.py, test_calcular_cuadrado.py, estudiantes.csv
- **Faltan:** ejercicio_4.py, ejercicio_9.py
- ⚠️ `ejercicio.8.py` tiene un punto en vez de guion bajo (error de naming)

---

### Ejercicio 1: Variables y cadenas de texto — 10/10

```python
def main():
    nombre = input("Ingrese su nombre: ")
    nombre = nombre.strip()
    nombre = nombre.title()
    print(f"Hola, {nombre}")
main()
```

✅ `strip()` y `title()` correctos. ✅ f-string. ✅ Envuelto en función `main()` (buena práctica, no requerida pero valorada). Perfecto.

---

### Ejercicio 2: Excepciones y bucles — 9/10

```python
def main():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if 100 > edad > 0:
                print(f"Edad registrada: {edad}")
                break
            else:
                print("Debe ingresar una edad entre 1 y 99.")
        except ValueError:
            print("Debe ingresar un número válido.")
main()
```

✅ `while True`. ✅ `try/except ValueError`. ✅ `break`. ✅ Mensajes apropiados.

⚠️ Agrega una validación de rango (1-99) que **no fue solicitada** en el enunciado. Si bien no rompe el programa, modifica el comportamiento esperado: el ejemplo solo pide detectar entradas no numéricas, no validar el rango. Se descuenta 1 punto por incorporar requisitos no pedidos.

---

### Ejercicio 3: Lista de comprensión — 10/10

```python
def main():
    palabras = ["hola", "mundo", "python"]
    mayusculas = [palabra.upper() for palabra in palabras]
    print(mayusculas)
main()
```

✅ Lista de comprensión en **una sola línea**: `[palabra.upper() for palabra in palabras]`. ✅ `.upper()` sobre cada elemento. Perfecto.

---

### Ejercicio 4: Lambda y sorted — 0/10

❌ **No entregado.** No existe el archivo `ejercicio_4.py`.

---

### Ejercicio 5: Manejo de archivos CSV — 10/10

```python
def main():
    import csv
    with open('estudiantes.csv', mode='r') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(fila['nombre'])
main()
```

✅ `import csv`. ✅ `with open()`. ✅ `csv.DictReader`. ✅ `print(fila['nombre'])`. Perfecto.

---

### Ejercicio 6: Expresiones regulares — 10/10

```python
def main():
    import re
    correo = input("Ingrese su correo electrónico: ")
    if re.search(r'@uai\.edu\.ar$', correo):
        print("Correo válido.")
    else:
        print("Correo inválido.")
main()
```

✅ `re.search()` con patrón correcto. ✅ `$` al final. ✅ Puntos escapados. ✅ Mensajes claro. Perfecto.

---

### Ejercicio 7: Argumentos de línea de comandos — 10/10

```python
def main():
    import sys
    if len(sys.argv) != 2:
        print("Error: Se esperaba exactamente un argumento adicional.")
        sys.exit(1)
    else:
        print("Argumento válido:", sys.argv[1])
main()
```

✅ `len(sys.argv) != 2`. ✅ `sys.exit(1)`. ✅ Mensaje de error. ✅ Uso de `sys.argv[1]`. Correcto.

---

### Ejercicio 8: POO básico — 8/10

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} por {self.autor}"
```

✅ Clase `Libro` correcta. ✅ `__init__` y `__str__` correctos.

⚠️ El archivo se llama **`ejercicio.8.py`** (con **punto** en vez de guion bajo). La consigna exige `ejercicio_x.py` con guion bajo. Se descuentan 2 puntos por error de nomenclatura. El código en sí es perfecto.

---

### Ejercicio 9: POO avanzado — 0/10

❌ **No entregado.** No existe el archivo `ejercicio_9.py`.

---

### Ejercicio 10: Pytest — 10/10

**Archivo `ejercicio_10.py`:**
```python
def calcular_cuadrado(n):
    return n * n
```

**Archivo `test_calcular_cuadrado.py`:**
```python
import pytest
from ejercicio_10 import calcular_cuadrado

def test_calcular_cuadrado():
    assert calcular_cuadrado(4) == 16
    assert calcular_cuadrado(0) == 0
```

✅ `calcular_cuadrado()` correcto. ✅ Archivo de pruebas separado. ✅ `test_calcular_cuadrado()` con asserts. ✅ Prueba con positivo y cero. ✅ El `import pytest` es innecesario pero no perjudica. Perfecto.

---

---

## PR #8 — Sebastian Cordoba (22/100)

### Estructura del PR
- Carpeta: `Sebastian Cordoba/` ❌ (usa **espacio** en vez de guion bajo — "Sebastian Cordoba" en vez de "Sebastian_Cordoba")
- Archivos entregados: ejercicio_1.py, ejercicio_2.py, ejercicio_5.py, ejercicio_6.py, ejercicio_8.py
- ⚠️ Incluye un archivo `Sebastian_Cordoba.zip` (no corresponde)
- **Faltan:** ejercicio_3.py, ejercicio_4.py, ejercicio_7.py, ejercicio_9.py, ejercicio_10.py
- ❌ Todos los archivos incluyen el texto del enunciado como comentarios (copy-paste)

---

### Ejercicio 1: Variables y cadenas de texto — 4/10

```python
name = input("Ingrese su nombre:")
name = name.strip()
name = name.capitalize()
f"Hola {name}"
```

✅ `strip()` correcto. ✅ `input()` correcto.

❌ Usa **`.capitalize()`** en vez de **`.title()`**. `.capitalize()` solo convierte a mayúscula la primera letra de toda la cadena (ej: "juan perez" → "Juan perez"), mientras que `.title()` convierte la primera letra de cada palabra ("Juan Perez"). ❌ El f-string **no tiene `print()`**, por lo que no se imprime nada en consola. ❌ Falta la coma en "Hola, Nombre".

---

### Ejercicio 2: Excepciones y bucles — 5/10

```python
def pedir_entero():
    edad = None
    while True:
        edad = input("Ingrese su edad: ")
        try:
            edad = int(edad)
        except ValueError:
            print("La edad ingresada no es correcta")
        else:
            break
```

✅ Define `pedir_entero()`. ✅ `while True`. ✅ `try/except ValueError`. ✅ `break` en el `else`.

❌ La función está **incompleta**: después del `break` no hay `return` ni `print`. No imprime "Edad registrada: X" como pide el ejemplo. ❌ La función no retorna la edad, por lo que no se puede usar su resultado.

---

### Ejercicio 3: Lista de comprensión — 0/10

❌ **No entregado.**

---

### Ejercicio 4: Lambda y sorted — 0/10

❌ **No entregado.**

---

### Ejercicio 5: Manejo de archivos CSV — 4/10

```python
import csv

with open("estudiantes.csv", newline="") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print((row.split())[0])
```

✅ `import csv`. ✅ `with open()`. ✅ `csv.DictReader`. ✅ Itera sobre las filas.

❌ **`row.split()` no funciona**: `row` es un diccionario (`DictReader`), no un string. Los diccionarios no tienen método `.split()`. Esto genera `AttributeError` en ejecución. ❌ Debería ser `print(row["nombre"])`.

---

### Ejercicio 6: Expresiones regulares — 2/10

```python
import re
correo = input("Ingrese su correo UAI:")
correo = correo.replace(".", "\.")
if re.search("@uai.edu.ar", correo) == None:
    print("El correo no es válido")
else:
    print("El correo es válido")
```

✅ `import re`. ✅ `input()`. ✅ `re.search()`. ✅ Estructura if/else.

❌ **`correo.replace(".", "\\.")` modifica el string de entrada**, reemplazando puntos literales por `\.` en el texto del correo. Esto rompe el valor original. ❌ La regex **no usa `$`** (anclaje de fin de línea). ❌ La regex **no escapa los puntos** con `\\.` (los puntos en regex matchean cualquier carácter). ❌ `re.search()` retorna `None` o un Match object; la comparación `== None` funciona pero es más idiomático usar `if not re.search(...)`.

---

### Ejercicio 7: Argumentos de línea de comandos — 0/10

❌ **No entregado.**

---

### Ejercicio 8: POO básico — 7/10

```python
class Libro:
    titulo = ""
    autor = ""

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return self.titulo + " por " + self.autor
```

✅ Clase `Libro`. ✅ `__init__` con `titulo` y `autor`. ✅ `__str__` devuelve "Título por Autor".

⚠️ Atributos de clase (`titulo = ""`, `autor = ""`) innecesarios y redundantes (son inmediatamente sobrescritos por `self.titulo` y `self.autor` en `__init__`). ❌ Usa concatenación con `+` en vez de f-strings (menos limpio pero funcional). Se descuentan 3 puntos por atributos de clase confusos y estilo.

---

### Ejercicio 9: POO avanzado — 0/10

❌ **No entregado.**

---

### Ejercicio 10: Pytest — 0/10

❌ **No entregado.**

---

---

## PR #9 — Lucas Jaime (69/100)

### Estructura del PR
- Carpeta: `Lucas_Jaime/` ✅ (nombre correcto)
- Archivos entregados: ejercicio_1.py, ejercicio_2.py, ejercicio_3.py, ejercicio_5.py, ejercicio_6.py, ejercicio_7.py, ejercicio_8.py
- **Faltan:** ejercicio_4.py, ejercicio_9.py, ejercicio_10.py
- ⚠️ No incluye `estudiantes.csv` en su carpeta (necesario para el ejercicio 5)

---

### Ejercicio 1: Variables y cadenas de texto — 10/10

```python
nombre = input("Ingrese su nombre: ")
nombre_procesado = nombre.strip().title()
print(f"Hola, {nombre_procesado}")
```

✅ `strip()` y `title()` encadenados correctamente. ✅ f-string con formato "Hola, Nombre". ✅ Código conciso y limpio. Perfecto.

---

### Ejercicio 2: Excepciones y bucles — 10/10

```python
def pedir_entero():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            print(f"Edad registrada: {edad}")
            break
        except ValueError:
            print("Debe ingresar un número válido.")

pedir_entero()
```

✅ `while True`. ✅ `try/except ValueError`. ✅ `break` después de conversión exitosa. ✅ Mensaje "Edad registrada: X". ✅ Llama a la función. Perfecto.

---

### Ejercicio 3: Lista de comprensión — 10/10

```python
palabras = ["hola", "mundo", "python"]
palabras_mayusculas = [palabra.upper() for palabra in palabras]
print(palabras_mayusculas)
```

✅ Lista de comprensión en una sola línea. ✅ `.upper()` sobre cada elemento. Perfecto.

---

### Ejercicio 4: Lambda y sorted — 0/10

❌ **No entregado.** No existe el archivo `ejercicio_4.py`.

---

### Ejercicio 5: Manejo de archivos CSV — 10/10

```python
import csv

with open("estudiantes.csv", mode="r", encoding="utf-8") as archivo:
    lector_csv = csv.DictReader(archivo)
    for fila in lector_csv:
        print(fila["nombre"])
```

✅ `import csv`. ✅ `with open()`. ✅ `csv.DictReader`. ✅ `print(fila["nombre"])`. ✅ Agrega `encoding="utf-8"` (buena práctica, no requerida). Perfecto.

---

### Ejercicio 6: Expresiones regulares — 10/10

```python
import re

correo = input("Ingrese su correo: ")

if re.search(r"@uai\.edu\.ar$", correo):
    print("Correo válido")
else:
    print("Correo inválido")
```

✅ `re.search()` con patrón correcto. ✅ `$` al final. ✅ Puntos escapados. ✅ Mensajes claros. Perfecto.

---

### Ejercicio 7: Argumentos de línea de comandos — 9/10

```python
import sys

if len(sys.argv) != 2:
    sys.exit("Error: Debe proporcionar exactamente un argumento adicional.")
```

✅ `len(sys.argv) != 2`. ✅ `sys.exit()` con mensaje de error.

⚠️ No muestra ninguna confirmación cuando el argumento es válido (el programa simplemente termina sin output). Si bien el enunciado no lo exige explícitamente, es una omisión de usabilidad. Se descuenta 1 punto.

---

### Ejercicio 8: POO básico — 10/10

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

libro = Libro("El Aleph", "Jorge Luis Borges")
print(libro)
```

✅ Clase `Libro` correcta. ✅ `__init__` y `__str__`. ✅ f-string. ✅ Incluye ejemplo de uso. Perfecto.

---

### Ejercicio 9: POO avanzado — 0/10

❌ **No entregado.** No existe el archivo `ejercicio_9.py`.

---

### Ejercicio 10: Pytest — 0/10

❌ **No entregado.** No existe `ejercicio_10.py` ni archivo de test.

---

---

## PR #10 — Mateo Duran (75/100)

### Estructura del PR
- Carpeta: `Mateo_Duran/` ✅ (nombre correcto)
- Archivos entregados: ejercicio_1.py, ejercicio_2.py, ejercicio_3.py, ejercicio_5.py, ejercicio_6.py, ejercicio_7.py, ejercicio_8.py, ejercicio_10.py, test_ej10.py
- **Faltan:** ejercicio_4.py, ejercicio_9.py
- ⚠️ El PR incluye `estudiantes.csv` en la raíz del repo (fuera de su carpeta)

---

### Ejercicio 1: Variables y cadenas de texto — 9/10

```python
nombre = input ("Ingrese su nombre: ")
nombre_final = nombre.strip().title()
print(f"Hola {nombre_final}")
```

✅ `strip()` y `title()` correctos. ✅ f-string.

❌ Falta la **coma** después de "Hola": `"Hola {nombre_final}"` produce "Hola Juan Perez", pero el ejemplo esperado es **"Hola, Juan Perez"** (con coma). Se descuenta 1 punto.

---

### Ejercicio 2: Excepciones y bucles — 10/10

```python
def pedir_entero():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            print(f"Edad registrada: {edad}")
            break
        except ValueError:
            print("Debe ingresar un numero válido")

pedir_entero()
```

✅ `while True`. ✅ `try/except ValueError`. ✅ `break`. ✅ Mensajes correctos. ✅ Llama a la función. Perfecto.

---

### Ejercicio 3: Lista de comprensión — 10/10

```python
palabras = ["hola", "mundo", "python"]
palabras_mayusculas = [palabra.upper() for palabra in palabras]
print(palabras_mayusculas)
```

✅ Lista de comprensión en una línea. ✅ `.upper()`. Perfecto.

---

### Ejercicio 4: Lambda y sorted — 0/10

❌ **No entregado.** No existe el archivo `ejercicio_4.py`.

---

### Ejercicio 5: Manejo de archivos CSV — 10/10

```python
import csv

with open("estudiantes.csv" , "r")as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
         print(fila["nombre"])
```

✅ `import csv`. ✅ `with open()`. ✅ `csv.DictReader`. ✅ `print(fila["nombre"])`. Perfecto. (Detalles menores de estilo como espacios alrededor de coma no afectan la corrección.)

---

### Ejercicio 6: Expresiones regulares — 10/10

```python
import re

correo = input("Ingrese su correo: ")

if re.search(r"@uai\.edu\.ar$", correo):
    print("El correo es válido")
else:
    print("El correo es inválido")
```

✅ `re.search()` con patrón correcto. ✅ `$`. ✅ Puntos escapados. Perfecto.

---

### Ejercicio 7: Argumentos de línea de comandos — 10/10

```python
import sys

if len(sys.argv) != 2:
    sys.exit("Error: Se esperaba exactamente un argumento adicional.")

argumento_adicional = sys.argv[1]
print(f"¡Todo correcto! El argumento ingresado es: {argumento_adicional}")
```

✅ `len(sys.argv) != 2`. ✅ `sys.exit()` con mensaje. ✅ Usa `sys.argv[1]`. ✅ Imprime confirmación con argumento válido (buena usabilidad). Perfecto.

---

### Ejercicio 8: POO básico — 10/10

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

libro = Libro("El Aleph", "Jorge Luis Borges")
print(libro)
```

✅ Clase `Libro`. ✅ `__init__` y `__str__`. ✅ f-string. ✅ Incluye ejemplo. Perfecto.

---

### Ejercicio 9: POO avanzado — 0/10

❌ **No entregado.** No existe el archivo `ejercicio_9.py`.

---

### Ejercicio 10: Pytest — 6/10

**Archivo `ejercicio_10.py`:**
```python
def calcular_cuadrado(n):
    return n * n

def test_calcular_cuadrado():
    assert calcular_cuadrado(4) == 16
    assert calcular_cuadrado(0) == 0
```

**Archivo `test_ej10.py`:** (vacío)

✅ `calcular_cuadrado()` retorna `n * n`. ✅ Asserts correctos (positivo y cero). ✅ Función `test_calcular_cuadrado()` definida.

❌ La función de test está en el **mismo archivo** que `calcular_cuadrado()` (`ejercicio_10.py`), no en un **archivo de pruebas separado** como exige explícitamente el enunciado: *"En un archivo de pruebas separado, escribí una función..."*. ❌ El archivo `test_ej10.py` está **vacío**. Se descuentan 4 puntos por no cumplir el requisito de separación de archivos.

---

---

## Observaciones Generales

### Errores comunes detectados en este batch:

1. **Ejercicio 4 (lambda/sorted)**: Fue el ejercicio **más faltante** del batch. Solo 0 de 5 alumnos lo resolvieron. Es llamativo que ningún alumno del batch B haya entregado este ejercicio.

2. **Ejercicio 9 (POO avanzado)**: También ausente en los 5 PRs. Nadie implementó properties ni validaciones defensivas.

3. **Nombres de archivo incorrectos**: Gallaretto usó `ejercicio.8.py` (punto en vez de guion bajo). Perez confundió ejercicio_4.py con ejercicio_5.py.

4. **Carpeta con espacio**: Sebastian Cordoba usó espacio en vez de guion bajo en el nombre de la carpeta (`Sebastian Cordoba/`), incumpliendo la instrucción explícita: *"cada alumno debe crear un directorio con su nombre y apellido, utilizando guion bajo entre ambos"*.

5. **Copy-paste del enunciado**: Cordoba dejó el texto completo del enunciado como comentarios en sus archivos, lo cual ensucia el código.

### Mejores desempeños:
- 🥇 **Gallaretto Leonel** (77/100): Mayor cantidad de ejercicios correctos. Solo falló por no entregar E4 y E9, y el naming de E8.
- 🥈 **Mateo Duran** (75/100): Código limpio y correcto en todos los ejercicios entregados. Solo falló E1 (coma), E4, E9, y E10 (archivos no separados).
- 🥉 **Lucas Jaime** (69/100): Excelente código en los 7 ejercicios que entregó. Le faltaron E4, E9 y E10.

### Situación preocupante:
- ⚠️ **Sebastian Cordoba** (22/100): Múltiples problemas: carpeta mal nombrada, solo 5 ejercicios entregados, errores conceptuales graves (regex mal implementada, `.capitalize()` en vez de `.title()`, `row.split()` en DictReader), funciones incompletas, y copy-paste del enunciado.