"""
4. Registro de participantes con listas (3 ptos)
Crea una lista vacía y realiza lo siguiente:
- Agrega los nombres de tres participantes.
- Inserta un nuevo participante en la segunda posición.
- Actualiza el nombre del primer participante.
- Elimina uno de los participantes.
- Muestra la lista final y la cantidad de participantes registrados.
- No utilizar ciclos ni recorridos.
"""
lista=[]
lista.append("Angela")
lista.append("Fernanda")
lista.append("Jenny")

lista.insert(1,"Alvaro")
lista[0]="Matias"
lista.remove("Jenny")

print("Lista final:", lista)
print("Cantidad de participantes:", len(lista))