# -*- coding: utf-8 -*-
# Codigo generado desde KobraV2
import sys


def _kobra_div(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    return a / b

costoComida = 450.50
costoBebidas = 120.00
tasaPropina = 0.15
personas = 3
total = 0.0
propina = 0.0
totalFinal = 0.0
porPersona = 0.0
total = costoComida + costoBebidas
print("--- TICKET DE KOBRA RESTAURANT ---")
print("Subtotal comida y bebida:")
print(total)
if total > 500.0:
    print("Consumo alto detectado. Aplicando propina sugerida del 15%")
    propina = total * tasaPropina
else:
    print("Consumo estandar. Propina fija de 50 pesos.")
    propina = 50.0
totalFinal = total + propina
print("Propina calculada:")
print(propina)
print("TOTAL A PAGAR:")
print(totalFinal)
porPersona = _kobra_div(totalFinal, personas)
print("Monto a pagar por persona:")
print(porPersona)
print("Imprimiendo recibos individuales...")
i = 0
i = 0
while i < personas:
    print("Recibo impreso.")
    i = i + 1
