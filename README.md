Se aplicaron principios de Código Limpio y refactorizaciones al sistema de inventario para mejorar su legibilidad, robustez y mantenibilidad, sin cambiar su funcionalidad.

Principales mejoras

Guardia y manejo de errores: se añadió una validación previa (if not existe_archivo():) al leer datos para evitar que el programa falle si datos_inv.txt no existe en la primera ejecución.

Soporte de codificación UTF‑8: se especificó encoding="utf-8" al abrir archivos para evitar errores con tildes y caracteres especiales (p. ej., categorías como Tecnología o Útiles).

Tipado estático (type hints): se agregaron anotaciones de tipo en parámetros y retornos para mejorar la claridad del flujo y el soporte del editor/IDE.

Formato consistente de salida: se estandarizó la impresión de valores monetarios usando dos decimales (:.2f) para mayor uniformidad.