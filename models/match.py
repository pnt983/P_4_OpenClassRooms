

from models.joueur import Joueur


class JoueurScore:

    def __init__(self, joueur: Joueur, score=0) -> None:
        self.joueur = joueur
        self._score = score

    def __repr__(self) -> str:
        return f"{self.joueur.nom}, {self.joueur.prenom}"

    def serialiser_joueur_score(self):
        joueur_serialise = self.joueur.serialiser_joueur()
        return joueur_serialise

    @property
    def ajouter_score(self):
        return self._score

    @ajouter_score.setter
    def ajouter_score(self, value):
        self._score = value
        self.joueur.score += value


class Match:
    """Crée un match entre deux joueurs"""
    def __init__(self, joueur_score_1: JoueurScore, joueur_score_2: JoueurScore):
        self.joueur_score_1 = joueur_score_1
        self.joueur_score_2 = joueur_score_2

    def __repr__(self):
        match = f"{self.joueur_score_1} joue contre {self.joueur_score_2}"
        return match

    def obtenir_resultat(self):
        return f"{self.joueur_score_1} : {self.joueur_score_1._score} VS {self.joueur_score_2} : \
{self.joueur_score_2._score}"

    def serialiser_match(self):
        joueur_1_serialise = self.joueur_score_1.joueur.id, self.joueur_score_1._score
        joueur_2_serialise = self.joueur_score_2.joueur.id, self.joueur_score_2._score
        serialise = {"Matchs": [joueur_1_serialise, joueur_2_serialise]}
        return serialise

    @classmethod
    def deserialiser_match(cls, info_match, table_joueur):
        liste_joueurs = []
        for row in info_match["Matchs"]:
            id_joueur = row[0]
            joueur = table_joueur.get(doc_id=id_joueur)
            objet_joueur = Joueur.deserialiser_joueur(joueur)
            liste_joueurs.append(objet_joueur)
        match = Match(JoueurScore(liste_joueurs[0]), JoueurScore(liste_joueurs[1]))
        return match

    def ajouter_joueur_deja_rencontre(self):
        joueur_1 = self.joueur_score_1.joueur
        joueur_2 = self.joueur_score_2.joueur
        joueur_1.adversaire_deja_rencontrer.append(joueur_2)
        joueur_2.adversaire_deja_rencontrer.append(joueur_1)
        print(id(joueur_1))
        print(id(joueur_2))
