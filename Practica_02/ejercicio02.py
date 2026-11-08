"""
2. Transferencias entre personas (3 ptos)
Requisitos:
• Utilizar la clase Persona del ejercicio anterior y su atributo saldo para simular transferencias entre dos personas.
• Implementar los métodos necesarios para consultar el saldo y efectuar una transferencia de dinero de una persona a otra.
• Cada transferencia válida deberá descontar el monto de la persona que envía el dinero y sumarlo al saldo de quien lo recibe.
• No permitir transferencias con montos no numéricos, menores o iguales a cero, ni superiores al saldo disponible. Informar al usuario cuando la operación no pueda realizarse y conservar los saldos sin cambios.
• Demostrar el funcionamiento con dos personas, incluyendo al menos una transferencia válida y un intento de transferencia rechazado.
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
    
    def consultar_saldo(self):
        print(f"El saldo de {self.nombre} es: {self.saldo}")

    def transferir(emisor, receptor, monto):
        try:
            monto = float(monto)
            if monto <= 0:
                print("El monto a enviar debe ser mayor a cero")
            elif monto > emisor.saldo:
                print(f"Rechazado, saldo insuficiente")
            else:
                emisor.saldo -= monto
                receptor.saldo += monto
                print(f"Transferencia de {monto} realizada con éxito.")
        except ValueError:
            print("El monto debe ser un número.")

#
persona1 = Persona(100)
persona1.registrar()
persona2 = Persona(50)
persona2.registrar()

persona1.consultar_saldo()
persona2.consultar_saldo()

Persona.transferir(persona1, persona2, 30)
persona1.consultar_saldo()
persona2.consultar_saldo()

Persona.transferir(persona1, persona2, 200)
persona1.consultar_saldo()
persona2.consultar_saldo()