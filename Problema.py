import Estado
import Solucao

class Problema:


    def __init__(self, einicial: Estado) -> None:
        self.einicial: Estado = einicial
        self.solucao: Solucao = None


    def teste_objetivo(self, estado: Estado) -> bool:
        pass


    def operador(self, estado: Estado) -> list[Estado.Estado]:
        pass
    

    


    
