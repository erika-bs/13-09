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
    
# Escreva um programa que cria uma fila vazia e insere 10 números aleatórios nessa fila. 
# Em seguida, remova todos os números pares da fila e exiba o conteúdo restante.

import random

fila = Fila()


for num in range(1,11):
    num = random.randint(1,500)
    fila.enqueue(num) 
    
print(fila)

filaImpar = Fila()

while not fila.is_empty():
    num = fila.dequeue()
    if num % 2 != 0:  
        filaImpar.enqueue(num)

# Atualiza a fila com os números restantes
fila = filaImpar

print("Fila após remover números pares:", fila)
    