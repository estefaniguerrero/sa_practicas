# REPORTE DE IMPLEMENTACIÓN DE CÓDIGO LIMPIO

## Asignatura

Sistemas Ágiles

## Objetivo

Aplicar principios de código limpio para mejorar la legibilidad, mantenimiento y organización del sistema de inventario desarrollado en Python, además de implementar los nuevos requerimientos solicitados durante la práctica.

---

# Diagnóstico del código inicial

Durante el análisis del programa original se identificaron los siguientes problemas:

* Existían nombres de variables poco descriptivos, dificultando la comprensión del código.
* Una única función realizaba múltiples responsabilidades (validación, cálculos, almacenamiento y presentación de datos).
* Se utilizaban valores constantes escritos directamente en el código (Hardcoding), como el porcentaje del IVA.
* Existía duplicación de código para el cálculo del IVA.
* La información se almacenaba en un archivo de texto plano, limitando la escalabilidad del sistema.
* El programa presentaba una estructura poco modular, dificultando futuras modificaciones.

---

# Mejoras implementadas

Como parte de la aplicación de código limpio se realizaron las siguientes mejoras:

* Se utilizaron nombres de variables y constantes más descriptivos.
* Se reemplazó el almacenamiento en archivos TXT por archivos JSON.
* Se implementó el manejo de código de barras para cada producto.
* Se agregó una alerta cuando el stock es menor a cinco unidades.
* Se modificó el cálculo del IVA para aplicar el 12% a los productos de la categoría Tecnología.
* Se mejoró la organización general del programa siguiendo principios de modularidad.

---

# Refactorización

Para mejorar la mantenibilidad del proyecto, el programa fue dividido en varios archivos con responsabilidades específicas:

* **main.py:** punto de entrada del sistema y menú principal.
* **producto.py:** definición y gestión de los productos.
* **inventario.py:** operaciones del inventario.
* **archivo_json.py:** lectura y escritura de datos en formato JSON.
* **constantes.py:** almacenamiento de constantes utilizadas por el sistema.

Esta organización facilita la reutilización del código y simplifica futuras modificaciones.

---

# Beneficios obtenidos

La implementación de código limpio permitió:

* Mejorar la legibilidad del código.
* Reducir la duplicación de lógica.
* Facilitar el mantenimiento del sistema.
* Mejorar la organización del proyecto.
* Favorecer la reutilización de componentes.
* Facilitar futuras ampliaciones del sistema.

---

# Conclusiones

La aplicación de principios de código limpio permitió transformar un programa monolítico en una solución más organizada, modular y fácil de mantener. La incorporación de almacenamiento en formato JSON, la implementación de nuevos requerimientos y la separación de responsabilidades contribuyen a mejorar la calidad del software y facilitan su evolución en futuras versiones.

