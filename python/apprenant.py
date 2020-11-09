class Apprenant:
    def __init__(self, *infos):
        self.id = infos[0]
        self.prenom = infos[1].lower().replace('éèêë', 'e')
        self.nom = infos[2].lower().replace("'", '').replace(' ', '-')
        self.mail = None
