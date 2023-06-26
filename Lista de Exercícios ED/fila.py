# Questão 01 

class Node:
    def __init__(self, elemento):
        self.data = elemento 
        self.next = None

class ListaEncadeada:
    
    def __init__(self):
        self.primeiro = None
        self.resto = None

     ### Q2 ###

    def pushWithClassLinkedList(self, e):
        novo = Node(e)
        if not self.primeiro:
            self.primeiro = novo
            self.resto = novo
        else:
            self.resto.next = novo
            self.resto = novo
    def pushWithArray(array, e):
        array.append(e)

    def insertWithLinkedList(self, e, posicao):
        if posicao < 0:
            raise ValueError("O índice deve ser maior ou igual a zero")
        novo = Node(e)
        if posicao == 0:
            novo.next = self.primeiro
            self.primeiro = novo
        else:
            atual = self.primeiro
            i = 0
            while atual and i < posicao - 1:
                atual = atual.next
                i += 1
            if not atual:
                raise ValueError("Índice fora do alcance")
            novo.next = atual.next
            atual.next = novo

    def insertWithArray(array, e, posicao):
        array.insert(posicao, e)

    
    ### Q3 ###

    def popWithClassLinkedList(self):
        if not self.primeiro:
            raise Exception('Lista vazia.')
        elemento = self.primeiro.elemento
        self.primeiro = self.primeiro.next
        return elemento
    def popWithArray(array):
        if not array:
            raise Exception('Array vazio.')
        return array.pop()

    def removeWithLinkedList(self, elemento): 
        if not self.primeiro:
            return None 
        else:
            elemento = self.primeiro.data
            self.primeiro = self.primeiro.next 
            if not self.primeiro:
                self.ultimo = None
            return elemento
    def removeWithArray(array, e, posicao):
        array.remove(posicao, e)
    

    
class Fila:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def imprimir(self): # OK!
        data = []
        no_atual = self.head
        while no_atual:
            data.append(no_atual.data)
            no_atual = no_atual.next
        print(f'Fila atual: {data}')
    
    def insert(self, data): # OK!
        novo = Node(data)
        if not self.head:
            self.head = novo
            self.tail = novo
        else:
            self.tail.next = novo
            self.tail = novo

    def remove(self): # OK!
        if self.head:
            removido = self.head.data
            self.head = self.head.next

            if self.head is None or self.head.next is None:
                 self.tail = self.head
            return removido
        else:
             return None
        
    ### Q4 ###

    def firstElementar(self):
        aux = self.remove()
        primeiro = aux
        if aux is not None:
            fila_aux = Fila()
            fila_aux.insert(aux)
            while True:
                aux = self.remove()
                if aux is not None:
                    fila_aux.insert(aux)
                else:
                    break
            while True:
                aux = fila_aux.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
        print(f'O primeiro elemento é: {primeiro}')
    
    def firstDiverso(self):
        if self.head is None:
            return None
        atual = self.head
        return print(atual.data)
    
    ### Q5 ###

    
    def isEmpty_Diversa(self):
        current=self.head
        if current is None:
            print ('esta vazia')
        else:
            print('não esta vazia')
        return False
    
    
    
    def isEmpty_Elementar(self):
        aux = self.remove()
        if aux:
            fila_nova = Fila() 
            fila_nova.insert(aux) 
            while True: 
                aux = self.remove() 
                if aux:
                    fila_nova.insert(aux) 
                else:
                    break
            while True:
                aux = fila_nova.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
        else:
            print('vazia')
        return False
    
    ### Q6 ### 
    def tamanho_Elementar(self): ### OK!
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
        print('O tamanho é: ', lentgh)

    def tamanho_Diverso(self):
        tam = 0
        current = self.head
        while current:
            tam += 1 
            current = current.next
        return print(tam)
    
    ### Q7 ###  
    def lastDiverso(self): # OK
        if self.head is None:
            return None
        atual = self.head
        while atual.next is not None:
            atual = atual.next
        return print(atual.data)
    
    def lastElementar(self): # OK
        aux = self.remove()
        if aux is not None:
            fila_aux = Fila()
            fila_aux.insert(aux)
            while True:
                aux = self.remove()
                if aux is not None:
                    fila_aux.insert(aux)
                    ultimo = aux
                else:
                    break
            while True:
                aux = fila_aux.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
        print(f'O ultimo elemento é: {ultimo}')

    ### Q8 ###
    def get_value_by_indexDiversa(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return print(current.data)
            current = current.next
            count += 1
        
        return None
    
    def get_value_by_indexElementar(self, index):
        vetor = 0
        aux = self.remove()
        if aux is not None:
            aux_fila = Fila()
            aux_fila.insert(aux)
            while True:
                aux = self.remove()
                if aux is not None:
                    aux_fila.insert(aux)
                    vetor+=1
                    if vetor == index:
                        return print(f'O valor na posição indicada é {aux}')
                else:
                    break
            while True:
                aux = aux_fila.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
        
     ### Q9 ###

    def get_index_by_valueElementar(self, value):
        index = 0
        aux = self.remove()
        if aux is not None:
            aux_fila = Fila()
            aux_fila.insert(aux)
            if aux == value: # caso o primeiro elemento seja o procurado
                posicao = index
            while True:
                aux = self.remove()
                if aux is not None:
                    aux_fila.insert(aux)
                    index+=1
                    if aux == value:
                        posicao = index
                else:
                    break
            while True:
                aux = aux_fila.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
            if UnboundLocalError:
                print('nao esta')
            else:
                return print(f'A posição do valor requerido é {posicao}')
    
    def get_index_by_value_Diversa(self, value):
        current = self.head
        index = 0

        while current:
            if current.data == value:
                return print(f"Está na posição {index}")
            current = current.next
            index += 1

        return print('O valor não está na fila')
    
    ### Q10 ###

    def get_AllIndexsByValue_Diversa(self, e):
        indexes = []
        current = self.head
        index = 0

        while current is not None:
            if current.data == e:
                indexes.append(index)
            current = current.next
            index += 1

        return print(indexes)
    
    def get_Allindex_by_valueElementar(self, value):
        posicoes = []
        index = 0

        aux = self.remove()
        if aux is not None:
            aux_fila = Fila()
            aux_fila.insert(aux)

            if aux == value: # caso o primeiro elemento seja o procurado
                posicoes = [index]

            while True:
                aux = self.remove()

                if aux is not None:
                    aux_fila.insert(aux)
                    index+=1

                    if aux == value:
                        if posicoes == []:
                            posicoes = [index]
                        else:
                            posicoes = posicoes + [index]
                else:
                    break
            while True:
                aux = aux_fila.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
            if not posicoes:
                print('nao esta na lista')
            else:
                return print(f'A posição do valor requerido é {posicoes}')
    
    ###Q11###

    def getValuesByIndexs_Diversa(self, positions):
        valores = []
        index = 0
        current = self.head

        while current:
            if index in positions:
                valores.append(current.data)
            current = current.next
            index+=1
        return print(valores)
    
    def getValuesByIndexs_Elementar(self, positions):
        valores = []

        index = 0
        aux = self.remove()

        if aux is not None:
            aux_fila = Fila()
            aux_fila.insert(aux)

            if index in positions:
                valores = [aux]

            while True:
                aux = self.remove()

                if aux is not None:
                    aux_fila.insert(aux)
                    index += 1

                    if index in positions:
                        valores += [aux]
                else:
                    break

            while True:
                aux = aux_fila.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break

        if not valores:
            print('As posições não estão na lista')
        else:
            print(f'Os valores das posições requeridas são: {valores}')

    
    ### Q12 ###
    
    def getValuesBySlice_Diversa(self, inicio, fim):
        valores = []
        index = 0
        current = self.head

        while current:
            if index >= inicio and index<= fim:
                valores.append(current.data)
            current = current.next
            index+=1
        return print(valores)
    
    def getValuesBySlice_Elementar(self, inicio, fim):
        valores = []

        index = 0
        aux = self.remove()

        if aux is not None:
            aux_fila = Fila()
            aux_fila.insert(aux)
            

            if index >= inicio and index<= fim:
                valores = [aux]

            while True:
                aux = self.remove()

                if aux is not None:
                    aux_fila.insert(aux)
                    index += 1

                    if index >= inicio and index<= fim:
                        valores += [aux]
                else:
                    break

            while True:
                aux = aux_fila.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break

        if not valores:
            print('As posições não estão na lista')
        else:
            print(f'Os valores das posições de {inicio} ate {fim} são: {valores}')

    ### Q13 ###

    def removeAll_Diversa(self):
        current = self.head
        while current:
            current = current.next
            self.remove()
        return  (current)

    def removeAll_Elementar(self):
        aux = self.remove()
        if aux:
            fila_nova = Fila() 
            fila_nova.insert(aux) 
            while True: 
                aux = self.remove() 
                if aux:
                    fila_nova.insert(aux) 
                else:
                    break
            while True:
                aux = fila_nova.remove()
                if aux is not None:
                    self.insert(aux)
                else:
                    break
        else:
            print('vazia')
        return False
    

    ###Q14###

    def removeByIndex_Diversa(self, indexes):
        current = self.head
        anterior = None
        count = 0
        removed_elements = []

        while current:
            if count in indexes:
                removed_elements.append(current.data)
                if anterior:
                    anterior.next = current.next
                    if current == self.tail:
                        self.tail = anterior
                else:
                    self.head = current.next
                    if not self.head:
                        self.tail = None
            else:
                anterior = current

            current = current.next
            count += 1

        return print(removed_elements)

    def removeByIndex_Elementar(self,index):
        i=0
        aux = self.remove()
        if i == index:
            removido=aux
            i+=1
        if aux is not None:
            aux_fila = Fila() 
            aux_fila.insert(aux)
            
            while True: 
                aux = self.remove() 
                if aux:
                    aux_fila.insert(aux)
                    i+=1
                    if i == index:
                        removido=aux
                    
                else:
                    break
            while True:
                aux = aux_fila.remove()
                if aux is not None:
                    if aux != removido:
                        self.insert(aux)
                    
                else:
                    break
            return print(removido)
    ###Q15###

    def removeByValueFirst_Diversa(self, value):
        current = self.head
        anterior = None
        while current:
            if current.data == value:
                removido = current.data
                if anterior:
                    anterior.next = current.next
                    if current == self.tail:
                        self.tail = anterior
                else:
                    self.head = current.next
                    if not self.head:
                        self.tail = None
                print(removido)
                break
            anterior= current
            current = current.next
        return None
    
    def removeByValueFirst_Elementar(self,value):
        removido = None
        posicao = -1

        aux_fila = Fila()

        while True:
            aux = self.remove()
            if aux is None:
                break
            if aux == value and posicao == -1:
                removido = aux
                posicao = 0
            else:
                aux_fila.insert(aux)
        while True:
            aux = aux_fila.remove()
            if aux is None:
                break
            self.insert(aux)
            if posicao!= -1:
                posicao +=1
        return print(removido)
    
    ###Q16###

    def removeAllByValue_Elementar(self,value):
        i=0
        aux = self.remove()
        if aux == value:
            removido=aux
            
        if aux is not None:
            aux_fila = Fila() 
            aux_fila.insert(aux)
            
            while True: 
                aux = self.remove() 
                if aux:
                    aux_fila.insert(aux)
                    i+=1
                    if aux == value:
                        removido=aux
                else:
                    break
            while True:
                aux = aux_fila.remove()
                if aux is not None:
                    if aux != removido:
                        self.insert(aux)
                        
                else:
                    break
            return print(removido)
        
    def removeAllByValue_Diversa(self, value):
        current = self.head
        anterior = None
        while current:
            if current.data == value:
                removido = current.data
                if anterior:
                    anterior.next = current.next
                    if current == self.tail:
                        self.tail = anterior
                else:
                    self.head = current.next
                    if not self.head:
                        self.tail = None
                print(removido)
            anterior= current
            current = current.next
        return None
    
    ###Q17###

    def removeByIndexes_Elementar(self, indexes):
        removed_elements = []
    
        aux_fila = Fila()
        aux = self.remove()
        current_index = 0
    
        while aux is not None:
            if current_index in indexes:
                removed_elements.append(aux)
            else:
                aux_fila.insert(aux)
            
            aux = self.remove()
            current_index += 1

        while True:
            aux = aux_fila.remove()
            if aux is not None:
                self.insert(aux)
            else:
                break

        return print(removed_elements)
    
    def removeByIndexes_Diversa(self, indexes):
        current = self.head
        anterior = None
        count = 0
        removed_elements = []

        while current:
            if count in indexes:
                removed_elements.append(current.data)
                if anterior:
                    anterior.next = current.next
                    if current == self.tail:
                        self.tail = anterior
                else:
                    self.head = current.next
                    if not self.head:
                        self.tail = None
            else:
                anterior = current

            current = current.next
            count += 1

        return print(removed_elements)
    
    ###Q18###

    def removeValuesBySlice_Diversa(self, inicio, fim):
        index = 0
        current = self.head
        prev = None

        while current and index < inicio:
            prev = current
            current = current.next
            index += 1

        while current and index < fim:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next
            current = current.next
            index += 1
            print(current.data)
        if current:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next
            current = current.next
        return

    def removeValuesBySlice_Elementar(self, inicio, fim):
        valores = []
        index = 0
        
        aux = self.remove()
        index_aux=[]
        if aux is not None:
            aux_fila = Fila()
            aux_fila.insert(aux)
            

            if index >= inicio and index<= fim:
                valores = [aux]
                index_aux=[index]

            while True:
                aux = self.remove()

                if aux is not None:
                    aux_fila.insert(aux)
                    index += 1

                    if index >= inicio and index<= fim:
                        valores += [aux]
                        index_aux+=[index]
                        
                else:
                    break
            index=0
            while True:
                aux = aux_fila.remove()
                if aux:
                    if index in index_aux:
                        index+=1
                    else:
                        self.insert(aux)
                        index+=1
                else:
                    break

        if not valores:
            print('As posições não estão na lista')
        else:
            print(f'Os valores das posições de {inicio} ate {fim} são: {valores}')
            print(f'index:{index}')
        return print(f'slice: {index_aux}') 
    
    ###Q19### aproveitadas do get value by index

    def setValueInIndex_Diversa(self, index, value):
        current = self.head
        count = 0
        while current:
            if count == index:
                current.data=value
                return print(current.data)
            current = current.next
            count += 1
        
        return None

    def setValueInIndex_Elementar(self, index, value):
        vetor = 0
        aux = self.remove()
        if aux is not None:
            aux_fila = Fila()
            aux_fila.insert(aux)
            while True:
                aux = self.remove()
                if aux is not None:
                    aux_fila.insert(aux)
                    
                else:
                    break

            while True:
                
                aux = aux_fila.remove()
                if aux is not None:
                    if vetor == index:
                        aux = value
                        self.insert(aux)
                        vetor+=1
                    else:
                        self.insert(aux)
                        vetor+=1
                else:
                    break
        return
    
    ###Q20###
    
    def setValuesInIndexes_Elementar(self, index, value):
        vetor = 0
        i=0

        aux = self.remove()
        if aux is not None:
            aux_fila = Fila()
            aux_fila.insert(aux)
            while True:
                aux = self.remove()
                if aux is not None:
                    aux_fila.insert(aux)
                    
                else:
                    break

            while True:
                
                aux = aux_fila.remove()
                if aux is not None:
                    if vetor in index:
                        aux = value[i]
                        self.insert(aux)
                        vetor+=1
                        i+=1
                    else:
                        self.insert(aux)
                        vetor+=1
                else:
                    break
        return
    
    def setValueInIndex_Diversa(self, index, value):
        current = self.head
        count = 0
        i=0
        while current:
            if count in index:
                current.data=value[i]
                i+=1
            current = current.next
            count += 1
            
        return None