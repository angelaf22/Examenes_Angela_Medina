"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (3 ptos)
Reglas:
    - Asignar en variables los datos de tu nombre, salario, edad y compañía para un
    usuario e identificar sus tipos de variables
    - Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
    conversión de datos
    - Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
    tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
    tiene un bono del 5% en el mes diciembre”
    - Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
    salario, según corresponda
"""
nombre="Angela Medina"
salario= 2800.00
edad="23"
compania="Notaria Medina"
tipo_nombre= type(nombre)
tipo_salario= type(salario)
tipo_edad= type(edad)
tipo_compania= type(compania)
if(int(edad)>30):
    mensaje="Usted tiene un bono de 10% en el mes de diciembre"
    bono= (salario*0.10)
else:
    mensaje="Usted tiene un bono del 5% en el mes de diciembre"
    bono= (salario*0.05)
print(mensaje)
print("El bono final es: S/", (salario**2)+bono)