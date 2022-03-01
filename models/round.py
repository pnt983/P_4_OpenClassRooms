import datetime
from itertools import islice
from operator import itemgetter
from .joueur import Joueur


class Round:
    """ Creation des tours pour le tournoi"""

    liste_des_matchs = []

    def __init__(self, nom, date_debut_round=None, date_fin_round="En_cours", etat_round="En_cours", matchs_round=[]):
        self.date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.date_fin = date_fin_round
        self.avancer_round = "En_cours"
        self.etat_round = etat_round
        self.nom = nom
        self.match = matchs_round

    def premieres_paires(self, liste_joueurs):
        " Classe les joueurs par meilleur classement et divise la liste en deux pour les associer"
        self.liste_des_matchs.clear()
        liste_a_classer = liste_joueurs
        liste_matchs = []
        separation_liste = len(liste_a_classer) / 2
        for premier, deuxieme in zip(liste_a_classer, islice(liste_a_classer, int(separation_liste), None)):
            matchs = (premier, deuxieme)
            liste_matchs.append(matchs)
        return liste_matchs

    def generer_paires(self, liste_joueurs):   # Revoir pour si un match est en double
        """Cree des matchs par rapport au score des joueurs"""
        liste_matchs = []
        for premier, deuxieme in zip(islice(liste_joueurs, 0, None, 2), islice(liste_joueurs, 1, None, 2)):
            matchs = (premier, deuxieme)
            liste_matchs.append(matchs)
        return liste_matchs

    def serialiser_round(self):
        liste_matchs_serialise = []
        for row in self.match:
            print(type(row), "row = ", row)
            for i in row:
                print(type(i), "i = ", i)
            #     joueur_serialise = i.serialiser_joueur()
            #     liste_matchs_serialise.append(joueur_serialise)
                joueur_serialise = [joueur.serialiser_joueur() for joueur in i]
                liste_matchs_serialise.append(joueur_serialise)
        # print(type(row), "Je suis dans serialise joueur", row)
                # for joueur in i:
                #     joueur_serialise = joueur.serialiser_joueur()
                #     liste_matchs_serialise.append(joueur_serialise)
                    # print(type(joueur), joueur)
        # joueur_serialise = [joueur.serialiser_joueur() for joueur in self.match]
        # liste_matchs_serialise.append(joueur_serialise)
        serialise = {
            "nom_round": self.nom,
            "date_debut_round": self.date,
            "date_fin_round": self.date_fin,
            "etat_round": self.etat_round,
            "matchs_round": liste_matchs_serialise
        }
        return serialise

    def test_serialiser_round(self):   # A revoir
        liste_matchs_serialise = []
        print(type(self.match[-1]), "match[-1] = ", self.match[-1])
        for joueur in self.match[-1]:
            print(type(joueur), "joueur = ", joueur)
        #     for row in joueur:
        #         print(type(row), "row = ", row)
            # joueur_serialise = [row.serialiser_joueur() for row in joueur]
            # liste_matchs_serialise.append(joueur_serialise)
        # for row in self.match:
        #     print(type(row), "row = ", row)
        #     for i in row:
        #         print(type(i), "i = ", i)
            #     joueur_serialise = i.serialiser_joueur()
            #     liste_matchs_serialise.append(joueur_serialise)
                # joueur_serialise = [joueur.serialiser_joueur() for joueur in i]
                # liste_matchs_serialise.append(joueur_serialise)
        # print(type(row), "Je suis dans serialise joueur", row)
                # for joueur in i:
                #     joueur_serialise = joueur.serialiser_joueur()
                #     liste_matchs_serialise.append(joueur_serialise)
                    # print(type(joueur), joueur)
        # joueur_serialise = [joueur.serialiser_joueur() for joueur in self.match]
        # liste_matchs_serialise.append(joueur_serialise)
        serialise = {
            "nom_round": self.nom,
            "date_debut_round": self.date,
            "date_fin_round": self.date_fin,
            "etat_round": self.etat_round,
            "matchs_round": liste_matchs_serialise
        }
        return serialise

    @classmethod
    def deserialiser_round(cls, infos_round):
        nom = infos_round["nom_round"]
        date_debut_round = infos_round["date_debut_round"]
        date_fin_round = infos_round["date_fin_round"]
        etat_round = infos_round["etat_round"]
        matchs_round = infos_round["matchs_round"]
        objet_round = Round(nom, date_debut_round, date_fin_round, etat_round, matchs_round)
        return objet_round

    def ajouter_date_fin_round(self):
        self.date_fin = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        return self.date_fin

    def cloturer_round(self):
        self.etat_round = "Round completement fini"
        return self.etat_round

    def classer_par_ordre_alphabetique(self, liste_joueurs):
        liste_par_alphabet = sorted(liste_joueurs, key=itemgetter(0), reverse=True)
        return liste_par_alphabet

    def classer_par_classement(self, liste_joueurs):
        for row in liste_joueurs:
            liste_par_classement = sorted(row, key=lambda joueur: joueur.classement_joueur, reverse=True)
            return liste_par_classement

    def classer_par_score(self, liste_joueurs):
        for row in liste_joueurs:
            liste_par_score = sorted(row, key=lambda joueur: joueur.score, reverse=True)
            return liste_par_score


def main():
    pass


if __name__ == "__main__":
    main()
