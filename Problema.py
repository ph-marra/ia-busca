import Estado

class Problema:

    def __init__(self, einicial: Estado, eatual: Estado, evisitados: list[Estado.Estado]):
        self.einicial = einicial
        self.eatual = eatual
        self.evisitados = evisitados

    def teste_objetivo(estado: Estado) -> bool:
        pass

    def operador(estado: Estado) -> list[Estado.Estado]:
        pass

    def g(n: Estado) -> int:
        return n.custo

    def h(n: Estado) -> int:
        return n.estimado

    def f(estado: Estado) -> int:
        pass

    
