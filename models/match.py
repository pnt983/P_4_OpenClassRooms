

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

    @classmethod
    def deserialiser_joueur_score(cls, match, liste_joueurs):
        test = match[0]
        for row in liste_joueurs:
            if test == row.id:
                joueur_score = JoueurScore(row, match[1])
                return joueur_score

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
    def deserialiser_match(cls, info_match, liste_joueurs):
        liste_joueurs_score = []
        liste_deserialiser_joueurs_score = []
        for match in info_match["Matchs"]:
            joueur_score = JoueurScore.deserialiser_joueur_score(match, liste_joueurs)
            liste_joueurs_score.append(joueur_score)
        for joueur in liste_joueurs_score:
            liste_deserialiser_joueurs_score.append(joueur)
        while len(liste_deserialiser_joueurs_score) > 0:
            joueur_1 = liste_deserialiser_joueurs_score[0]
            joueur_2 = liste_deserialiser_joueurs_score[1]
            objet_match = Match(joueur_1, joueur_2)
            liste_deserialiser_joueurs_score.remove(joueur_1)
            liste_deserialiser_joueurs_score.remove(joueur_2)
            return objet_match

    def ajouter_joueur_deja_rencontre(self):
        joueur_1 = self.joueur_score_1.joueur
        joueur_2 = self.joueur_score_2.joueur
        joueur_1.adversaire_deja_rencontrer.append(joueur_2)
        joueur_2.adversaire_deja_rencontrer.append(joueur_1)
        print(id(joueur_1))
        print(id(joueur_2))
