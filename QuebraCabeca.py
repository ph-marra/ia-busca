from Problema import Problema
from EstadoQuebraCabeca import EstadoQuebraCabeca
import copy

class QuebraCabeca(Problema):


    def __init__(self, einicial: EstadoQuebraCabeca, emeta: EstadoQuebraCabeca) -> None:       
        super().__init__(einicial, emeta)


    def teste_objetivo(self, estado: EstadoQuebraCabeca) -> bool:
        n = len(estado.dados)
        for i in range(0, n):
            for j in range(0, n):
                if estado.dados[i][j] != self.emeta.dados[i][j]:
                    return False
                
        return True
        

    def operador(self, estado: EstadoQuebraCabeca) -> list[EstadoQuebraCabeca]:
        tam = len(estado.dados)

        for i in range(0, tam):
            for j in range(0, tam):
                if estado.dados[i][j] == 0:
                    vi, vj = i, j

        # ncoords são as tuplas (x,y) com as coordenadas de onde
        # o valor 0 (vazio) pode ser trocado
        ncoords = [(vi-1, vj), (vi, vj-1), (vi, vj+1), (vi+1, vj)]
        ncoords = list(filter(lambda n: n[0] >= 0 and n[0] < tam and n[1] >= 0 and n[1] < tam, ncoords))

        nestados = []

        # x, y onde o 0 tem que ir
        for x, y in ncoords:
            nc = copy.deepcopy(estado.dados)
            nc[vi][vj] = nc[x][y]
            nc[x][y] = 0

            nestados.append(nc)

        return nestados
