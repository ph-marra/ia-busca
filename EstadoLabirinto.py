from Estado import Estado

from Estado import Estado

class EstadoLabirinto(Estado):

    @staticmethod
    def h1(estado, meta) -> int:
        pass


    @staticmethod
    def h2(estado, meta) -> int:
        pass
    

    def __init__(self, dados: list[object], heuristica='h1') -> None:       
        super().__init__(dados)

        if heuristica == 'h2':
            self.__h__ = EstadoLabirinto.h2
        else:
            self.__h__ = EstadoLabirinto.h1
        

    def h(self, meta) -> int:
        return self.__h__(self, meta)
    
    def get_dados(self):
        return self.dados

    def __eq__(self, other):
        n = len(self.dados)

        for i in range(0, n):
            for j in range(0, n):
                if other.dados[i][j] != self.dados[i][j]:
                    return False
                
        return True
    
    def __str__(self):
        s = ''

        if self.g is not None:
            s += '-------------------------\ng = '
            s += str(self.g)

        if self.dados is not None:
            s += '\n\nLabirinto = \n\n'

            for i in range(0, len(self.dados)):
                for j in range(0, len(self.dados)):
                    s += str(self.dados[i][j])
                    s += ' '
                s += '\n'

            s += '-------------------------\n'

        return s