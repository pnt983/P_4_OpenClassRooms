

class Match:
    """Crée un match entre deux joueurs"""
    def __init__(self, joueur_1, joueur_2):
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2

    def __repr__(self):
        match = f"{self.joueur_1} joue contre {self.joueur_2}"
        return match

    def serialiser_match(self):
        joueur_1_serialise = self.joueur_1.serialiser_joueur()
        joueur_2_serialise = self.joueur_2.serialiser_joueur()
        return(joueur_1_serialise, joueur_2_serialise)
