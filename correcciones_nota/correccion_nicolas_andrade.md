# Corrección — Parcial 1 de Python (2026)

**Repositorio:** `cursos-uai/python2026_parcial1_uai`
**PR:** #16 — `nicolasandradedesarrollosit`
**Alumno:** Nicolás Andrade
**Fecha de corrección:** 27/06/2026

---

## Resumen

| Ejercicio | Tema | Nota |
|---|---|---|
| 1 | Variables y cadenas | 2/10 |
| 2 | Excepciones y bucles | 5/10 |
| 3 | Listas de comprensión | 3/10 |
| 4 | Lambda y sorted | 1/10 |
| 5 | Archivos CSV | 1/10 |
| 6 | Expresiones regulares | 1/10 |
| 7 | Argumentos de línea de comandos | 3/10 |
| 8 | POO — clase Libro | 7/10 |
| 9 | POO — encapsulamiento | 0/10 |
| 10 | Pytest | 2/10 |
| **TOTAL** | | **25/100** |

---

## Corrección detallada

### Ejercicio 1 — Variables y cadenas de texto (2/10)

**Requisito:** Solicitar nombre, limpiar espacios, capitalizar cada palabra, imprimir `Hola, Nombre Apellido` con f-string.

**Errores:**
- ❌ **Formato de salida incorrecto.** El enunciado pide `Hola, Juan Perez`. El alumno imprime `Tu nombre es Juan` y luego `Tu nombre es Perez` (una línea por palabra).
- ❌ **Divide el nombre por espacios** y procesa cada palabra por separado. El enunciado pide procesar la cadena completa.
- ❌ Usa `.capitalize()` en vez de `.title()`. Si el nombre fuera "juan pérez", `.capitalize()` solo convierte la primera letra de cada palabra a mayúscula pero deja el resto en minúscula; `.title()` es más apropiado (aunque para este caso puntual el resultado sería el mismo).

```python
# Lo que hizo (incorrecto):
for i in range(len(split_input)):
    escape_input = split_input[i].strip().capitalize()
    print(f"Tu nombre es {escape_input}")

# Lo esperado:
nombre = input("Ingrese su nombre: ").strip().title()
print(f"Hola, {nombre}")
```

---

### Ejercicio 2 — Excepciones y bucles (5/10)

**Requisito:** Función `pedir_entero()` con `while True`, `try/except ValueError`, que no crashee, que repita hasta dato válido, y finalice con `break` o `return`.

**Aciertos:**
- ✅ Usa `while True` correctamente.
- ✅ Usa `try/except ValueError`.
- ✅ Termina con `break`.

**Errores:**
- ❌ **`raise ValueError` dentro del `try`.** El `ValueError` que lanza es capturado por su propio `except`. Esto es redundante y confunde: mezcla validación de negocio (edad fuera de rango) con el manejo de error de conversión (`int()`). Si el usuario ingresa "veinte", el `int("veinte")` lanza `ValueError` y se imprime el mensaje genérico de Python, no el suyo.
- ❌ **Mensaje de error incorrecto.** El enunciado pide `"Debe ingresar un número válido."`. El código imprime el mensaje de la excepción (`e`), que para texto sería algo como `invalid literal for int() with base 10: 'veinte'`.
- ❌ El except no diferencia entre error de conversión y validación de rango.

```python
# Lo que hizo:
except ValueError as e:
    print(e)  # Imprime el mensaje crudo de Python, no "Debe ingresar un número válido."

# Lo esperado:
except ValueError:
    print("Debe ingresar un número válido.")
```

---

### Ejercicio 3 — Listas de comprensión (3/10)

**Requisito:** Crear una nueva lista **en una sola línea** usando lista de comprensión con `.upper()`.

**Errores:**
- ❌ **No usa lista de comprensión.** Este era el requisito central del ejercicio. En su lugar usa un bucle `for` tradicional con `.append()`.
- ✅ El resultado final es correcto (la lista en mayúsculas).

```python
# Lo que hizo:
new_list = []
for i in range(len(palabras)):
    new_list.append(palabras[i].upper())

# Lo esperado:
new_list = [p.upper() for p in palabras]
```

---

### Ejercicio 4 — Lambda y sorted (1/10)

**Requisito:** Una sola línea con `for`, `sorted()` y `lambda` para ordenar por nombre e imprimir.

**Errores:**
- ❌ **Código roto.** `sorted(alumnos["nombre"])` — `alumnos` es una **lista** de diccionarios, no un diccionario. Esto produce `TypeError: list indices must be integers or slices, not str`.
- ❌ No usa `lambda`.
- ❌ No itera con `for` para imprimir los nombres.

```python
# Lo que hizo (no funciona):
sorteado = sorted(alumnos["nombre"])  # TypeError

# Lo esperado:
for alumno in sorted(alumnos, key=lambda a: a["nombre"]):
    print(alumno["nombre"])
```

---

### Ejercicio 5 — Archivos CSV (1/10)

**Requisito:** Abrir `estudiantes.csv` con `with open`, usar `csv.DictReader`, imprimir columna `nombre`.

**Errores:**
- ❌ **Confunde dos ejercicios.** Mezcla la lógica del ejercicio 7 (`sys.argv`) con el 5 (`csv`). El código valida argumentos de línea de comandos en lugar de abrir `estudiantes.csv` directamente.
- ❌ `ValueError("...")` sin `raise` — no hace nada, solo crea un objeto que se descarta.
- ❌ `with open(file, "r", ...)` sin `as f:` — el archivo se abre pero no se asigna a ninguna variable. No se puede leer.
- ❌ `for filas in file:` — itera sobre el string `file` (nombre del archivo), no sobre las líneas.
- ❌ `filas["nombre"]` — no funcionaría aunque leyera el archivo correctamente.
- ❌ No usa `csv.DictReader`.

---

### Ejercicio 6 — Expresiones regulares (1/10)

**Requisito:** Usar `re.search()` con `$` y `\\.` para validar correo `@uai.edu.ar`.

**Errores:**
- ❌ **No usa `re`.** El alumno lo admite en un comentario: *"olvide estudiar expresiones regulares :("*.
- ❌ No usa `re.search()`, no usa `$`, no escapa puntos.
- ✅ La lógica alternativa con `split("@")` funciona para el caso básico, pero no cumple el requisito del ejercicio.

```python
# Lo esperado:
import re
if re.search(r"@uai\.edu\.ar$", correo):
    print("El correo es válido")
else:
    print("El correo es inválido")
```

---

### Ejercicio 7 — Argumentos de línea de comandos (3/10)

**Requisito:** Verificar exactamente 1 argumento adicional con `sys.argv`. Si no, mostrar error y `sys.exit()`.

**Errores:**
- ❌ **No valida cantidad exacta.** `len(sys.argv) >= 2` acepta 1, 2, 3... argumentos. Debía ser `len(sys.argv) != 2` o `len(sys.argv) == 2`.
- ❌ **No usa `sys.exit()`.** El enunciado pide explícitamente salir con `sys.exit()` en caso de error.
- ❌ No imprime mensaje de error, solo "válida/inválida".

```python
# Lo que hizo:
if q >= 2:
    return True

# Lo esperado:
if len(sys.argv) != 2:
    print("Error: se requiere exactamente un argumento")
    sys.exit(1)
```

---

### Ejercicio 8 — POO: clase Libro (7/10)

**Requisito:** Clase `Libro` con `__init__` (titulo, autor) y `__str__` que devuelva `"Título por Autor"`.

**Aciertos:**
- ✅ `__init__` correcto con ambos atributos.
- ✅ `__str__` implementado.

**Errores:**
- ❌ **String de `__str__` incorrecto.** Agrega `"El "` al principio: `f"El {self.titulo} por {self.autor}"`. El formato esperado es `"El Aleph por Jorge Luis Borges"`, pero su código produciría `"El El Aleph por Jorge Luis Borges"` para ese ejemplo. Si el título fuera solo "Aleph", imprimiría `"El Aleph por Jorge Luis Borges"` — correcto por casualidad para ese caso, pero conceptualmente mal.

```python
# Lo que hizo:
return f"El {self.titulo} por {self.autor}"

# Lo esperado:
return f"{self.titulo} por {self.autor}"
```

---

### Ejercicio 9 — POO: encapsulamiento (0/10)

**Requisito:** Modificar clase `Libro` con `_titulo`, `@property`, `@titulo.setter`, validar no vacío, `raise ValueError`.

**Errores:**
- ❌ **No entregado.** Falta el archivo `ejercicio_9.py`. No hay código para evaluar.

---

### Ejercicio 10 — Pytest (2/10)

**Requisito:** Función `calcular_cuadrado(n)` que retorne `n * n`, y `test_calcular_cuadrado()` con asserts para positivo y cero.

**Aciertos:**
- ✅ El archivo de test (`test_ejercicio_10.py`) tiene la estructura correcta con dos asserts.

**Errores:**
- ❌ **`calcular_cuadrado` imprime en vez de retornar.** Usa `print(numero * numero)` en lugar de `return n * n`. La función retorna `None`.
- ❌ **Los tests fallarían.** `calcular_cuadrado(4)` retorna `None`, no `16`. Ambos asserts fallan.
- ❌ El import en el test (`from python2026_parcial1_uai.Nicolas_Andrade.ejercicio_10 import ...`) usa una ruta que no funcionaría al ejecutar `pytest`.

```python
# Lo que hizo:
def calcular_cuadrado(numero=1):
    print(numero * numero)  # solo imprime, no retorna

# Lo esperado:
def calcular_cuadrado(n):
    return n * n
```

---

## Observaciones generales

- **Estructura de archivos:** Falta `ejercicio_9.py`. El resto de los archivos sigue la convención de nombres (`ejercicio_X.py`).
- **Legibilidad:** El código es razonablemente claro, con comentarios y funciones separadas.
- **Comprensión de consignas:** Varios ejercicios reflejan que se leyó mal el enunciado (ej. 1: salida repetida por palabra; ej. 3: no usar lista de comprensión; ej. 5: mezclar ejercicios).
- **Uso de IA:** No hay evidencia clara de uso de IA generativa (los errores son "demasiado humanos" — errores típicos de principiante).