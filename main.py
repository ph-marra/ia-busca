from QuebraCabeca import QuebraCabeca
from EstadoQuebraCabeca import EstadoQuebraCabeca
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
    einicial = EstadoQuebraCabeca([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
    emeta = EstadoQuebraCabeca([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

    problema = QuebraCabeca(einicial, emeta)

    print('Busca Largura')
    if Busca.bli(problema):
        print(problema.solucao)
    else:
        print("Não tem solução!")



if __name__ == "__main__":
    main()

