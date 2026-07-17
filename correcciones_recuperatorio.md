# Corrección Recuperatorio - Parcial 1 Python 2026

**Fecha de corrección:** 16 de julio de 2026  
**Corrector:** Hermes Agent  
**Repositorio:** https://github.com/cursos-uai/python2026_parcial1_uai

---

## 📋 Metodología de Corrección

- **Ejercicios evaluados:** 1, 2, 3, 5, 6, 7, 8 (obligatorios)
- **Ejercicios opcionales:** 4, 9, 10 (no suman a la nota base)
- **Escala:** 0-10 por ejercicio
- **Criterio de aprobación:** 6.0/10 (42/70 puntos)

---

## 👨‍🎓 ANÁLISIS INDIVIDUAL

### 1. Nicolás Andrade

**PR:** #16 - "Corrección Recuperatorio Nicolas Andrade"  
**Nota Final:** 5.4/10 (38/70 puntos)  
**Estado:** ❌ **DESAPROBADO** (nota < 6.0)

#### Ejercicios Obligatorios

| Ejercicio | Nota | Comentarios |
|-----------|------|-------------|
| **1. Nombre + f-strings** | 6/10 | Usa f-string correctamente pero el formato de salida es incorrecto. Imprime "Tu nombre es [parte]" para cada palabra en lugar de "Hola, [Nombre Completo]". Lógica confusa con split() + capitalize(). |
| **2. pedir_entero()** | 10/10 | ✅ Perfecto. Implementa while True, try/except ValueError, validación adicional de rango (0-120), y break correctamente. |
| **3. List comprehension** | 4/10 | ❌ **NO usa list comprehension.** Usa bucle for tradicional con .append(). El enunciado pide explícitamente comprensión de listas en una sola línea. |
| **5. CSV DictReader** | 3/10 | ❌ No usa csv.DictReader. Intenta iterar directamente sobre el objeto file sin crear el reader. Código no funcional. Error en manejo de argumentos. |
| **6. Regex @uai.edu.ar** | 3/10 | ❌ **NO usa expresiones regulares.** Reconoce que no estudió regex y hace un workaround con split("@"). No usa re.search(), anclaje $, ni escapes \. como requiere el enunciado. |
| **7. sys.argv** | 4/10 | ❌ No usa sys.exit() para terminar el programa. Solo imprime mensajes. Validación incorrecta: `if q >= 2` permite más de 1 argumento cuando debería ser exactamente 2. |
| **8. POO Libro** | 8/10 | Clase y métodos correctos. ❌ **Formato incorrecto:** __str__ retorna "El {titulo} por {autor}" pero el ejemplo pide "{titulo} por {autor}" (sin "El"). |

#### Ejercicios Opcionales

| Ejercicio | Nota | Comentarios |
|-----------|------|-------------|
| 4. sorted + lambda | 1/10 | Error de sintaxis: intenta `sorted(alumnos["nombre"])` cuando alumnos es una lista. No usa lambda. |
| 9. @property | No entregado | - |
| 10. pytest | 2/10 | La función calcular_cuadrado() usa print() en lugar de return. Los tests van a fallar porque la función retorna None. |

#### Análisis Pedagógico

**Fuertes:**
- Comprensión sólida de try/except y manejo de excepciones
- Estructura básica de POO (clase, __init__, __str__)

**Errores conceptuales críticos:**
1. **List comprehension:** No entiende que es una alternativa al bucle for con append()
2. **Regex:** Evita el tema en lugar de aprenderlo ("olvidé estudiar expresiones regulares")
3. **sys.exit():** No comprende que debe terminar el programa, no solo imprimir mensajes
4. **CSV DictReader:** Confunde el objeto file con el reader
5. **Portabilidad:** No aplica buenas prácticas de rutas relativas

**Recomendación:**  
Nicolás necesita repasar los temas 3 (list comprehension), 6 (regex), 7 (sys.argv con sys.exit), y 5 (CSV con DictReader). Se sugiere realizar ejercicios adicionales prácticos sobre estos conceptos antes de un próximo recuperatorio.

---

### 2. Agustín Aguero

**PR:** #17 - "Recuperación Parcial 1 Agustin Aguero"  
**Nota Final:** 10/10 (70/70 puntos)  
**Estado:** ✅ **APROBADO CON EXCELENCIA**

#### Ejercicios Obligatorios

| Ejercicio | Nota | Comentarios |
|-----------|------|-------------|
| **1. Nombre + f-strings** | 10/10 | ✅ Perfecto. Usa strip() + title(), f-string con formato "Hola, {nombre}" que coincide exactamente con el ejemplo. |
| **2. pedir_entero()** | 10/10 | ✅ Perfecto. while True, try/except ValueError, return para salir del bucle. Mensaje de error claro. |
| **3. List comprehension** | 10/10 | ✅ Perfecto. `[palabra.upper() for palabra in palabras]` - comprensión de listas en una sola línea. |
| **5. CSV DictReader** | 10/10 | ✅ Perfecto. Corrige el error de portabilidad de su entrega original. Usa ruta relativa "estudiantes.csv" en lugar de ruta absoluta de Windows. |
| **6. Regex @uai.edu.ar** | 10/10 | ✅ Perfecto. `re.search(r"@uai\.edu\.ar$", correo)` - usa re.search(), anclaje $, escapa puntos con \., maneja ambos casos. |
| **7. sys.argv** | 10/10 | ✅ Perfecto. Verifica `len(sys.argv) != 2`, usa sys.exit() con mensaje de error, termina el programa correctamente. |
| **8. POO Libro** | 10/10 | ✅ Perfecto. Clase Libro con __init__ y __str__. Formato correcto: "{titulo} por {autor}". |

#### Ejercicio Adicional: Video de Metacognición

| Elemento | Nota | Comentarios |
|----------|------|-------------|
| **Video de Recuperación** | 10/10 | ✅ Excelent trabajo. Link válido a Google Drive, 10 minutos de duración. Transcripción detallada de 4 ejercicios (1, 3, 5, 8). Explica claramente: (1) qué estaba mal en la entrega original, (2) qué concepto le faltaba, (3) cómo lo corrigió paso a paso. Demuestra metacognición y aprendizaje profundo. |

#### Análisis Pedagógico

**Fuertes:**
- **Corrección integral:** Identificó y corrigió TODOS los errores de su entrega original
- **Comprensión profunda:** No solo corrigió código, sino que entendió los conceptos subyacentes
- **Metacognición excelente:** El video demuestra reflexión crítica sobre su propio aprendizaje
- **Portabilidad:** Aprendió la importancia de rutas relativas vs absolutas
- **Buenas prácticas:** Aplica principios de código limpio y legible

**Evolución desde entrega original:**
- Original: Errores en f-strings, list comprehension, paths absolutos, regex, POO
- Recuperación: **10/10 en todos los ejercicios obligatorios**

**Recomendación:**  
Agustín demostró capacidad de aprendizaje excepcional. Su enfoque de video-transcripción es ejemplar y debería ser modelo para futuros estudiantes. Continuar con ejercicios más avanzados de POO y automatización.

---

## 📊 TABLA RESUMEN

| # | Alumno | Ej1 | Ej2 | Ej3 | Ej5 | Ej6 | Ej7 | Ej8 | Total | Base 10 | Estado |
|---|--------|-----|-----|-----|-----|-----|-----|-----|-------|---------|--------|
| 1 | Nicolás Andrade | 6 | 10 | 4 | 3 | 3 | 4 | 8 | 38/70 | **5.4** | ❌ Desaprobado |
| 2 | Agustín Aguero | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 70/70 | **10.0** | ✅ Aprobado |

**Estadísticas del Recuperatorio:**
- **Promedio:** 7.7/10
- **Aprobados:** 1 de 2 (50%)
- **Desaprobados:** 1 de 2 (50%)
- **Nota más alta:** 10.0 (Agustín Aguero)
- **Nota más baja:** 5.4 (Nicolás Andrade)

---

## 🎯 ERRORES MÁS FRECUENTES

1. **No usar list comprehension** (Nicolás): Usa for tradicional con append()
2. **Evitar regex** (Nicolás): Workaround con split() en lugar de re.search()
3. **No usar sys.exit()** (Nicolás): Solo imprime mensajes, no termina el programa
4. **Confundir file con DictReader** (Nicolás): Itera sobre el objeto file directamente
5. **Formato incorrecto en __str__** (Nicolás): Agrega "El" al inicio cuando no corresponde

---

## 💡 RECOMENDACIONES GENERALES

### Para Nicolás Andrade:
1. **Repasar temas 3, 5, 6, 7** con ejercicios prácticos adicionales
2. **No evitar temas difíciles:** "Olvidé estudiar regex" no es excusa, es señal de que necesita más práctica
3. **Leer con atención los enunciados:** Muchas fallas vienen de no seguir las instrucciones específicas
4. **Probar el código mentalmente:** Antes de entregar, simular la ejecución paso a paso

### Para Agustín Aguero:
1. **Continuar con nivel avanzado:** Está listo para POO con herencia, decoradores, y testing
2. **Ser mentor de compañeros:** Su comprensión y capacidad de explicación son valiosas
3. **Documentar más proyectos:** Su enfoque de video-transcripción es excelente para portfolios

### Para el curso:
1. **Refuerzo en regex:** Muchos estudiantes evitan este tema; considerar ejercicios semanales
2. **Ejemplos de list comprehension:** Mostrar más casos de uso en contexto real
3. **sys.exit() vs print():** Aclarar diferencia entre terminar programa y mostrar mensaje

---

## 📝 OBSERVACIONES FINALES

**Nicolás Andrade** necesita un segundo recuperatorio o trabajo adicional para aprobar. Se recomienda:
- Entregar un nuevo PR con ejercicios adicionales de los temas fallidos
- O realizar un examen oral de 15 minutos demostrando comprensión de los conceptos

**Agustín Aguero** ha demostrado excelencia en esta recuperación. Su trabajo es un ejemplo de:
- Capacidad de aprendizaje autónomo
- Metacognición (reflexión sobre el propio aprendizaje)
- Compromiso con la mejora continua

---

**Firmado:**  
Hermes Agent - Corrector Automático  
16 de julio de 2026
