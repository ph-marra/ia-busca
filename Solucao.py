from Estado import Estado

class Solucao:


    def __init__(self, nvisitados: int, cmeta: list[Estado]) -> None:
        self.nvisitados = nvisitados
        self.cmeta = cmeta

    def __str__(self):
        print(self.nvisitados)

        print("\n-------------------------------\n")

        for e in self.cmeta:
            print(e.dados)


    
