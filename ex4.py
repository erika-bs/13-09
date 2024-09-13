# Implementação de uma fila
"""""
enqueue - inclui elementos na fila
dequeue  - remove o elemento da fila
is_empty - retorna se a fila esta vazia
size - retorna o tamanho da fila

"""
# Criação da Classe
class Fila:
    # Criação do construtor
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    

# 4) Inverter a fila

fila = Fila()

for item in range(1,11):
    fila.enqueue(item)
    
print(f"fila original: {fila}")


# Armazenar os elementos em uma lista
listaInvertida = []
while not fila.is_empty():
    listaInvertida.append(fila.dequeue())

# Reinsere os elementos na fila em ordem invertida
while listaInvertida:
    fila.enqueue(listaInvertida.pop())

print(f"fila invertida: {fila}")
    