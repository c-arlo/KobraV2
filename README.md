# KobraV2 

KobraV2 es un transpilador que convierte archivos escritos en el lenguaje original de KobraV2 a archivos en el lenguaje Python listos para su ejecucion 

## Información del Curso
* Materia: Compiladores 2
* Institución: Universidad Autónoma de Tamaulipas - Facultad de Ingeniería
* Semestre: Segundo semestre de 2025
* Profesor(es): Dante Adolfo Muñoz Quintero

## Integrantes del Equipo
- Badillo González Víctor Manuel - a2213332135
- Clemente Villegas José Adán - a2213332149
- Cristóbal Francisco Jesús Marcelino - a2213332150
- Granados Gallegos Carlo Sebastián - a2203330135

## Estructura del Proyecto
docs/
  • Manual técnico y de usuario
examples/
  expected/
    • Archivos de salida de los ejemplos validos
  invalid/
    • Ejemplos de entrada CON errores
  valid/
    • Ejemplos de entrada SIN errores
lib/
  • Archivo fuente para antlr4
src/
  •	KobraV2.g4 – archivo de gramática del lenguaje.
  •	KobraV2Lexer.py – archivo generado por ANTLR que define los tokens.
  •	KobraV2Parser.py – parser generado a partir de la gramática.
  •	KobraCompiler.py – módulo principal donde se implementa el visitor y generación de código.
  •	main.py – archivo que ejecuta el proceso de transpilación.
tests/
  • Archivos autogenerados con Makefile
•	Makefile – Script de construcción

## Requisitos y Dependencias
[Software y librerías necesarias]

## Instrucciones de Compilación y Ejecución
[Pasos detallados para compilar y ejecutar]

## Ejemplos de Uso
[Código de ejemplo y explicación]
