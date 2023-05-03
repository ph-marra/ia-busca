from QuebraCabeca import QuebraCabeca
from EstadoQuebraCabeca import EstadoQuebraCabeca
from Labirinto import Labirinto
from EstadoLabirinto import EstadoLabirinto
from Busca import Busca

import sys

# Constante para limpar terminal (Linux ou Windows)
CLEAR = 'clear' if sys.platform.startswith('linux') else 'cls'

def main():

    einicial = EstadoQuebraCabeca([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
    emeta = EstadoQuebraCabeca([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
    problema = QuebraCabeca(einicial, emeta)

    print('Busca Profundidade')
    if Busca.bpl(problema, 5):
        print(problema.solucao)
    else:
        print("Não tem solução!")

    einicial = EstadoQuebraCabeca([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
    emeta = EstadoQuebraCabeca([[2, 8, 0], [1, 6, 3], [7, 5, 4]])
    problema = QuebraCabeca(einicial, emeta)

    print('Busca Profundidade Iterativa')
    if Busca.bli(problema, 4):
        print(problema.solucao)
    else:
        print("Não tem solução!")

    einicial = EstadoQuebraCabeca([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
    einicial = EstadoQuebraCabeca([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
    emeta = EstadoQuebraCabeca([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

    problema = QuebraCabeca(einicial, emeta)

    print('Busca Largura')
    if Busca.blarg(problema):
        print(problema.solucao)
    else:
        print("Não tem solução!")

    einicial_gina = EstadoLabirinto([
                    [2, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                    [0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 3, 1, 1, 1, 1, 0, 0],
                    ])
    
    print(einicial_gina)




if __name__ == "__main__":
    main()

