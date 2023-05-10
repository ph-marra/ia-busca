from Problema import Problema
from EstadoLabirinto import EstadoLabirinto
import copy

class Labirinto(Problema):


    def __init__(self, einicial: EstadoLabirinto, emeta: EstadoLabirinto) -> None:

        x, y = len(einicial.dados), len(einicial.dados[0])
        for i in range(0, x):
            for j in range(0, y):
                if einicial.dados[i][j] == 2:
                    einicial.dados[i][j] *= 10
                if emeta.dados[i][j] == 3:
                    emeta.dados[i][j] *= 10

        super().__init__(einicial, None, emeta)


    def teste_objetivo(self, estado: EstadoLabirinto) -> bool:

        x, y = len(estado.dados), len(estado.dados[0])
        for i in range(0, x):
            for j in range(0, y):
                if estado.dados[i][j] == 30:
                    return True
                
        return False
        

    def operador(self, estado: EstadoLabirinto) -> list[EstadoLabirinto]:

        x, y = len(estado.dados), len(estado.dados[0])
        for i in range(0, x):
            for j in range(0, y):
                if estado.dados[i][j] == 10 or estado.dados[i][j] == 20 or estado.dados[i][j] == 30:
                    ip, jp = i, j
                    break

        vs = [(ip-1, jp), (ip+1, jp), (ip, jp-1), (ip, jp+1)]
        vs = list(filter(lambda v: v[0] >= 0 and v[0] < x and v[1] >= 0 and v[1] < y and estado.dados[v[0]][v[1]] != 0, vs))
        
        nestados = []
        for ie, je in vs:
            ne = copy.deepcopy(estado.dados)
            ne[ip][jp] = int(ne[ip][jp] / 10)
            ne[ie][je] *= 10

            nestados.append(EstadoLabirinto(ne))

        return nestados
    
    def relacao(self, estado1: EstadoLabirinto, estado2: EstadoLabirinto) -> int:
        return 1
        


