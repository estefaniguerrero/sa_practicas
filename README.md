# 📊 Reporte de Deuda Técnica y Adaptabilidad del Software

[cite_start]**Asignatura:** Sistemas Ágiles [cite: 142]
[cite_start]**Integrantes:** Estefani Guerrero y Paola Tapia [cite: 143]
[cite_start]**Fecha:** 30 de Junio de 2026 [cite: 144]

---

## [cite_start]🔍 1. Diagnóstico de Calidad (Código Legacy) [cite: 145]
[cite_start]Principales problemas de diseño encontrados en el archivo original utilizando conceptos de calidad de código[cite: 146]:

1. [cite_start]**Problema 1: Código Duplicado (Antipatrón Duplicated Code)** [cite: 21, 56, 147]
   * [cite_start]**Sección afecta:** Líneas 19 y 66 del documento de la práctica[cite: 19, 66]. [cite_start]El cálculo del IVA del 15% está quemado (hardcoded) dos veces en lugares totalmente separados (en el registro y en el reporte)[cite: 18, 19, 56, 65, 66], violando el principio DRY (Don't Repeat Yourself).
2. [cite_start]**Problema 2: Función Monolítica / Función Dios** [cite: 12, 13, 147]
   * [cite_start]**Sección afecta:** Función `p_pro` (Líneas 12 a 68)[cite: 12, 68]. [cite_start]Una sola función se encarga de hacer absolutamente todo al mismo tiempo: valida datos, calcula impuestos, escribe archivos y formatea la consola[cite: 13].
3. [cite_start]**Problema 3: Nombres de Variables Oscuros o Crípticos** [cite: 44, 147]
   * [cite_start]**Sección afecta:** Líneas 44 a 51[cite: 44, 51]. [cite_start]Uso de variables poco claras como `A`, `x1`, `p1`, `c1`, `t1` y `pf1`[cite: 11, 45, 47, 48, 50, 51], lo cual destruye la legibilidad del código.

---

## [cite_start]📈 2. Mapeo de Dificultades para la Evolución (Evidencia Git) [cite: 149]
[cite_start]Impacto técnico al aplicar los requerimientos de forma individual[cite: 149]:

* [cite_start]### 🛠️ Rama: `cambio-impuesto` [cite: 152]
  * [cite_start]**Impacto encontrado:** Debido a la duplicación del cálculo del IVA [cite: 56, 65][cite_start], cambiar el impuesto al 12% para Tecnología obligó a buscar y alterar múltiples bloques funcionales[cite: 135]. Si se olvida cambiar uno, el reporte financiero de IVA se rompe y queda inconsistente.
* [cite_start]### 🛠️ Rama: `cambio-json` [cite: 155]
  * [cite_start]**Impacto encontrado:** Cambiar el almacenamiento de texto plano `.txt` separado por comas a un archivo estructurado `.json` rompió por completo el sistema de lectura y escritura[cite: 28, 35, 136], obligando a reescribir toda la lógica de persistencia desde cero.
* [cite_start]### 🛠️ Rama: `codigo-barras` [cite: 158]
  * [cite_start]**Impacto encontrado:** Al añadir un parámetro obligatorio al inicio de la función principal, se alteró la firma de la función en todo el script[cite: 12, 137]. [cite_start]Además, desalineó el orden de los arreglos por posición (`datos1[0]`, `datos1[1]`)[cite: 46, 47], generando errores en cadena.

---

## [cite_start]🚀 3. Propuesta de Refactorización Inicial [cite: 160]
[cite_start]Tres acciones principales para eliminar la deuda técnica usando Código Limpio (Clean Code)[cite: 161]:

1. [cite_start]**Aplicar el Principio de Responsabilidad Única (SRP):** Dividir la función gigante `p_pro` en funciones pequeñas e independientes (ej. `validar_producto`, `guardar_producto`, `calcular_iva`, `imprimir_tabla`)[cite: 12, 13, 162].
2. [cite_start]**Encapsular los datos en Objetos (POO):** Reemplazar el manejo de strings crípticos por una clase formal `Producto` con atributos claros y tipados[cite: 44, 163].
3. [cite_start]**Abstracción de Persistencia:** Crear un módulo separado para el manejo de archivos, permitiendo cambiar entre TXT y JSON sin alterar la lógica de negocio del inventario[cite: 136, 163].

---

## [cite_start]🏁 4. Conclusiones del Equipo [cite: 164]
* [cite_start]**Porcentaje estimado de deuda técnica en el script original (0% al 100%):** 75% [cite: 165]
* [cite_start]**Reflexión ágil:** Un software rígido y con alta deuda técnica frena drásticamente la velocidad de entrega en Scrum[cite: 165]. [cite_start]Cada cambio "sorpresa" o nuevo requerimiento genera un efecto dominó que rompe partes del código viejo, obligando a realizar retrabajos masivos en lugar de entregar valor constante en cada Sprint[cite: 149, 165].