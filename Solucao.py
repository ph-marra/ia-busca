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
        
        for i, e in enumerate(self.cmeta):
            s += '\n-------------------------------\n\n'

            s += f"{i+1}-ésimo estado (com H = {str(e.h(self.emeta))})\n\n"
            s += e.__str__()
            s += '\n'

            s += '\n-------------------------------\n'

        return s


    
