
class Read:
    def __init__(self, fichier):
        self.fichier = fichier

    def read(self):
        f = open(self.fichier, "r")
        return f.readlines()
