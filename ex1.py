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
    
# Fim da Classe

# Escreva um programa que cria uma fila vazia e insere os números de 1 a 5 nessa fila. 

fila = Fila()

for num in range(1,6):
    fila.enqueue(num)
    
print("fila completa",fila)


# em seguida, remova os dois primeiros números da fila e exiba o conteúdo restante.

fila.dequeue()
fila.dequeue()

print("fila reduzida",fila)