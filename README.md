# Reporte de Deuda Técnica y Adaptabilidad del Software

**Asignatura:** Sistemas Ágiles  
**Integrantes:** Estefani Guerrero, Christian Flores y Paola Tapia  
**Fecha:** 30 de Junio de 2026  

---

## 🔍 1. Diagnóstico de Calidad (Código Legacy)

Principales problemas de diseño encontrados en el archivo original utilizando conceptos de calidad de código:

* **Problema 1: Código Duplicado (Antipatrón Duplicated Code)** * *Sección afectada:* Líneas 19 y 66 del documento de la práctica. El cálculo del IVA del 15% está quemado (hardcoded) dos veces en lugares totalmente separados (en el registro y en el reporte), violando el principio DRY (Don't Repeat Yourself).
* **Problema 2: Función Monolítica / Función Dios** * *Sección afectada:* Función p_pro (Líneas 12 a 68). Una sola función se encarga de hacer absolutamente todo al mismo tiempo: valida datos, calcula impuestos, escribe archivos y formatea la consola.
* **Problema 3: Nombres de Variables Oscuros o Crípticos** * *Sección afectada:* Líneas 44 a 51. Uso de variables poco claras como A, x1, p1, c1, t1 y pf1, lo cual destruye la legibilidad del código.

---

## 📈 2. Mapeo de Dificultades para la Evolución (Evidencia Git)

Impacto técnico al aplicar los requerimientos de forma individual:

* ### 🛠️ Rama: cambio-impuesto
    * *Impacto encontrado:* Debido a la duplicación del cálculo del IVA, cambiar el impuesto al 12% para Tecnología obligó a buscar y alterar múltiples bloques funcionales. Si se olvida cambiar uno, el reporte financiero de IVA se rompe y queda inconsistente.
* ### 🛠️ Rama: cambio-json
    * *Impacto encontrado:* Cambiar el almacenamiento de texto plano .txt separado por comas a un archivo estructurado .json rompió por completo el sistema de lectura y escritura, obligando a reescribir toda la lógica de persistencia desde cero.
* ### 🛠️ Rama: codigo-barras
    * *Impacto encontrado:* Al añadir un parámetro obligatorio al inicio de la función principal, se alteró la firma de la función en todo el script. Además, desalineó el orden de los arreglos por posición (datos1[0], datos1[1]), generando errores en cadena.

---

## 🚀 3. Propuesta de Refactorización Inicial

Tres acciones principales para eliminar la deuda técnica usando Código Limpio (Clean Code):

1. **Aplicar el Principio de Responsabilidad Única (SRP):** Dividir la función gigante p_pro en funciones pequeñas e independientes (ej. validar_producto, guardar_producto, calcular_iva, imprimir_tabla).
2. **Encapsular los datos en Objetos (POO):** Reemplazar el manejo de strings crípticos por una clase formal Producto con atributos claros y tipados.
3. **Abstracción de Persistencia:** Crear un módulo separado para el manejo de archivos, permitiendo cambiar entre TXT y JSON sin alterar la lógica de negocio del inventario.

---

## 🏁 4. Conclusiones del Equipo

* **Porcentaje estimado de deuda técnica en el script original (0% al 100%):** 75%  
* **Reflexión ágil:** Un software rígido y con alta deuda técnica frena drásticamente la velocidad de entrega en Scrum. Cada cambio "sorpresa" o nuevo requerimiento genera un efecto dominó que rompe partes del código viejo, obligando a realizar retrabajos masivos en lugar de entregar valor constante en cada Sprint.