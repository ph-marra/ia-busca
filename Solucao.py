from Estado import Estado

class Solucao:


    def __init__(self, nvisitados: int, cmeta: list[Estado], profmeta: int, emeta: Estado) -> None:
        self.nvisitados = nvisitados
        self.cmeta = cmeta
        self.profmeta = profmeta
        self.emeta = emeta

    def __str__(self):
        s = ''
        
        s += 'Visitados = '
        s += str(self.nvisitados)

        s += '\nProfundidade = '
        s += str(self.profmeta)

        if self.cmeta is not None:
            for i, e in enumerate(self.cmeta):
                s += '\n\n----------------------------\n\n'

                s += f"{i+1}-ésimo estado (com H = {str(e.h(self.emeta))})\n\n"
                s += e.__str__()

        return s


    
