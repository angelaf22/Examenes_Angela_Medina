"""
1. Registro de personas (4 ptos)
Requisitos:
• Crear una clase Persona con los atributos nombre, edad, saldo y nacionalidad. La nacionalidad tendrá como valor inicial “Peruana”.
• Implementar un método que permita registrar el nombre y la edad de una persona mediante la consola. Si la edad ingresada no es un número entero válido o es negativa, informar el problema y solicitar nuevamente el dato.
• Implementar un método cumpleaños que incremente la edad en un año cada vez que se invoque.
• Crear como mínimo dos objetos de la clase Persona, utilizar el método cumpleaños y mostrar las edades actualizadas.
• Registrar el momento de creación de cada persona y mostrar, mediante una función, la fecha y hora de registro con precisión de minutos.
"""
class Persona:
    def __init__(self,monto):
        from datetime import datetime
        self.nombre = ""
        self.edad = 0
        self.saldo = monto  
        self.nacionalidad = "Peruana"
        self.fecha = datetime.now()

    def registrar(self):
        self.nombre = input("Ingrese el nombre: ")
        while True:
            try:
                self.edad = int(input("Ingrese la edad: "))
                if self.edad < 0:
                    print("La edad no puede ser negativa.")
                else:
                    break
            except ValueError:
                print("La edad debe ser un número entero.")

    def cumpleanos(self):
        self.edad += 1

    def mostrar_fecha_registro(self):
        return self.fecha.strftime('%Y-%m-%d %H:%M')

#
if __name__ == "__main__":
    persona1 = Persona(0)
    persona1.registrar()
    persona2 = Persona(0)
    persona2.registrar()
    
    print(f"Edad inicial de {persona1.nombre} es: {persona1.edad}")
    print(f"Edad inicial de {persona2.nombre} es: {persona2.edad}")

    persona1.cumpleanos()
    persona2.cumpleanos()
    
    print(f"Edad actualizada de {persona1.nombre} es: {persona1.edad}")
    print(f"Edad actualizada de {persona2.nombre} es: {persona2.edad}")
    
    print(f"Fecha de registro de {persona1.nombre} es: {persona1.mostrar_fecha_registro()}")
    print(f"Fecha de registro de {persona2.nombre} es: {persona2.mostrar_fecha_registro()}")