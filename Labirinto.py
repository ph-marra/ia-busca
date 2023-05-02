from Problema import Problema
from EstadoLabirinto import EstadoLabirinto

class Labirinto(Problema):


    def __init__(self, einicial: EstadoLabirinto, emeta: EstadoLabirinto) -> None:       
        super().__init__(einicial, emeta)


    def teste_objetivo(self, estado: EstadoLabirinto) -> bool:
        n = len(estado.dados)
        for i in range(0, n):
            for j in range(0, n):
                if estado.dados[i][j] != self.emeta.dados[i][j]:
                    return False
                
        return True
        

    def operador(self, estado: EstadoLabirinto) -> list[EstadoLabirinto]:
        pass
