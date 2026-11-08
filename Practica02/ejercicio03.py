"""
3. Funciones y manejo de excepciones (3 ptos)
Requisitos:
    • Crear una función que solicite al usuario dos valores numéricos por consola y los retorne para utilizarlos en las operaciones.
    • Crear una función que reciba dos valores como parámetros, realice una división y retorne el resultado.
    • Crear una función que reciba dos valores como parámetros, realice una suma y retorne el resultado.
    • Solicitar al usuario cuántos elementos desea registrar (N) y crear una función que reciba esos datos ingresados por consola, los almacene en una lista y retorne la lista.
    • Solicitar al usuario el índice que desea consultar y crear una función que reciba la lista y dicho índice como parámetros para retornar el elemento correspondiente.
    • Controlar los errores provocados por entradas no numéricas, divisiones entre cero, operaciones entre tipos incompatibles y consultas a posiciones inexistentes de la lista.
    • Cuando se produzca un error, mostrar un mensaje descriptivo y permitir un nuevo intento de la operación correspondiente.
    • Utilizar else y finally en al menos una de las operaciones realizadas.
    • Ejecutar las funciones creadas utilizando los datos proporcionados por el usuario y mostrar por consola los resultados de las operaciones correctas. Incluir 3 pruebas con datos válidos e inválidos.
""" 
def solicitar_valores():
    while True:
        try:
            valor1=float(input("Ingrese el primer valor: "))
            valor2=float(input("Ingrese el segundo valor: "))
            return valor1, valor2
        except ValueError:
            print("Los valores deben ser numeros")
def dividir_valores(valor1, valor2):
    try:
        division = valor1/valor2
    except ZeroDivisionError:
        print("División entre cero no es válida")
        return None
    else:
        return division
    finally:
        print("división finalizada")

def suma_valores(valor1, valor2):
        suma = valor1 + valor2
        return suma 

def cantidad_elementos():
    while True:
        try:
            n = int(input("Ingrese el numero de elementos a registrar: "))
            if n <= 0:
                print("La cantidad debe ser mayor a cero")
            else:
                return n
        except ValueError:
            print("La cantidad debe ser un número entero")
def registar(n):
    elementos = []
    for i in range(n):
        while True:
            try:
                valor = float(input(f"Ingrese el elemento numero {i+1}: "))
                elementos.append(valor)
                break
            except ValueError:
                print("El valor debe ser un número")
    return elementos

#impresion de valores
valor1,valor2=solicitar_valores()
print("Valores: ",valor1,valor2)

division=dividir_valores(valor1,valor2)
print("Division: ",division)

suma=suma_valores(valor1,valor2)
print("Suma: ",suma)

n=cantidad_elementos()
elementos=registar(n)
print("Elementos ingresados: ",elementos)