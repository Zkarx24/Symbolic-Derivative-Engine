# Symbolic Derivative Engine

## Descripción del Proyecto
Este proyecto consiste en un motor de cálculo simbólico desarrollado en Python que deduce derivadas mediante la aplicación de la definición formal de límite:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

El sistema automatiza el proceso de derivación prescindiendo de reglas de derivación pre-programadas, ejecutando en su lugar la expansión polinómica, la simplificación algebraica y la resolución del cociente de diferencias mediante la librería SymPy.

## Especificaciones Técnicas
* **Lenguaje:** Python 3.x
* **Dependencias:** SymPy (Cálculo Simbólico)
* **Arquitectura:**
    * **Módulo de Parsing:** Conversión de expresiones de texto a objetos matemáticos con contexto de variables restringido.
    * **Motor de Inyección:** Aplicación de incrementos (h) mediante sustitución de variables.
    * **Módulo de Expansión:** Resolución de identidades trigonométricas y desarrollos binomiales para $f(x+h)$.
    * **Evaluador de Límites:** Cálculo simbólico del cociente de Newton tendiendo a cero.

## Justificación Técnica
El desarrollo de este motor tiene como objetivo demostrar competencia en:
1. **Descomposición Algorítmica:** Capacidad para traducir modelos matemáticos teóricos en flujos de trabajo de software estructurados.
2. **Pensamiento Analítico:** Implementación de soluciones lógicas mediante el manejo de restricciones (variables reales, entornos locales, resolución de singularidades).
3. **Gestión de Entornos:** Configuración de dependencias y aislamiento de proyectos para garantizar la reproducibilidad del código.

## Configuración y Ejecución

### Requisitos
* Python 3.10+
* Gestor de paquetes `pip`

### Instalación
1. Clonar el repositorio:
   ```bash
   git clone <https://github.com/Zkarx24/Symbolic-Derivative-Engine/>
### Ejecución
1. Ejecutar el script llamado sde.py en python
   <img width="699" height="486" alt="image" src="https://github.com/user-attachments/assets/66275f6b-7591-4eb7-a8c6-69caca112601" />

