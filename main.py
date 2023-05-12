from time import process_time
from Problema import Problema
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

def print_solucao_busca_local(problema: Problema, encontrou: bool, busca: int):
    if encontrou == True:
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

def testes(tipo_problema: int, problemas, buscas, busca_escolhida: int, l: int, minimization = True):
    if busca_escolhida == 1:
        busca_nome = "Busca por Profundidade Limitada com L = " + str(l)
    elif busca_escolhida == 2:
        busca_nome = "Busca por Profundidade Iterativa"
    elif busca_escolhida == 3:
        busca_nome = "Busca Gulosa"
    elif busca_escolhida == 4:
        busca_nome = "Busca A*"
    elif busca_escolhida == 5:
        busca_nome = "Subida de Encosta"
    elif busca_escolhida == 6:
        busca_nome = "Subida de Encosta c/ Movimentos Laterais"
    else:
        busca_nome = "Recristalização Simulada"

    if tipo_problema == 1: 
        print("\nTESTES - QUEBRA CABEÇA")
    elif tipo_problema == 2:
        print("TESTES - LABIRINTO")
    print(f"BUSCA - {busca_nome}\n")
        
    for p in problemas:
        encontrou = False
        busca_nome = ""

        if tipo_problema == 1: 
            einicial = EstadoQuebraCabeca(p["Estado-Inicial"])
            emeta = EstadoQuebraCabeca(p["Estado-Meta"])
            problema = QuebraCabeca(einicial, emeta)
        elif tipo_problema == 2:
            einicial = EstadoLabirinto(p["Estado-Inicial"])
            emeta = EstadoLabirinto(p["Estado-Meta"])
            problema = Labirinto(einicial, emeta)

        start = process_time() 
   
        if busca_escolhida == 1 or busca_escolhida == 2:
            encontrou = buscas[busca_escolhida-1](problema, l)
        elif busca_escolhida == 3 or busca_escolhida == 4:
            encontrou = buscas[busca_escolhida-1](problema)
        else:
            encontrou = buscas[busca_escolhida-1](p, minimization=minimization)

        stop = process_time()

        print("-----------------------------------------------\n") 
        descricao = p["Descricao"]
        n = p["N"]
        print(f"PROBLEMA - {descricao} --- N = {n}")    
        print(f"TEMPO GASTO - {str(stop - start)}\n",) 

        if encontrou == True:
            print(f"Nós visitados = {problema.solucao.nvisitados}")
            print(f"Profundidade = {len(problema.solucao.cmeta) - 1}")
            print(f"Solução Encontrada\n")
            for e in problema.solucao.cmeta:
                print(e.dados) 
            print()
        else:
            print(f"Nós visitados = {problema.solucao.nvisitados}")
            print(f"Solução Não Encontrada\n")

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
        buscas = [Busca.bli, Busca.bpl, Busca.gulosa, Busca.astar, Busca.subida_encosta, Busca.subida_encosta_mov_lat, Busca.recristalizacao_simulada]
        busca = 0
        l = -1
        minimization = None

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
            if busca == 1:
                while l < 0:
                    os.system(CLEAR)
                    try:
                        l = int(input("Entre a altura máxima da Busca por Profundidade Limitada: "))
                    except:
                        pass
            elif busca == 2:
                while l < 0:
                    os.system(CLEAR)
                    try:
                        l = int(input("Entre a altura máxima da Busca por Profundidade Iterativa: "))
                    except:
                        pass 
            elif busca == 5 or busca == 6 or busca == 7:
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

            disp = -1
            while disp < 1 or disp > len(problemas) + 1:
                os.system(CLEAR)
                print("---------------------OPÇÕES------------------------")
                print("---------------------------------------------------\n")

                for i, problema in enumerate(problemas):
                    descricao = problema["Descricao"]
                    n = problema["N"]
                    print(f"{i+1}. {descricao} --- N = {n}")

                print(f"{i+2}. TESTES")

                print("\n---------------------------------------------------\n")

                try:
                    disp = int(input("Escolha uma opção: "))
                except:
                    pass

            if disp == len(problemas) + 1:
                testes(prob, problemas, buscas, busca, l, minimization)
                return

            if prob == 1: 
                einicial = EstadoQuebraCabeca(problemas[disp-1]["Estado-Inicial"])
                emeta = EstadoQuebraCabeca(problemas[disp-1]["Estado-Meta"])
                problema = QuebraCabeca(einicial, emeta)
            elif prob == 2:
                einicial = EstadoLabirinto(problemas[disp-1]["Estado-Inicial"])
                emeta = EstadoLabirinto(problemas[disp-1]["Estado-Meta"])
                problema = Labirinto(einicial, emeta)

            os.system(CLEAR)
            if busca == 1:
                os.system(CLEAR)
                if buscas[busca-1](problema, l):
                    print(f"Encontrada a seguinte solução para Busca por Profundidade Limitada com L = {l}\n")
                    print(problema.solucao)
                else:
                    print(f"Impossível achar solução para Busca por Profundidade Limitada com L = {l}")
                    print("Problema com a solução não encontrada:\n\n")
                    print(problema.solucao)
            elif busca == 2:
                os.system(CLEAR)
                if buscas[busca-1](problema, l):
                    print(f"Encontrada a seguinte solução para Busca por Profundidade Iterativa com L = {l}\n")
                    print(problema.solucao)
                else:
                    print(f"Impossível achar solução para Busca por Profundidade Iterativa com L = {l}")
                    print("Problema com a solução não encontrada:\n\n")
                    print(problema)
            elif busca == 5 or busca == 6 or busca == 7:
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






