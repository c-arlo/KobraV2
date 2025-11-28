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
- docs
    - Manual técnico y de usuario
- examples/
  - expected/
    - Archivos de salida de los ejemplos validos
  - invalid/
    - Ejemplos de entrada CON errores
  - valid/
    - Ejemplos de entrada SIN errores
- lib/
    - Archivo fuente para antlr4
- src/
  - KobraV2.g4 – archivo de gramática del lenguaje.
  - KobraV2Lexer.py – archivo generado por ANTLR que define los tokens.
  - KobraV2Parser.py – parser generado a partir de la gramática.
  - KobraCompiler.py – módulo principal donde se implementa el visitor y generación de código.
  - main.py – archivo que ejecuta el proceso de transpilación.
- tests/
  - Archivos autogenerados con Makefile
- Makefile – Script de construcción

## Requisitos y Dependencias
| Componente | Versión | Propósito |
| - | - | - |
| Python  | 3.x	| Entorno de ejecución  |
| ANTLR4 Runtime  | 4.13.2	| Biblioteca de tiempo de ejecución del analizador  |
Archivos de gramática | Generados	| Componentes del analizador léxico y sintáctico

## Instrucciones de Compilación y Ejecución
1. Descargar Python desde la página oficial: https://www.python.org/downloads/ 
2. Verificar la instalación de Python
```bash
python –version o python3 --version
```
4.	Instalar ANTLR4 Python Runtime
```bash
pip install antlr4-python3-runtime==4.13.2
```
5.	Generar los archivos Lexer, Parser y Visitor para la gramatica 
```bash
antlr4 -o /src -Dlanguage=Python3 -visitor KobraV2.g4
```
6. El transpilador se ejecuta a través de main.py con un único argumento de línea de comandos que especifica la ruta del archivo de entrada:
```bash
python main.py <archivo_de_entrada.txt>
```

## Ejemplos de Uso
Ejemplo de declaración de variables, operadores y uso de la función integrada IMPRIMIR.
```
ENTERO a = 10;
ENTERO b = 3;
ENTERO c = a + b;
IMPRIMIR(c);
```
Archivo de salida generado.
```
# -*- coding: utf-8 -*-
# Codigo generado desde KobraV2
import sys

def _kobra_div(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    return a / b

a = 10
b = 3
c = a + b
print(c)
```
Ejemplo de condicionales.
```
ENTERO x = 5;
SI (x > 0) {
    IMPRIMIR("El valor es positivo");
} SINO {
    IMPRIMIR("El valor es negativo");
}
```
Archivo de salida generado.
```
# -*- coding: utf-8 -*-
# Codigo generado desde KobraV2
import sys

def _kobra_div(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    return a / b

x = 5
if x > 0:
    print("El valor es positivo")
else:
    print("El valor es negativo")
```
Ejemplo de ciclo PARA (Equivalente de FOR).
```
PARA (i = 0; i < 3; i = i + 1) {
    IMPRIMIR("Iteración " + i);
}
```
Archivo de salida generado.
```
# -*- coding: utf-8 -*-
# Codigo generado desde KobraV2
import sys


def _kobra_div(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    return a / b

i = 0
while i < 3:
    print("Iteración " + i)
    i = i + 1
```
