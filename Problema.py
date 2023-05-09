from Estado import Estado
from Solucao import Solucao

class Problema:


    def __init__(self, einicial: Estado, einfos: object, emeta: Estado) -> None:
        self.einicial: Estado = einicial
        self.emeta: Estado = emeta
        self.einfos = einfos
        self.solucao: Solucao = None


    def teste_objetivo(self, estado: Estado) -> bool:
        pass


    def operador(self, estado: Estado) -> list[Estado]:
        pass
    
    def relacao(self, estado1: Estado, estado2: Estado) -> int:
        pass
    

    


    
