class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    
class Fila:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, data):
        novo = Node(data)
        if not self.head:
            self.head = novo
            self.tail = novo
        else:
            self.tail.next = novo
            self.tail = novo

    def remove(self): 
        if self.head:
            removido = self.head.data
            self.head = self.head.next

            if self.head is None or self.head.next is None:
                 self.tail = self.head
            return removido
        else:
             return None
        
    def tamanhoElementar(self): ### OK!
        lentgh = 0
        aux = self.remove()
        if aux is not None:
            lentgh = lentgh + 1
            aux_fila = Fila()
            aux_fila.insert(aux)
            while True:
                aux = self.remove()
                if aux is not None:
                    lentgh = lentgh + 1
                    aux_fila.insert(aux)
                else:
                    break
            while True:
                aux = aux_fila.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
        return lentgh
    


###     COPIE A FUNÇÃO AQUI PARA TESTÁ-LA


    def imprimir(self):
        data = []
        no_atual = self.head
        while no_atual:
            data.append(no_atual.data)
            no_atual = no_atual.next
        print(f'Fila atual: {data}')


def main():
    fila = Fila()
    i=5
    while i <17:
        fila.insert(i)
        i+=1
    fila.insert(7)
    
    fila.imprimir()
    
    fila.imprimir()
    
main()


