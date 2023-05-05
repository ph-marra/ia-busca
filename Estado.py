
class Estado:
    

    def __init__(self, dados: list[object]) -> None:
        self.dados: list[object] = dados
        self.g: int = 0
   

    def h(self, meta) -> int:
        pass

    def gera_aleatorio(self) -> None:
        pass

    def sucessor_hill_climbing(self, problema, minimization = True) -> None:
        vizinhos = problema.operador(self)
        hatual = self.h(problema.emeta)
        hsuc = self.h(problema.emeta)
        suc = None

        for e in vizinhos:
            if minimization == True:
                if e.h(problema.emeta) < hatual and e.h(problema.emeta) < hsuc:
                    suc = e
                    hsuc = e.h(problema.emeta)
            else:
                if e.h(problema.emeta) > hatual and e.h(problema.emeta) > hsuc:
                    suc = e
                    hsuc = e.h(problema.emeta)

        return suc
    

    
        