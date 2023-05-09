import math
import random

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
                problema.solucao = Solucao(len(evisitados), ecaminho, problema.emeta)
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
        # meta dada essa profundidade l, então solução é nula (retorna ainda
        # quantidade de visitados para usar em Busca.bli)
        problema.solucao = Solucao(len(evisitados), None, problema.emeta)
        return False


    @staticmethod
    def bli(problema: Problema, maxAltura: int) -> bool:
        
        buscados = 0
        for i in range(0, maxAltura + 1):
            result = Busca.bpl(problema, i)
            buscados += problema.solucao.nvisitados

            if result == True:
                problema.solucao = Solucao(buscados, problema.solucao.cmeta, problema.emeta)
                return True

        problema.solucao = Solucao(buscados, None, problema.emeta)    
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
                problema.solucao = Solucao(len(evisitados), ecaminho, problema.emeta)
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
    def gulosa(problema: Problema) -> bool:
        # Tratar eavisitar como fila de prioridade
        # Ou seja, estruturar eavisitar ordenadamente
        # de forma que o estado com menor heurística
        # seja o primeiro elemento da lista e seu pai
        eavisitar = [(problema.einicial, None)]

        # Guarda as duplas dos estados visitados na busca
        evisitados = []

        # Enquanto tiver estados na fila de duplas estados a visitar
        while eavisitar:

            # Desenfila a próxima dupla de estado a buscar
            datual = eavisitar.pop(0)
            eatual, epai = datual

            # Marca a dupla atual como visitada
            # Adiciona datual no fim do possível caminho da solução
            evisitados.append(datual)

            if problema.teste_objetivo(eatual):
                ecaminho = []
                n = len(evisitados)

                while epai is not None:
                    for i in range(0, n):
                        if evisitados[i][0] == epai:
                            ipai = i
                            break
                    
                    ecaminho.append(eatual)
                    datual = evisitados[ipai]
                    eatual, epai = datual

                ecaminho.append(eatual)

                problema.solucao = Solucao(n, ecaminho[::-1], problema.emeta)

                return True

            # Caso contrário, operamos sob o estado atual para achar
            # novos estados de busca possíveis estados meta
            nestados = problema.operador(eatual)

            # Enfileire na fila de prioridade os estados e que ainda não foram visitados
            # Todos esses novos não-visitados tem +1 de altura
            aux = list(map(lambda de: de[0], evisitados))
            nvisitados = list(filter(lambda e: e not in aux, nestados))
            nvisitados = list(map(lambda e: (e, eatual), nvisitados))

            eavisitar.extend(nvisitados)
            eavisitar.sort(key = lambda de: de[0].h(problema.emeta))
        
        # Se estados a visitar está vazio, é porque não achou nenhum estado
        # meta dada essa profundidade l, então solução é nula
        return False
    

    @staticmethod
    def astar(problema: Problema) -> bool:
        # Tratar eavisitar como fila de prioridade
        # Ou seja, estruturar eavisitar ordenadamente
        # de forma que o estado com menor heurística
        # seja o primeiro elemento da lista e seu pai
        eavisitar = [(problema.einicial, None)]
        problema.einicial.g = 0

        # Guarda as duplas dos estados visitados na busca
        evisitados = []

        # Enquanto tiver estados na fila de duplas estados a visitar
        while eavisitar:

            # Desenfila a próxima dupla de estado a buscar
            datual = eavisitar.pop(0)
            eatual, epai = datual

            # Marca a dupla atual como visitada
            # Adiciona datual no fim do possível caminho da solução
            evisitados.append(datual)

            if problema.teste_objetivo(eatual):
                ecaminho = []
                n = len(evisitados)

                while epai is not None:
                    for i in range(0, n):
                        if evisitados[i][0] == epai:
                            ipai = i
                            break
                    
                    ecaminho.append(eatual)
                    datual = evisitados[ipai]
                    eatual, epai = datual

                ecaminho.append(eatual)

                problema.solucao = Solucao(n, ecaminho[::-1], problema.emeta)

                return True

            # Caso contrário, operamos sob o estado atual para achar
            # novos estados de busca possíveis estados meta
            nestados = problema.operador(eatual)

            # Enfileire na fila de prioridade os estados e que ainda não foram visitados
            # Todos esses novos não-visitados tem +1 de altura
            aux = list(map(lambda de: de[0], evisitados))
            nvisitados = list(filter(lambda e: e not in aux, nestados))

            for nv in nvisitados:
                nv.g = problema.relacao(nv, eatual) + eatual.g

            nvisitados = list(map(lambda e: (e, eatual), nvisitados))

            eavisitar.extend(nvisitados)
            eavisitar.sort(key = lambda de: de[0].g + de[0].h(problema.emeta))
        
        # Se estados a visitar está vazio, é porque não achou nenhum estado
        # meta dada essa profundidade l, então solução é nula
        return False


    @staticmethod
    def hill_climbing(problema: Problema, minimization = True) -> None:
        
        corrente = problema.einicial
        achou = False
        caminho = []
        
        caminho.append(corrente)

        while True:
            if problema.teste_objetivo(corrente):
                solucao = Solucao(len(caminho), caminho, problema.emeta)
                achou = True
                break

            suc = corrente.sucessor_hill_climbing(problema, minimization)

            if suc is None:
                solucao = Solucao(len(caminho), [corrente], problema.emeta)
                achou = False
                break

            corrente = suc
            caminho.append(corrente)

        problema.solucao = solucao
        return achou
    

    @staticmethod
    def hill_climbing_mov_lat(problema: Problema, minimization = True) -> None:
        
        problema.einicial.gera_aleatorio()
        corrente = problema.einicial
        achou = False
        mov_lat = False
        visitados = []
        caminho = []
        
        caminho.append(corrente)

        while True:
            if problema.teste_objetivo(corrente):
                solucao = Solucao(len(caminho), caminho, problema.emeta)
                achou = True
                break

            suc = corrente.sucessor_hill_climbing(problema, minimization)

            if suc is None:
                if mov_lat == True:
                    vizinhos = problema.operador(corrente)
                    nvisitados = list(filter(lambda e: e not in visitados, vizinhos))

                    if len(nvisitados) == 0:
                        problema.einicial.gera_aleatorio()
                        corrente = problema.einicial
                        caminho.clear()
                        visitados.clear()
                        mov_lat = True
                    else:
                        corrente = nvisitados[0]
                        mov_lat = False
                else:
                    problema.einicial.gera_aleatorio()
                    corrente = problema.einicial
                    caminho.clear()
                    visitados.clear()
                    mov_lat = True
            else:
                corrente = suc
            
            caminho.append(corrente)

        problema.solucao = solucao
        return achou


    @staticmethod
    def tempera_simulada(problema: Problema, l = 10**6, minimization = True) -> None:
        ecorrente = problema.einicial
        count = 1

        mapeamento = [100 * random.random() for i in range(0, l)]

        while mapeamento:
            T = mapeamento.pop()

            objetivou = problema.teste_objetivo(ecorrente)
            if T == 0 or objetivou:
                problema.solucao = Solucao(count, [ecorrente], problema.emeta)
                return objetivou

            proximo = random.choice(problema.operador(ecorrente))
            count += 1
            dE = proximo.h(problema.emeta) - ecorrente.h(problema.emeta)
            
            if dE > 0:
                ecorrente = proximo
            else:
                probabilidade = math.exp(dE / T)
                ecorrente = random.choices([ecorrente, proximo], weights=[1-probabilidade, probabilidade])[0]

        problema.solucao = Solucao(count, [ecorrente], problema.emeta)
        return False