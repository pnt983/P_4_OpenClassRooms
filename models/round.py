import datetime
from itertools import islice
from operator import itemgetter


class Round:
    """ Creation des tours pour le tournoi"""

    liste_des_matchs = []

    def __init__(self, nom, date_debut_round=None, date_fin_round="En_cours", etat_round="En_cours", matchs_round=[]):
        self.date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.date_fin = date_fin_round
        self.etat_round = etat_round
        self.nom = nom
        self.match = matchs_round

    def premieres_paires(self, liste_joueurs):
        """ Classe les joueurs par meilleur classement et divise la liste en deux pour les associer"""
        self.liste_des_matchs.clear()
        liste_a_classer = liste_joueurs
        liste_matchs = []
        separation_liste = len(liste_a_classer) / 2
        for premier, deuxieme in zip(liste_a_classer, islice(liste_a_classer, int(separation_liste), None)):
            matchs = (premier, deuxieme)
            liste_matchs.append(matchs)
            premier.deja_jouer.append(deuxieme)
            deuxieme.deja_jouer.append(premier)
        return liste_matchs

    def generer_paires(self, liste_joueurs):   # Revoir pour si un match est en double
        """ Cree des matchs par rapport au score des joueurs. Retourne la liste des matchs"""
        liste_matchs = []
        liste_premiere = []
        liste_deuxieme = []
        for p, d in zip(islice(liste_joueurs, 0, None, 2), islice(liste_joueurs, 1, None, 2)):
            liste_premiere.append(p)
            liste_deuxieme.append(d)
        for i in range(len(liste_premiere)):
            for premier, deuxieme in zip(liste_premiere, liste_deuxieme):
                if deuxieme in premier.deja_jouer:
                    if len(liste_deuxieme) == 1:
                        matchs = (liste_premiere[0], liste_deuxieme[0])
                        liste_matchs.append(matchs)
                        premier.deja_jouer.append(liste_deuxieme[0])
                        deuxieme.deja_jouer.append(liste_premiere[0])
                        liste_premiere.pop(0)
                        liste_deuxieme.pop(0)
                        i += 1
                    else:
                        match = (liste_premiere[0], liste_deuxieme[1])
                        liste_matchs.append(match)
                        premier.deja_jouer.append(liste_deuxieme[1])
                        deuxieme.deja_jouer.append(liste_premiere[0])
                        liste_premiere.pop(0)
                        liste_deuxieme.pop(1)
                        i += 1
                else:
                    matchs = (liste_premiere[0], liste_deuxieme[0])
                    liste_matchs.append(matchs)
                    premier.deja_jouer.append(liste_deuxieme[0])
                    deuxieme.deja_jouer.append(liste_premiere[0])
                    liste_premiere.pop(0)
                    liste_deuxieme.pop(0)
                    i += 1
        return liste_matchs

    def serialiser_round(self):
        liste_matchs_serialise = []
        for row in self.match:
            for i in row:
                joueur_serialise = [joueur.serialiser_joueur() for joueur in i]
                liste_matchs_serialise.append(joueur_serialise)
        serialise = {
            "nom_round": self.nom,
            "date_debut_round": self.date,
            "date_fin_round": self.date_fin,
            "etat_round": self.etat_round,
            "matchs_round": liste_matchs_serialise
        }
        return serialise

    def serialiser_round_apres_reprise(self):
        liste_matchs_serialise = []
        for row in self.match[-1]:
            joueur_serialise = [joueur.serialiser_joueur() for joueur in row]
            liste_matchs_serialise.append(joueur_serialise)
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
