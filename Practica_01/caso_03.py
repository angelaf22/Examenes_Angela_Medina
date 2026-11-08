"""
- Caso: Calculadora de propinas
Crea un programa que permita ingresar el total de una cuenta en un restaurante,
el porcentaje de propina que desea dejar el cliente y el número de personas que
dividirán la cuenta. El programa debe mostrar:
El monto total con propina.
El monto que debe pagar cada persona (con 2 decimales).
Un mensaje será personalizado, indicará si el monto individual supera los 100
soles, mostrando un mensaje de advertencia si es el caso.
Entrada esperada (por input):
Total de la cuenta: float
Porcentaje de propina: float
Número de personas: int
Salida ejemplo (output):
Monto total con propina: S/. 230.00
Cada persona debe pagar: S/. 115.00
¡Advertencia! El monto por persona supera los S/. 100
"""
total=250.12
propina=0.15
personas=2

monto_total= total+(total*propina)
monto_persona= monto_total/personas

print("Monto total incluida propina: S/. {:.2f}".format(monto_total))
print("Cada persona debe pagar: S/. {:.2f}".format(monto_persona))

if monto_persona>100:
    print("¡Advertencia! El monto por persona supera los S/. 100")