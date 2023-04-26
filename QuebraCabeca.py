import Problema
import EstadoQuebraCabeca

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
        

    def operador(self, estado: EstadoQuebraCabeca) -> list[EstadoQuebraCabeca.EstadoQuebraCabeca]:
        n = len(self.estado.dados)

        for i in range(0, n):
            for j in range(0, n):
                if self.estado.dados == 0:
                    vi, vj = i, j

        nestados = []

        # Não terminou ainda, trocar o 0 de lugar pra criar novos 
        # estados (nestados)
