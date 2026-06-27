# Corrección Parcial Python 2026 — Batch A (PRs 1-5)

---

## Alumno: Lucas Calvo Coltro (PR #1)

### Resumen
| Ej | Tema | Nota |
|---|---|---|
| 1 | Cadenas (input, strip, title, f-string) | 10 |
| 2 | Excepciones (while True, try/except, pedir_entero) | 10 |
| 3 | Lista de comprensión | 10 |
| 4 | Lambda y sorted | 10 |
| 5 | CSV con DictReader | 10 |
| 6 | Regex (re.search, anclaje $) | 10 |
| 7 | sys.argv | 10 |
| 8 | POO básico (Libro, __init__, __str__) | 10 |
| 9 | POO avanzado (@property, setter, validación) | 0 |
| 10 | Pytest (test_calcular_cuadrado) | 9 |
| **TOTAL** | | **89/100** |

### Corrección detallada

**Error de estructura:** Los archivos están en la raíz del repositorio, no dentro de un subdirectorio `Nombre_Apellido/` como exige el enunciado. Penalización reflejada en el contexto general, no descuenta puntos por ejercicio individual.

**Ejercicio 1 (10/10):** ✅ Perfecto. Usa `input()`, `.strip()`, `.title()` y `f-string` correctamente.
```python
# Entregado (correcto):
nombre_ingresado = input("Ingrese su nombre: ")
nombre_limpio = nombre_ingresado.strip().title()
print(f"Hola, {nombre_limpio}")
```

**Ejercicio 2 (10/10):** ✅ Perfecto. Implementa `pedir_entero()` con `while True`, `try/except ValueError`, y usa `return` para salir del bucle.
```python
# Entregado (correcto):
def pedir_entero():
    while True:
        try:
            edad = input("Ingrese su edad: ")
            edad_entera = int(edad)
            print(f"Edad registrada: {edad_entera}")
            return edad_entera
        except ValueError:
            print("Debe ingresar un número válido.")
```

**Ejercicio 3 (10/10):** ✅ Perfecto. Lista de comprensión en una sola línea con `.upper()`.
```python
mayusculas = [palabra.upper() for palabra in palabras]
```

**Ejercicio 4 (10/10):** ✅ Perfecto. `for`, `sorted()` y `lambda` en una sola construcción.
```python
for alumno in sorted(alumnos, key=lambda x: x["nombre"]):
     print(alumno["nombre"])
```

**Ejercicio 5 (10/10):** ✅ Perfecto. `with open`, `csv.DictReader`, imprime columna `"nombre"`.
```python
with open("estudiantes.csv") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila["nombre"])
```

**Ejercicio 6 (10/10):** ✅ Perfecto. `re.search()` con `@uai\.edu\.ar$`, escapes y anclaje correctos.

**Ejercicio 7 (10/10):** ✅ Perfecto. Verifica `len(sys.argv) != 2`, usa `sys.exit()`.

**Ejercicio 8 (10/10):** ✅ Perfecto. Clase `Libro` con `__init__`, atributos `titulo` y `autor`, y `__str__` que devuelve `"Título por Autor"`.

**Ejercicio 9 (0/10):** ❌ No entregado. Falta el archivo `ejercicio_9.py`.

**Ejercicio 10 (9/10):** ✅ Código correcto pero con detalles menores. La función `test_calcular_cuadrado()` tiene 3 asserts correctos. El archivo `maths.py` contiene `calcular_cuadrado()`. Sin embargo, incluye `import pytest` (innecesario), un `print()` y una llamada manual a `test_calcular_cuadrado()`, lo cual no es idiomático para pytest (que descubre y ejecuta los tests automáticamente). No rompe nada, pero no es la práctica esperada.

---

## Alumno: Franco Terrazzino (PR #2)

### Resumen
| Ej | Tema | Nota |
|---|---|---|
| 1 | Cadenas (input, strip, title, f-string) | 9 |
| 2 | Excepciones (while True, try/except, pedir_entero) | 4 |
| 3 | Lista de comprensión | 2 |
| 4 | Lambda y sorted | 0 |
| 5 | CSV con DictReader | 9 |
| 6 | Regex (re.search, anclaje $) | 10 |
| 7 | sys.argv | 0 |
| 8 | POO básico (Libro, __init__, __str__) | 2 |
| 9 | POO avanzado (@property, setter, validación) | 0 |
| 10 | Pytest (test_calcular_cuadrado) | 0 |
| **TOTAL** | | **36/100** |

### Corrección detallada

**Error de estructura:** Los archivos están en subdirectorios `EJERCICIO 1/`, `EJERCICIO 2/`, etc. en lugar de un único directorio `Nombre_Apellido/`. Además los archivos se llaman `ejercicio1.py` (sin guion bajo) en vez de `ejercicio_1.py`. Doble error de estructura.

**Ejercicios no entregados:** 4, 7, 9, 10 (4 de 10 ejercicios ausentes).

**Ejercicio 1 (9/10):** ✅ Funcionalmente correcto: `input()`, `.strip()`, `.title()`, `f-string`. Pero envuelve todo en funciones con `main()` y `if __name__ == "__main__"`, lo cual es sobre-ingeniería para un ejercicio simple de 3 líneas. El nombre de función `IngresarNombre` usa PascalCase en vez de snake_case (convención Python).
```python
def IngresarNombre():
    nombre = input("Ingrese su nombre: ").strip().title()
    print(f"Hola, {nombre}")
```

**Ejercicio 2 (4/10):** 🔴 Errores significativos:
1. La función se llama `IngresarEdad` en vez de `pedir_entero` como exige el enunciado.
2. No usa `while True` literalmente (usa `while condicion` con variable booleana).
3. El mensaje de salida es `"Su edad es {edad} años"` en vez de `"Edad registrada: {edad}"`.
4. El mensaje de error es `"El valor ingresado debe ser numerico"` (sin tilde) en vez de `"Debe ingresar un número válido."`.

El esqueleto try/except/break es correcto, pero los desvíos del enunciado son múltiples.

**Ejercicio 3 (2/10):** 🔴 Error conceptual grave. El enunciado pide explícitamente: *"Creá una nueva lista en una sola línea utilizando una lista de comprensión"*. El alumno usó un bucle `for` tradicional con `.append()`, lo cual no cumple el requisito fundamental del ejercicio.
```python
# Entregado (incorrecto — no es lista de comprensión):
def convertirMayusculas(lista):
    nueva_lista = []
    for i in lista:
        nueva_lista.append(str(i).upper())
    return nueva_lista

# Esperado:
mayusculas = [palabra.upper() for palabra in palabras]
```

**Ejercicio 4 (0/10):** ❌ No entregado.

**Ejercicio 5 (9/10):** ✅ Código correcto: `with open`, `csv.DictReader`, imprime `line['nombre']`. Sin embargo, no incluye el archivo `estudiantes.csv` en el PR, por lo que el código fallaría en ejecución real. La lógica de Python es correcta.

**Ejercicio 6 (10/10):** ✅ Perfecto. `re.search()` con patrón `r"@uai\.edu\.ar$"`, escapes y anclaje correctos.

**Ejercicio 7 (0/10):** ❌ No entregado.

**Ejercicio 8 (2/10):** 🔴 Error conceptual grave. El método `__str__` **debe retornar** un string, pero el alumno lo implementó con `print()`. Esto rompe el contrato de `__str__`: cuando Python llama a `print(libro)`, espera que `__str__` devuelva un string, pero al tener `print()` adentro y no `return`, retorna `None` implícitamente. Además, nunca se llama a `print(libro)`, se llama manualmente a `libro.__str__()` lo cual es incorrecto.
```python
# Entregado (incorrecto):
def __str__(self):
    print(f'{self.titulo} por {self.autor}')  # ❌ print en vez de return

# Esperado:
def __str__(self):
    return f"{self.titulo} por {self.autor}"  # ✅ return
```

**Ejercicio 9 (0/10):** ❌ No entregado.

**Ejercicio 10 (0/10):** ❌ No entregado.

---

## Alumno: Fernando Almansa (PR #3)

### Resumen
| Ej | Tema | Nota |
|---|---|---|
| 1 | Cadenas (input, strip, title, f-string) | 10 |
| 2 | Excepciones (while True, try/except, pedir_entero) | 10 |
| 3 | Lista de comprensión | 10 |
| 4 | Lambda y sorted | 0 |
| 5 | CSV con DictReader | 10 |
| 6 | Regex (re.search, anclaje $) | 10 |
| 7 | sys.argv | 10 |
| 8 | POO básico (Libro, __init__, __str__) | 10 |
| 9 | POO avanzado (@property, setter, validación) | 0 |
| 10 | Pytest (test_calcular_cuadrado) | 10 |
| **TOTAL** | | **80/100** |

### Corrección detallada

**Estructura:** ✅ Correcta. Directorio `Fernando_Almansa/` con archivos `ejercicio_x.py`. El archivo `estudiantes.csv` está en la raíz en vez de dentro del directorio (error menor de estructura).

**Ejercicios no entregados:** 4, 9.

**Ejercicio 1 (10/10):** ✅ Perfecto. Conciso y correcto.
```python
nombre = input("Ingrese su nombre: ").strip().title()
print(f"Hola, {nombre}")
```

**Ejercicio 2 (10/10):** ✅ Perfecto. `pedir_entero()` con `while True`, `try/except ValueError`, `return` para salir. Mensajes correctos.
```python
def pedir_entero():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            return edad
        except ValueError:
            print("Debe ingresar un número válido.")
```

**Ejercicio 3 (10/10):** ✅ Perfecto. Lista de comprensión en una línea con `.upper()`.

**Ejercicio 4 (0/10):** ❌ No entregado.

**Ejercicio 5 (10/10):** ✅ Perfecto. `with open`, `csv.DictReader`, imprime `fila["nombre"]`.

**Ejercicio 6 (10/10):** ✅ Perfecto. `re.search(r"@uai\.edu\.ar$", correo)` con escapes y anclaje correctos.

**Ejercicio 7 (10/10):** ✅ Perfecto. Verifica `len(sys.argv) != 2` y usa `sys.exit()` con mensaje.

**Ejercicio 8 (10/10):** ✅ Perfecto. Clase `Libro` con `__init__`, atributos, y `__str__` con return.
```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def __str__(self):
        return f"{self.titulo} por {self.autor}"
```

**Ejercicio 9 (0/10):** ❌ No entregado.

**Ejercicio 10 (10/10):** ✅ Perfecto. `calcular_cuadrado()` en `calculadora.py` y `test_calcular_cuadrado()` en `ejercicio_10.py` con dos asserts (positivo y cero). Archivos separados como pide el enunciado.

---

## Alumno: Mateo Dip (PR #4)

### Resumen
| Ej | Tema | Nota |
|---|---|---|
| 1 | Cadenas (input, strip, title, f-string) | 10 |
| 2 | Excepciones (while True, try/except, pedir_entero) | 9 |
| 3 | Lista de comprensión | 10 |
| 4 | Lambda y sorted | 0 |
| 5 | CSV con DictReader | 10 |
| 6 | Regex (re.search, anclaje $) | 9 |
| 7 | sys.argv | 10 |
| 8 | POO básico (Libro, __init__, __str__) | 10 |
| 9 | POO avanzado (@property, setter, validación) | 0 |
| 10 | Pytest (test_calcular_cuadrado) | 10 |
| **TOTAL** | | **78/100** |

### Corrección detallada

**Estructura:** ✅ Correcta. Directorio `Mateo_Dip/` con archivos `ejercicio_x.py`. El archivo `estudiantes.csv` está en la raíz en vez de dentro del directorio (error menor). El CSV tiene espacios después de las comas (`nombre, casa`), lo cual es inusual pero el código lo maneja correctamente.

**Ejercicios no entregados:** 4, 9.

**Ejercicio 1 (10/10):** ✅ Perfecto.
```python
nombre = input("Ingrese su nombre: ").strip().title()
print(f"Hola, {nombre}")
```

**Ejercicio 2 (9/10):** ✅ Código correcto en lógica: `while True`, `try/except ValueError`, `return`. Pero tiene detalles: escribe `"numero"` sin tilde y deja un espacio extra al final del mensaje (`"Debe ingresar un numero valido. "`).

**Ejercicio 3 (10/10):** ✅ Perfecto. Usa `p.upper()` con nombres cortos de variable, perfectamente válido.
```python
mayusculas = [p.upper() for p in palabras]
```

**Ejercicio 4 (0/10):** ❌ No entregado.

**Ejercicio 5 (10/10):** ✅ Perfecto. `with open`, `csv.DictReader`, imprime `fila["nombre"]`.

**Ejercicio 6 (9/10):** ✅ Regex correcto: `re.search(r"@uai\.edu\.ar$", correo)`. Pero tiene un typo: `"Correco incorrecto."` en vez de `"Correo incorrecto."`.

**Ejercicio 7 (10/10):** ✅ Correcto. Verifica `len(sys.argv) != 2` y usa `sys.exit()`. Usa `print()` con coma en vez de f-string, pero es válido.

**Ejercicio 8 (10/10):** ✅ Perfecto. Clase `Libro` con `__init__`, `__str__` con return correcto.

**Ejercicio 9 (0/10):** ❌ No entregado.

**Ejercicio 10 (10/10):** ✅ Perfecto. `calcular_cuadrado()` en `programa.py` y `test_calcular_cuadrado()` en `ejercicio_10.py` con dos asserts. Archivos separados correctamente.

---

## Alumno: Ulises Sosa (PR #5)

### Resumen
| Ej | Tema | Nota |
|---|---|---|
| 1 | Cadenas (input, strip, title, f-string) | 0 |
| 2 | Excepciones (while True, try/except, pedir_entero) | 0 |
| 3 | Lista de comprensión | 0 |
| 4 | Lambda y sorted | 0 |
| 5 | CSV con DictReader | 0 |
| 6 | Regex (re.search, anclaje $) | 0 |
| 7 | sys.argv | 0 |
| 8 | POO básico (Libro, __init__, __str__) | 0 |
| 9 | POO avanzado (@property, setter, validación) | 0 |
| 10 | Pytest (test_calcular_cuadrado) | 6 |
| **TOTAL** | | **6/100** |

### Corrección detallada

**Error de estructura:** Si bien tiene el directorio `Ulises_Sosa/`, el archivo se llama `problema10.py` en vez de `ejercicio_10.py`, incumpliendo el formato requerido.

**Ejercicios 1-9 (0/10 cada uno):** ❌ No entregados. Solo entregó el ejercicio 10.

**Ejercicio 10 (6/10):** 🔴 Parcialmente correcto pero con errores significativos:
1. **Error de estructura:** Ambas funciones (`calcular_cuadrado` y `test_calcular_cuadrado`) están en el mismo archivo. El enunciado pide explícitamente *"En un archivo de pruebas separado"*.
2. **Error de nombrado:** El archivo se llama `problema10.py` en vez de `ejercicio_10.py`.
3. ✅ La lógica de las funciones es correcta: `calcular_cuadrado(n)` retorna `n * n` y `test_calcular_cuadrado()` tiene 3 asserts válidos (positivo, negativo, cero).
```python
# Entregado (ambas funciones en mismo archivo — error):
def calcular_cuadrado(n):
    return n * n

def test_calcular_cuadrado():
    assert calcular_cuadrado(2) == 4
    assert calcular_cuadrado(-2) == 4
    assert calcular_cuadrado(0) == 0
```

---

## Resumen del batch

| # | Alumno | Total | Estructura | Entregados |
|---|---|---|---|---|
| 1 | Lucas Calvo Coltro | 89/100 | ❌ Archivos en raíz | 9/10 (falta ej 9) |
| 2 | Franco Terrazzino | 36/100 | ❌ Subdirectorios por ejercicio + nombres incorrectos | 6/10 (faltan 4,7,9,10) |
| 3 | Fernando Almansa | 80/100 | ✅ Correcta | 8/10 (faltan 4,9) |
| 4 | Mateo Dip | 78/100 | ✅ Correcta | 8/10 (faltan 4,9) |
| 5 | Ulises Sosa | 6/100 | ❌ Nombre de archivo incorrecto | 1/10 (solo ej 10) |

**Error más común:** Los ejercicios 4 (lambda/sorted) y 9 (POO avanzado) fueron los más omitidos. El ejercicio 9 requería resolverse primero en papel, lo que probablemente contribuyó a su baja tasa de entrega.