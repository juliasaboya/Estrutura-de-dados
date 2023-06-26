class Node:
    def __init__(self, e):
        self.data = e 
        self.next = None

class Pilha:
    def __init__(self):
        self.primeiro = None
        self.tail = None

    def push(self,e): 
        novo = Node(e)
        if not self.primeiro:
            self.primeiro = novo 
            self.tail = novo 
        else:
            novo.next = self.primeiro 
            self.primeiro = novo

    def pop(self): 
        if not self.primeiro:
            return None 
        else:
            e = self.primeiro.data 
            self.primeiro = self.primeiro.next 
            if not self.primeiro:
                self.tail = None
            return e
        
    ### Q4 ###

    def peek_Diversa (self):
        if not self.primeiro:
            return None
        else:
            return print(self.primeiro.data)
    
    def peek_Elementar(self):
        peek = self.pop()
        if peek is None:
            return print('pilha vazia')
        else:
            self.push(peek)
            return print(f'o primeiro elemento é {peek}')
    
    ### Q5 ###

    
    def isEmpty_Diversa(self):
        if not self.primeiro:
            return print('vazia')
        else:
            return print('not empty')
    
    
    def isEmpty_Elementar(self):
        aux = self.pop()
        if aux is None:
            print('A pilha está vazia')
            return True
        else:
            self.push(aux)
        return print('not empty')
    
    ###Q6###

    def tamanho_Elementar(self):
        tam=0
        aux = self.pop()
        if aux:
            tam+=1
            aux_pilha = Pilha()
            aux_pilha.push(aux)
            while True:
                aux = self.pop()
                if aux:
                    tam+=1
                    aux_pilha.push(aux)
                else:
                    break
            while True:
                aux = aux_pilha.pop()
                if aux:
                    self.push(aux)
                else:
                    break
        return print(f'o tamanho é {tam}')
    
    def tamanho_Diverso(self):
        tam = 0
        current = self.primeiro
        while current:
            current = current.next
            tam+=1

        return print(tam)
    
    ###Q7###

    def lastDiverso(self): # OK
        if self.primeiro is None:
            return None
        atual = self.primeiro
        while atual.next is not None:
            atual = atual.next
        return print(atual.data)
    
    def lastElementar(self): # OK
        aux = self.pop()
        if aux:
            pilha_aux = Pilha()
            pilha_aux.push(aux)
            while True:
                aux = self.pop()
                if aux:
                    pilha_aux.push(aux)
                    ultimo = aux
                else:
                    break
            while True:
                aux = pilha_aux.pop()
                if aux:
                    self.push(aux)
                else:
                    break
        print(f'O ultimo elemento é: {ultimo}')

    ### Q8 ###
    def getValueByIndex_Diversa(self, index):
        current = self.primeiro
        count = 0
        while current:
            if count == index:
                return print(f'diversa:{current.data}')
            current = current.next
            count += 1
        
        return None
    
    def getValueByIndex_Elementar(self, index):
        vetor = 0
        aux = self.pop()
        if aux is not None:
            pilha_aux = Pilha()
            pilha_aux.push(aux)
            while True:
                aux = self.pop()
                if aux is not None:
                    pilha_aux.push(aux)
                    vetor+=1
                    if vetor == index:
                        print(f'elementar: {aux}')
                else:
                    break

            while True:
                aux = pilha_aux.pop()
                if aux:
                    self.push(aux)
                else:
                    break
        return aux
    
    ### Q9 ###

    def getIndexByValue_Elementar(self, value):
        index = 0
        aux = self.pop()
        if aux is not None:
            pilha_aux = Pilha()
            pilha_aux.push(aux)
            if aux == value: # caso o primeiro elemento seja o procurado
                posicao = index
            while True:
                aux = self.pop()
                if aux is not None:
                    pilha_aux.push(aux)
                    index+=1
                    if aux == value:
                        posicao = index
                else:
                    break
            while True:
                aux = pilha_aux.pop()
                if aux is not None:
                    self.push(aux)
                else:
                    break
        if aux is UnboundLocalError:
            print('nao esta')
        else:
            return print(f'A posição do valor requerido é {posicao}')
    
    def getIndexByValue_Diversa(self, value):
        current = self.primeiro
        index = 0

        while current:
            if current.data == value:
                return print(f"Está na posição {index}")
            current = current.next
            index += 1

        return print('O valor não está na fila')
    
    ### Q10 ###

    def getAllIndexsByValue_Diversa(self, e):
        indexes = []
        current = self.primeiro
        index = 0

        while current is not None:
            if current.data == e:
                indexes.append(index)
            current = current.next
            index += 1

        return print(f'diversa:{indexes}')
    
    def getAllIndexsByValue_Elementar(self, value):
        posicoes = []
        index = 0

        aux = self.pop()
        if aux is not None:
            pilha_aux = Pilha()
            pilha_aux.push(aux)

            if aux == value: # caso o primeiro elemento seja o procurado
                posicoes = [index]

            while True:
                aux = self.pop()

                if aux is not None:
                    pilha_aux.push(aux)
                    index+=1

                    if aux == value:
                        if posicoes == []:
                            posicoes = [index]
                        else:
                            posicoes = posicoes + [index]
                else:
                    break
            while True:
                aux = pilha_aux.pop()
                if aux is not None:
                    self.push(aux)
                else:
                    break
            if not posicoes:
                print('nao esta na lista')
            else:
                return print(f'Elementar {posicoes}')
            
    ###Q11###

    def getValuesByIndexs_Diversa(self, positions):
        valores = []
        index = 0
        current = self.primeiro

        while current:
            if index in positions:
                valores.append(current.data)
            current = current.next
            index+=1
        return print(valores)
    
    def getValuesByIndexs_Elementar(self, positions):
        valores = []

        index = 0
        aux = self.pop()

        if aux is not None:
            pilha_aux = Pilha()
            pilha_aux.push(aux)

            if index in positions:
                valores = [aux]

            while True:
                aux = self.pop()

                if aux is not None:
                    pilha_aux.push(aux)
                    index += 1

                    if index in positions:
                        valores += [aux]
                else:
                    break

            while True:
                aux = pilha_aux.pop()
                if aux is not None:
                    self.push(aux)
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
        current = self.primeiro

        while current:
            if index >= inicio and index<= fim:
                valores.append(current.data)
            current = current.next
            index+=1
        return print(f'diversa:{valores}')
    
    def getValuesBySlice_Elementar(self, inicio, fim):
        valores = []

        index = 0
        aux = self.pop()

        if aux is not None:
            pilha_aux = Pilha()
            pilha_aux.push(aux)
            

            if index >= inicio and index<= fim:
                valores = [aux]

            while True:
                aux = self.pop()

                if aux is not None:
                    pilha_aux.push(aux)
                    index += 1

                    if index >= inicio and index<= fim:
                        valores += [aux]
                else:
                    break

            while True:
                aux = pilha_aux.pop()
                if aux is not None:
                    self.push(aux)
                else:
                    break

        if not valores:
            print('As posições não estão na lista')
        else:
            print(f'elementar: {valores}')


    ### Q13 ###

    def removeAll_Diversa(self):
        current = self.primeiro
        while current:
            current = current.next
            self.pop()
        return print(f'diversa:{current}')

    def removeAll_Elementar(self):
        aux = self.pop()
        if aux:
            pilha_aux = Pilha() 
            pilha_aux.push(aux) 
            while True: 
                aux = self.pop() 
                if aux:
                    pilha_aux.push(aux) 
                else:
                    break
        else:
            print('elementar: vazia')
        return False
    
    ###Q14###

    def removeByIndex_Diversa(self, indexes): # deve ser usado array para 1 elemento
        current = self.primeiro
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
                    self.primeiro = current.next
                    if not self.primeiro:
                        self.tail = None
            else:
                anterior = current

            current = current.next
            count += 1

        return print(f'diversa: {removed_elements}')

    def removeByIndex_Elementar(self,index):
        i=0
        aux = self.pop()
        if i == index:
            removido=aux
            i+=1
        if aux is not None:
            pilha_aux = Pilha() 
            pilha_aux.push(aux)
            
            while True: 
                aux = self.pop() 
                if aux:
                    pilha_aux.push(aux)
                    i+=1
                    if i == index:
                        removido=aux
                    
                else:
                    break
            while True:
                aux = pilha_aux.pop()
                if aux is not None:
                    if aux != removido:
                        self.push(aux)
                    
                else:
                    break
            return print(removido)
        

     ###Q15###

    def removeByValueFirst_Diversa(self, value):
        current = self.primeiro
        anterior = None
        while current:
            if current.data == value:
                removido = current.data
                if anterior:
                    anterior.next = current.next
                    if current == self.tail:
                        self.tail = anterior
                else:
                    self.primeiro = current.next
                    if not self.primeiro:
                        self.tail = None
                print(removido)
                break
            anterior= current
            current = current.next
        return None
    
    def removeByValueFirst_Elementar(self,value):
        removido = None
        posicao = -1

        pilha_aux = Pilha()

        while True:
            aux = self.pop()
            if aux is None:
                break
            if aux == value and posicao == -1:
                removido = aux
                posicao = 0
            else:
                pilha_aux.push(aux)
        while True:
            aux = pilha_aux.pop()
            if aux is None:
                break
            self.push(aux)
            if posicao!= -1:
                posicao +=1
        return print(removido)
    

        ###Q16###

    def removeAllByValue_Elementar(self,value):
        i=0
        aux = self.pop()
        if aux == value:
            removido=aux
            
        if aux is not None:
            pilha_aux = Pilha() 
            pilha_aux.push(aux)
            
            while True: 
                aux = self.pop() 
                if aux:
                    pilha_aux.push(aux)
                    i+=1
                    if aux == value:
                        removido=aux
                else:
                    break
            while True:
                aux = pilha_aux.pop()
                if aux is not None:
                    if aux != removido:
                        self.push(aux)
                        
                else:
                    break
            return print(removido)
        
    def removeAllByValue_Diversa(self, value):
        current = self.primeiro
        anterior = None
        while current:
            if current.data == value:
                removido = current.data
                if anterior:
                    anterior.next = current.next
                    if current == self.tail:
                        self.tail = anterior
                else:
                    self.primeiro = current.next
                    if not self.primeiro:
                        self.tail = None
                print(removido)
            anterior= current
            current = current.next
        return None


    ###Q17###

    def removeByIndexes_Elementar(self, indexes):
        removed_elements = []
    
        pilha_aux = Pilha()
        aux = self.pop()
        current_index = 0
    
        while aux is not None:
            if current_index in indexes:
                removed_elements.append(aux)
            else:
                pilha_aux.push(aux)
            
            aux = self.pop()
            current_index += 1

        while True:
            aux = pilha_aux.pop()
            if aux is not None:
                self.push(aux)
            else:
                break

        return print(f'removendo: {removed_elements}')
    
    def removeByIndexes_Diversa(self, indexes):
        current = self.primeiro
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
                    self.primeiro = current.next
                    if not self.primeiro:
                        self.tail = None
            else:
                anterior = current

            current = current.next
            count += 1

        return print(f'removendo: {removed_elements}')


    ###Q18###

    def removeValuesBySlice_Diversa(self, inicio, fim):
        index = 0
        current = self.primeiro
        prev = None

        while current and index <inicio:
            prev = current
            current = current.next
            index += 1
            
        while current and index < fim:
            if prev:
                prev.next = current.next
            else:
                self.primeiro = current.next
            current = current.next
            index += 1
            
            
        if current:
            if prev:
                prev.next = current.next
            else:
                self.primeiro = current.next
            current = current.next
        return print()

    def removeValuesBySlice_Elementar(self, inicio, fim):
        valores = []
        index = 0
        
        aux = self.pop()
        index_aux=[]
        
        if aux is not None:
            pilha_aux = Pilha()
            pilha_aux.push(aux)
            

            if index >= inicio and index<= fim:
                valores = [aux]
                index_aux=[index]

            while True:
                aux = self.pop()

                if aux is not None:
                    pilha_aux.push(aux)
                    index += 1

                    if index >= inicio and index<= fim:
                        valores += [aux]
                        index_aux+=[index]
                        
                else:
                    break
            
            while True:
                aux = pilha_aux.pop()
                if aux:
                    if index in index_aux:
                        index-=1
                    else:
                        self.push(aux)
                        index-=1
                else:
                    break

        if not valores:
            print('As posições não estão na lista')
        else:
            print(f'elementar: {valores}')
        return 


    ###Q19###

    def setValueInIndex_Diversa(self, index, value):
        current = self.primeiro
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
        aux = self.pop()
        if aux is not None:
            pilha_aux = Pilha()
            pilha_aux.push(aux)
            while True:
                aux = self.pop()
                if aux is not None:
                    pilha_aux.push(aux)
                    vetor+=1
                else:
                    break
            
            while True:
                
                aux = pilha_aux.pop()
                if aux is not None:
                    if vetor == index:
                        aux = value
                        self.push(aux)
                        vetor-=1
                    else:
                        self.push(aux)
                        vetor-=1
                else:
                    break
        return
    
    ###Q20###
    
    def setValuesInIndexes_Elementar(self, index, value):
        vetor = 0
        
        tam_valores=len(value)
        
        
        aux = self.pop()
        if aux is not None:
            pilha_aux = Pilha()
            pilha_aux.push(aux)
            while True:
                aux = self.pop()
                if aux is not None:
                    pilha_aux.push(aux)
                    vetor+=1
                else:
                    break

            i=tam_valores-1
            while True:
                aux = pilha_aux.pop()
                if aux is not None:
                    if vetor in index:
                        aux = value[i]
                        self.push(aux)
                        vetor-=1
                        i-=1
                    else:
                        self.push(aux)
                        vetor-=1
                else:
                    break
        return
    
    def setValuesInIndexes_Diversa(self, index, value):
        current = self.primeiro
        count = 0
        i=0
        while current:
            if count in index:
                current.data=value[i]
                i+=1
            current = current.next
            count += 1
            
        return None



### apenas para imprimir no main com ARRAY
    def imprimir(self):
        data = []
        no_atual = self.primeiro
        while no_atual:
            data.append(no_atual.data)
            no_atual = no_atual.next
        print(f'Pilha atual: {data}')
    
def main():
    pilha = Pilha()
    i=1
    while i<11:
        pilha.push(i)
        i+=1
    pilha.push(6)
    pilha.push(3)
    pilha.imprimir()
    
    
    
    pilha.setValuesInIndexes_Elementar([0,1,2],[1,2,3])
    
    
    pilha.imprimir()
    return 
main()