from QuebraCabeca import QuebraCabeca
from EstadoQuebraCabeca import EstadoQuebraCabeca
from Labirinto import Labirinto
from EstadoLabirinto import EstadoLabirinto
from Busca import Busca

import os
import sys
import json

# Constante para limpar terminal (Linux ou Windows)
CLEAR = 'clear' if sys.platform.startswith('linux') else 'cls'

def main():

    prob = 0
    # Menu de problemas
    while prob > 3 or prob < 1:
        os.system(CLEAR)
        print("---------------------OPÇÕES------------------------")
        print("---------------------------------------------------\n")
        print("1. Quebra-cabeça de N^2-1 Peças Deslizantes.")
        print("2. Labirinto em uma Sala N x N.")
        print("3. Sair.")
        print("\n---------------------------------------------------\n")
        try:
            prob = int(input("Escolha uma opção: "))
        except:
            pass

    if prob == 3: return
    else:
        f = open('problemas.json', encoding='utf-8')

        if prob == 1:
            problemas = json.load(f)["Quebra-Cabecas"]
        elif prob == 2:
            problemas = json.load(f)["Labirintos"]


        disp = -1
        while disp < 1 or disp > len(problemas):
            os.system(CLEAR)
            print("---------------------OPÇÕES------------------------")
            print("---------------------------------------------------\n")

            for i, problema in enumerate(problemas):
                descricao = problema["Descricao"]
                print(f"{i+1}. {descricao}.")

            print("\n---------------------------------------------------\n")

            try:
                disp = int(input("Escolha uma opção: "))
            except:
                pass

        if prob == 1: 
            einicial = EstadoQuebraCabeca(problemas[disp-1]["Estado-Inicial"])
            emeta = EstadoQuebraCabeca(problemas[disp-1]["Estado-Meta"])
            problema = QuebraCabeca(einicial, emeta)
        elif prob == 2:
            einicial = EstadoLabirinto(problemas[disp-1]["Estado-Inicial"])
            emeta = EstadoLabirinto(problemas[disp-1]["Estado-Meta"])
            problema = Labirinto(einicial, emeta)

        busca = 0
        # Menu de tipos de busca
        while busca > 8 or busca < 1:
            os.system(CLEAR)
            print("---------------------OPÇÕES------------------------")
            print("---------------------------------------------------\n")
            print("1. Busca por Profundidade Limitada.")
            print("2. Busca por Profundidade Iterativa.")
            print("3. Busca Gulosa.")
            print("4. Busca A*.")
            print("5. Subida de Encosta.")
            print("6. Subida de Encosta c/ Movimentos Laterais.")
            print("7. Recristalização Simulada.")
            print("8. Sair.")
            print("\n---------------------------------------------------\n")
            try:
                busca = int(input("Escolha uma opção: "))
            except:
                pass

        if busca == 8: return
        else:
            os.system(CLEAR)
            buscas = [Busca.bli, Busca.bpl, Busca.gulosa, Busca.astar, Busca.subida_encosta, Busca.subida_encosta_mov_lat, Busca.recristalizacao_simulada]

            if busca == 1:
                l = -1
                while l < 0:
                    os.system(CLEAR)
                    try:
                        l = int(input("Entre a altura máxima da Busca por Profundidade Limitada: "))
                    except:
                        pass

                os.system(CLEAR)
                if buscas[busca-1](problema, l):
                    print(f"Encontrada a seguinte solução para Busca por Profundidade Limitada com L = {l}\n")
                    print(problema.solucao)
                else:
                    print(f"Impossível achar solução para Busca por Profundidade Limitada com L = {l}")
                    print("Problema com a solução não encontrada:\n\n")
                    print(problema)

            elif busca == 2:
                l = -1
                while l < 0:
                    os.system(CLEAR)
                    try:
                        l = int(input("Entre a altura máxima da Busca por Profundidade Iterativa: "))
                    except:
                        pass

                os.system(CLEAR)
                if buscas[busca-1](problema, l):
                    print(f"Encontrada a seguinte solução para Busca por Profundidade Iterativa com L = {l}\n")
                    print(problema.solucao)
                else:
                    print(f"Impossível achar solução para Busca por Profundidade Iterativa com L = {l}")
                    print("Problema com a solução não encontrada:\n\n")
                    print(problema)

            elif busca == 5 or busca == 6 or busca == 7:
                minimization = None
                while minimization != True and minimization != False:
                    os.system(CLEAR)
                    try:
                        inp = int(input("1. Minimização.\n2. Maximização.\nEscolha uma opção: "))
                        if inp == 1:
                            minimization = True
                        elif inp == 2:
                            minimization = False
                    except:
                        pass

                os.system(CLEAR)

                if buscas[busca-1](problema, minimization=minimization):
                    if busca == 5:
                        print(f"Encontrada solução para Busca Subida de Encosta\n")
                    elif busca == 6:
                        print(f"Encontrada solução para Busca Subida de Encosta com Movimentos Laterais\n")
                    else:
                        print(f"Encontrada solução para Recristalização Simulada\n")
                    print(problema.solucao)
                else:
                    if busca == 5:
                        print(f"Subida de Encosta finalizada por encontrar máximo local")
                        print("Caminho realizado até parada:\n\n")
                        print(problema.solucao)
                    else:
                        print("Problema com a solução não encontrada:\n\n")
                        print(problema)

            else:
                os.system(CLEAR)
                buscas[busca-1](problema)
                print(problema.solucao)


if __name__ == "__main__":
    main()

