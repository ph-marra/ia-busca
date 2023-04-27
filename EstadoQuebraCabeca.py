from Estado import Estado

class EstadoQuebraCabeca(Estado):

    @staticmethod
    def h1(meta) -> int:
        pass

    @staticmethod
    def h2(meta) -> int:
        pass


    def __init__(self, dados: list[object], heuristica='h1') -> None:
        #n = len(dados)
        #if n != 3 or n != 4 or any(map(lambda l: len(l) != 3 or len(l) != 4, dados)):
        #    raise Exception
        
        super().__init__(dados)

        if heuristica == 'h2':
            self.__h__ = EstadoQuebraCabeca.h2
        else:
            self.__h__ = EstadoQuebraCabeca.h1
        

    def h(self, meta) -> int:
        return self.__h__(meta)
    
    def get_dados(self):
        return self.dados

    def __eq__(self, other):
        n = len(self.dados)

        for i in range(0, n):
            for j in range(0, n):
                if other[i][j] != self.dados[i][j]:
                    return False
                
        return True
    
    def __str__(self):
        s = ''

        if self.g is not None:
            s += '-------------------------\ng = '
            s += str(self.g)

        if self.dados is not None:
            s += '\n\nmatriz = '
            s += str(self.dados)
            s += '\n-------------------------\n'

        return s