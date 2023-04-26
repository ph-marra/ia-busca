import Problema
import Estado

class QuebraCabeca(Problema):


    def __init__(self) -> None:
        einicial = Estado([
                    [2, 8, 3],
                    [1, 6, 4],
                    [7, 0, 5]
                   ])
        
        super().__init__(einicial)

    
    def teste_objetivo(self, estado: Estado) -> bool:
        meta = Estado([[1, 2, 3],
                [8, 0, 4],
                [7, 6, 5],
               ])
        
        n = len(self.estado.dados)
        for i in range(0, n):
            for j in range(0, n):
                if self.einicial.dados[i][j] != meta.dados[i][j]:
                    return False
                
        return True
        

    def operador(self, estado: Estado) -> list[Estado.Estado]:
        n = len(self.estado.dados)

        for i in range(0, n):
            for j in range(0, n):
                if self.estado.dados == 0:
                    vi, vj = i, j

        nestados = []

        # Não terminou ainda, trocar o 0 de lugar pra criar novos 
        # estados (nestados)
