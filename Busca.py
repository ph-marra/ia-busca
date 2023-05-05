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
        # meta dada essa profundidade l, então solução é nula (retorna ainda
        # quantidade de visitados para usar em Busca.bli)
        problema.solucao = Solucao(len(evisitados), None)
        return False

    @staticmethod
    def bli(problema: Problema, maxAltura: int) -> bool:
        
        buscados = 0
        for i in range(0, maxAltura + 1):
            result = Busca.bpl(problema, i)
            buscados += problema.solucao.nvisitados

            if result == True:
                problema.solucao = Solucao(buscados, problema.solucao.cmeta)
                return True

        problema.solucao = Solucao(buscados, None)    
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

                problema.solucao = Solucao(n, ecaminho[::-1])

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
    def astar(problema: Problema) -> None:
        pass

    @staticmethod
    def hill_climbing(problema: Problema, minimization = True) -> None:
        
        corrente = problema.einicial
        achou = False
        caminho = []
        
        caminho.append(corrente)

        while True:
            if problema.teste_objetivo(corrente):
                solucao = Solucao(len(caminho), caminho)
                achou = True
                break

            suc = corrente.sucessor_hill_climbing(problema, minimization)

            if suc is None:
                solucao = Solucao(len(caminho), [corrente])
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
                solucao = Solucao(len(caminho), caminho)
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
    def astar(problema: Problema) -> None:
        pass

    @staticmethod
    def hill_climbing_huryel(problema: Problema, minimization = True) -> None:
        
        eatual = problema.einicial
        count = 0

        while True:
            count += 1
            eavisitar = problema.operador(eatual)
            
            best_successor = eavisitar[0]
            broke_condition = True

            eavisitar = eavisitar[1:]

            for est in eavisitar:
                if minimization == True:
                    if est.h(problema.emeta) < best_successor.h(problema.emeta):
                        best_successor = est
                        broke_condition = best_successor.h(problema.emeta) < eatual.h(problema.emeta)
                else:
                    if est.h(problema.emeta) > best_successor.h(problema.emeta):
                        best_successor = est
                        broke_condition = best_successor.h(problema.emeta) > eatual.h(problema.emeta)
            # print(eatual)
            # print(eatual.h(problema.emeta))
            # print(broke_condition)

            if broke_condition and best_successor.h(problema.emeta) != 0:
                eatual = best_successor
            else:
                break
                
                
        problema.solucao = Solucao(count, [best_successor])
        return True if best_successor.h(problema.emeta) == 0 else False

