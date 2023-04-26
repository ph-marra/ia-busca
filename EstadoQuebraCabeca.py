import Estado

class EstadoQuebraCabeca(Estado):

    @staticmethod
    def h1(meta) -> int:
        pass

    @staticmethod
    def h2(meta) -> int:
        pass


    def __init__(self, dados: list[object], heuristica='h1') -> None:
        n = len(dados)
        if n != 3 or n != 4 or any(map(lambda l: len(l) != 3 or len(l) != 4, dados)):
            raise Exception
        
        super().__init__(dados)

        if heuristica == 'h2':
            self.__h__ = EstadoQuebraCabeca.h2
        else:
            self.__h__ = EstadoQuebraCabeca.h1
        


    def h(self, meta) -> int:
        return self.__h__(meta)
