from Problema import Problema
from Solucao import Solucao
from Estado import Estado

class Busca:


    @staticmethod
    def bpl(problema: Problema, l: int) -> bool:
        # Tratar eavisitar como pilha

        # Como precisamos da altura de cada estado na pilha de busca,
        # guardamos uma pilha de duplas = (altura_estado, estado)
        # Inicialmente, essa pilha tem o estado inicial do problema
        eavisitar = [(0, problema.einicial)]

        # Guarda os estados visitados na busca
        evisitados = []

        # Guarda o caminho da solução, se encontrada
        ecaminho = []

        # Enquanto tiver estados na pilha de estados a visitar
        while eavisitar:
            
            # Desempilha o próximo estado a buscar
            natual, eatual = eavisitar.pop()

            # Marca atual como visitado
            # Adiciona atual no fim do possível caminho da solução
            evisitados.append(eatual)
            ecaminho.append(eatual)

            # Se chegamos em um estado meta, paramos a busca,
            # assim, eatual é o estado meta, dessa forma, 
            # retornamos que a busca foi sucedida (True)
            if problema.teste_objetivo(eatual):
                problema.solucao = Solucao(len(evisitados), ecaminho)
                return True

            # Se a altura do estado atual é l, podamos essa busca,
            # isto é, não continuamos a descer na árvore de busca
            if natual == l:

                # Como não achou caminho, tira o último estado do
                # caminho, sendo esse último o estado atual
                ecaminho.pop()
                continue

            # Caso contrário, operamos sob o estado atual para achar
            # novos estados de busca possíveis estados meta
            nestados = problema.operador(eatual)
            
            # Filtra esses novos estados para novos estados que não foram
            # visitados ainda
            nvisitados = list(filter(lambda e: e not in evisitados, nestados))

            # Se não tem mais nenhum filho não-visitado (nvisitado é vazio),
            # então o estado atual não faz parte do caminho solução, logo
            # devemos tirar ele do caminho de estados (ele está no final)
            if not nvisitados:
                ecaminho.pop()
            else:
                # Empilhe na pilha os estados e que ainda não foram visitados
                # (cada um tem altura +1 em relação ao eatual)
                eavisitar.extend(map(lambda e: (natual + 1, e), nvisitados))

        # Se estados a visitar está vazio, é porque não achou nenhum estado
        # meta dada essa profundidade l, então solução é nula
        return False

    @staticmethod
    def bli(problema: Problema, maxAltura: int) -> bool:
        for i in range(0, maxAltura + 1):
            result = Busca.bpl(problema, i)

            if result == True:
                return True
            
        return False

    @staticmethod
    def blarg(problema: Problema) -> bool:
        # Tratar estadoa a visitar como fila

        # Então, guardamos uma fila de estados
        # Inicialmente, essa fila tem o estado inicial do problema
        eavisitar = [problema.einicial]

        # Guarda os estados visitados na busca
        evisitados = []

        # Guarda o caminho da solução, se encontrada
        ecaminho = []

        # Enquanto tiver estados na fila de estados a visitar
        while eavisitar:

            # Desenfila o próximo estado a buscar
            eatual = eavisitar.pop(0)

            # Marca atual como visitado
            # Adiciona atual no fim do possível caminho da solução
            evisitados.append(eatual)
            ecaminho.append(eatual)

            # Se chegamos em um estado meta, paramos a busca,
            # assim, eatual é o estado meta, dessa forma,
            # retornamos que a busca foi sucedida (True)
            if problema.teste_objetivo(eatual):
                problema.solucao = Solucao(len(evisitados), ecaminho)
                return True


            # Caso contrário, operamos sob o estado atual para achar
            # novos estados de busca possíveis estados meta
            nestados = problema.operador(eatual)

            # Enfileire na fila de prioridade os estados e que ainda não foram visitados
            # Todos esses novos não-visitados tem +1 de altura
            nvisitados = list(filter(lambda e: e not in evisitados, nestados))
            eavisitar.extend(nvisitados)

            # Se não tem mais nenhum filho não-visitado (nvisitado é vazio),
            # então o estado atual não faz parte do caminho solução, logo
            # devemos tirar ele do caminho de estados (ele está no final)
            if not nvisitados:
                ecaminho.pop()

        # Se estados a visitar está vazio, é porque não achou nenhum estado
        # meta dada essa profundidade l, então solução é nula
        return False


    @staticmethod
    def gulosa(problema: Problema) -> None:
        # Tratar eavisitar como fila de prioridade
        # Ou seja, estruturar eavisitar ordenadamente
        # de forma que o estado com menor heurística
        # seja o primeiro elemento da lista
        eavisitar = [problema.einicial]

        # Guarda os estados visitados na busca
        evisitados = []

        # Guarda o caminho da solução, se encontrada
        ecaminho = []

        # Enquanto tiver estados na fila de estados a visitar
        while eavisitar:

            # Desenfila o próximo estado a buscar
            eatual = eavisitar.pop(0)

            # Marca atual como visitado
            # Adiciona atual no fim do possível caminho da solução
            evisitados.append(eatual)
            ecaminho.append(eatual)

            # Se chegamos em um estado meta, paramos a busca,
            # assim, eatual é o estado meta, dessa forma,
            # retornamos que a busca foi sucedida (True)
            if problema.teste_objetivo(eatual):
                problema.solucao = Solucao(len(evisitados), ecaminho)
                return True

            # Caso contrário, operamos sob o estado atual para achar
            # novos estados de busca possíveis estados meta
            nestados = problema.operador(eatual)

            # Enfileire na fila de prioridade os estados e que ainda não foram visitados
            # Todos esses novos não-visitados tem +1 de altura
            nvisitados = list(filter(lambda e: e not in evisitados, nestados))

            # Se não tem mais nenhum filho não-visitado (nvisitado é vazio),
            # então o estado atual não faz parte do caminho solução, logo
            # devemos tirar ele do caminho de estados (ele está no final)
            if not nvisitados:
                ecaminho.pop()
            else:
                nvisitados.sort(key = lambda e: e.h())
                eavisitar.extend(nvisitados)
        
        # Se estados a visitar está vazio, é porque não achou nenhum estado
        # meta dada essa profundidade l, então solução é nula
        return False


    @staticmethod
    def astar(problema: Problema) -> None:
        pass

    @staticmethod
    def se(problema: Problema) -> None:
        pass

