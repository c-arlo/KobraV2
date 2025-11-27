# -*- coding: utf-8 -*-
# Codigo generado desde KobraV2
import sys


def _kobra_div(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    return a / b

contador = 5
factorial = 1
i = 1
sumaPares = 0
maximo = 10
print("1. Cuenta regresiva con MIENTRAS:")
while contador > 0:
    print(contador)
    contador = contador - 1
print("2. Calculo de factorial y suma de pares con PARA:")
i = 1
while i <= maximo:
    factorial = factorial * i
    checkPar = (_kobra_div(i, 2)) * 2
    if checkPar == i:
        sumaPares = sumaPares + i
        print("Numero par encontrado:")
        print(i)
    i = i + 1
print("Resultados Finales:")
print("Factorial de 10 (aprox):")
print(factorial)
print("Suma de los numeros pares:")
print(sumaPares)
