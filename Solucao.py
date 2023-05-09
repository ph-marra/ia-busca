from Estado import Estado

class Solucao:


    def __init__(self, nvisitados: int, cmeta: list[Estado], emeta: Estado) -> None:
        self.nvisitados = nvisitados
        self.cmeta = cmeta
        self.emeta = emeta

    def __str__(self):
        s = ''
        
        s += 'Visitados = '
        s += str(self.nvisitados)

        s += "\n-------------------------------\n"
        
        for e in self.cmeta:
            s += '\n******\n'
            s += str(e.dados) + ' h = ' + str(e.h(self.emeta))
            s += '\n******\n'

        return s


    
