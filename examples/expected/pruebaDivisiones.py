# -*- coding: utf-8 -*-
# Codigo generado desde KobraV2
import sys


def _kobra_div(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    return a / b

a = 9
b = 2
x = 9.0
y = 2.0
check = True
print("--- PRUEBA DE DIVISION ---")
print("Division Entera (9/2):")
print(_kobra_div(a, b))
print("Division Flotante (9.0/2.0):")
print(_kobra_div(x, y))
print("Division Mixta (9/2.0):")
print(_kobra_div(a, y))
if check == True:
    print("El booleano en español funciona!")
