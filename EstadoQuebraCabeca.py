import random
from Estado import Estado

class EstadoQuebraCabeca(Estado):

    # heuristica 01 consiste em contar quantas peças do estado atual
    # estão posicionadas corretamente comparado às posições do estado meta
    @staticmethod
    def h1(estado, meta) -> int:
        soma = 0
        n = len(estado.dados)

        # para cada elemento do estado atual, se aposição dele 
        # for igual ao da meta a soma é incrementada
        for i in range(0, n):
            for j in range(0, n):
                if estado.dados[i][j] != meta.dados[i][j]:
                    soma += 1

        return soma

    # heuristica 02 consiste em contar, para cada peça do estado atual, quantos
    # movimentos faltam para chegar ao estado meta
    @staticmethod
    def h2(estado, meta) -> int:
        soma = 0
        n = len(estado.dados)

        # para cada elemento do estado atual, verifica a posição dele,
        # conta-se quantos passos ele terá que fazer até o estado meta e 
        # é devolvida a soma de todos os passos necessários para cada elemento
        for i in range(0, n):
            for j in range(0, n):

                bof = False
                for k in range(0, n):
                    for l in range(0, n):
                        if estado.dados[i][j] == meta.dados[k][l]:
                            soma += abs(k - i) + abs(l - j)
                            bof = True
                            break
                    if bof:
                        break

        return soma
    

    def __init__(self, dados: list[object], heuristica='h1') -> None:
        #n = len(dados)
        #if n != 3 or n != 4 or any(map(lambda l: len(l) != 3 or len(l) != 4, dados)):
        #    raise Exception
        
        super().__init__(dados)

        if heuristica == 'h2':
            self.__h__ = EstadoQuebraCabeca.h2
        else:
            self.__h__ = EstadoQuebraCabeca.h1
        

    def h(self, meta) -> int:
        return self.__h__(self, meta)
    
    def get_dados(self):
        return self.dados
    
    def gera_aleatorio(self):
        n = len(self.dados)
        novos_dados = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        options = [i for i in range(0, n * n)]

        for i in range(0, n):
            for j in range(0, n):
                num = random.choice(options)
                novos_dados[i][j]  = num
                options.remove(num)


        self.dados = novos_dados

    def __eq__(self, other):
        n = len(self.dados)

        for i in range(0, n):
            for j in range(0, n):
                if other.dados[i][j] != self.dados[i][j]:
                    return False
                
        return True
    
    def __str__(self):
        s = ''

        if self.g is not None:
            s += '-------------------------\ng = '
            s += str(self.g)

        if self.dados is not None:
            s += '\n\nMatriz = \n'
            for j in range(0, len(self.dados)):
                for k in range(0, len(self.dados)):
                    s += str(self.dados[j][k])
                    s += ' '
                s += '\n'
            s += '\n-------------------------\n'

        return s