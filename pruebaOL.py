# -*- coding: utf-8 -*-
# Codigo generado desde KobraV2
import sys


def _kobra_div(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    return a / b

tengoLlave = False
soyAdmin = True
sistemaActivo = True
nivelSeguridad = 5
print("Verificando acceso al sistema Kobra...")
if tengoLlave == True or soyAdmin == True:
    print("Acceso Basico: CONCEDIDO (Tienes llave O eres admin)")
else:
    print("Acceso Basico: DENEGADO")
if soyAdmin == True and nivelSeguridad >= 5:
    print("Acceso Nivel Alto: CONCEDIDO")
if (tengoLlave == True and sistemaActivo == False) or (soyAdmin == True and sistemaActivo == True):
    print("Acceso de Emergencia: ACTIVADO")
else:
    print("Acceso de Emergencia: FALLIDO")
if nivelSeguridad != 0:
    print("El sistema tiene seguridad activa.")
