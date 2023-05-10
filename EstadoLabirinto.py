from Estado import Estado

from Estado import Estado

class EstadoLabirinto(Estado):

    @staticmethod
    def h1(estado, meta) -> int:
        
        x, y = len(estado.dados), len(estado.dados[0])
        ip, jp = 0, 0
        im, jm = 0, 0

        for i in range(0, x):
            for j in range(0, y):
                if estado.dados[i][j] == 10 or estado.dados[i][j] == 20:
                    ip, jp = i, j
                if meta.dados[i][j] == 30:
                    im, jm = i, j

        return abs(im - ip)**2 + abs(jm - jp)**2


    @staticmethod
    def h2(estado, meta) -> int:

        x, y = len(estado.dados), len(estado.dados[0])
        ip, jp = 0, 0
        im, jm = 0, 0

        for i in range(0, x):
            for j in range(0, y):
                if estado.dados[i][j] == 10 or estado.dados[i][j] == 20:
                    ip, jp = i, j
                if meta.dados[i][j] == 30:
                    im, jm = i, j

        return abs(im - ip) + abs(jm - jp)


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

            x, y = len(self.dados), len(self.dados[0])
            for i in range(0, x):
                for j in range(0, y):
                    if self.dados[i][j] >= 10:
                        s += 'P'
                    else:
                        s += str(self.dados[i][j])
                    s += ' '
                s += '\n'

            s += '-------------------------\n'

        return s