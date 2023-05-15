import math
import random

from Problema import Problema
from Solucao import Solucao
from Estado import Estado

class Busca:


    @staticmethod
    def bpl(problema: Problema, l: int) -> bool:
        eavisitar = [(0, problema.einicial)]
        evisitados = []
        ecaminho = []

        while eavisitar:
            
            natual, eatual = eavisitar.pop()

            evisitados.append(eatual)
            ecaminho.append(eatual)

            if problema.teste_objetivo(eatual):
                problema.solucao = Solucao(len(evisitados), ecaminho, problema.emeta)
                return True

            if natual == l:

                ecaminho.pop()
                continue

            nestados = problema.operador(eatual)
            
            nvisitados = list(filter(lambda e: e not in evisitados, nestados))

            if not nvisitados:
                ecaminho.pop()
            else:
                eavisitar.extend(map(lambda e: (natual + 1, e), nvisitados))

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
        eavisitar = [problema.einicial]
        evisitados = []
        ecaminho = []

        while eavisitar:

            eatual = eavisitar.pop(0)

            evisitados.append(eatual)
            ecaminho.append(eatual)

            if problema.teste_objetivo(eatual):
                problema.solucao = Solucao(len(evisitados), ecaminho, problema.emeta)
                return True


            nestados = problema.operador(eatual)

            nvisitados = list(filter(lambda e: e not in evisitados, nestados))
            eavisitar.extend(nvisitados)

            if not nvisitados:
                ecaminho.pop()

        return False


    @staticmethod
    def gulosa(problema: Problema) -> bool:
        eavisitar = [(problema.einicial, None)]

        evisitados = []

        while eavisitar:

            datual = eavisitar.pop(0)
            eatual, epai = datual

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

            nestados = problema.operador(eatual)

            aux = list(map(lambda de: de[0], evisitados))
            nvisitados = list(filter(lambda e: e not in aux, nestados))
            nvisitados = list(map(lambda e: (e, eatual), nvisitados))

            eavisitar.extend(nvisitados)
            eavisitar.sort(key = lambda de: de[0].h(problema.emeta))
        
        return False
    

    @staticmethod
    def astar(problema: Problema) -> bool:
        eavisitar = [(problema.einicial, None)]
        problema.einicial.g = 0

        evisitados = []

        while eavisitar:
            datual = eavisitar.pop(0)
            eatual, epai = datual

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

            nestados = problema.operador(eatual)

            aux = list(map(lambda de: de[0], evisitados))
            nvisitados = list(filter(lambda e: e not in aux, nestados))

            for nv in nvisitados:
                nv.g = problema.relacao(nv, eatual) + eatual.g

            nvisitados = list(map(lambda e: (e, eatual), nvisitados))

            eavisitar.extend(nvisitados)
            eavisitar.sort(key = lambda de: de[0].g + de[0].h(problema.emeta))
        
        return False


    @staticmethod
    def subida_encosta(problema: Problema, minimization = True) -> None:
        
        eatual = problema.einicial
        achou = False
        caminho = []
        
        caminho.append(eatual)

        while True:
            if problema.teste_objetivo(eatual):
                solucao = Solucao(len(caminho), caminho, problema.emeta)
                achou = True
                break

            suc = eatual.sucessor_hill_climbing(problema, minimization)

            if suc is None:
                solucao = Solucao(len(caminho), caminho, problema.emeta)
                achou = False
                break

            eatual = suc
            caminho.append(eatual)

        problema.solucao = solucao
        return achou
    

    @staticmethod
    def subida_encosta_mov_lat(problema: Problema, minimization = True) -> None:
        
        problema.einicial.gera_aleatorio()
        eatual = problema.einicial
        achou = False
        mov_lat = False
        evisitados = []
        caminho = []
        
        caminho.append(eatual)

        while True:
            if problema.teste_objetivo(eatual):
                solucao = Solucao(len(caminho), caminho, problema.emeta)
                achou = True
                break

            suc = eatual.sucessor_hill_climbing(problema, minimization)

            if suc is None:
                if mov_lat == True:
                    vizinhos = problema.operador(eatual)
                    nvisitados = list(filter(lambda e: e not in evisitados, vizinhos))

                    if len(nvisitados) == 0:
                        problema.einicial.gera_aleatorio()
                        eatual = problema.einicial
                        caminho.clear()
                        evisitados.clear()
                        mov_lat = True
                    else:
                        eatual = nvisitados[0]
                        mov_lat = False
                else:
                    problema.einicial.gera_aleatorio()
                    eatual = problema.einicial
                    caminho.clear()
                    evisitados.clear()
                    mov_lat = True
            else:
                eatual = suc
            
            caminho.append(eatual)

        problema.solucao = solucao
        return achou


    @staticmethod
    def recristalizacao_simulada(problema: Problema, l = 10**6, minimization = True) -> None:
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