from vues.vue_round import VueRound
from models.round import Round
import time


class ControllerRound:

    def __init__(self):
        pass

    def creer_premier_round(self):  # A faire
        date = time.strftime("%A %d %B %Y")
        heure = time.strftime("%X")
        nom_du_tour = VueRound.nom(VueRound)
        matchs = Round.premieres_paires(Round)  # Mettre les arguments
        print(f"Le {nom_du_tour} commence le {date}, a {heure}.")
        return matchs

    def creer_les_rounds_suivant(self):  # A faire
        date = time.strftime("%A %d %B %Y")
        heure = time.strftime("%X")
        nom_du_tour = VueRound.nom(VueRound)
        matchs = Round.generer_paires(Round)
        print(f"Le {nom_du_tour} commence le {date}, a {heure}.")
        return matchs

    def fin_round(self):   # A faire
        date = time.strftime("%A %d %B %Y")
        heure = time.strftime("%X")
        Round.entrer_resultat_matchs(Round,)  # Mettre les arguments
        print(f"{date}{heure}")
