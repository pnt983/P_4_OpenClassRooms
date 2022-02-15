from vues.vue_round import VueRound
from models.round import Round


class ControllerRound:

    def __init__(self):
        self.round = None

    def creer_premier_round(self, liste_joueurs):
        self.round = Round()
        joueurs = self.round.classer_par_classement(liste_joueurs)
        matchs = self.round.premieres_paires(joueurs)
        self.round.match.extend([self.round.nom, matchs])
        self.round.liste_des_matchs.extend([self.round.nom, matchs])
        VueRound.montrer_message(VueRound, matchs)
        VueRound.afficher_debut_round(VueRound, self.round.nom, self.round.date)
        return matchs, self.round

    def creer_les_rounds_suivant(self, liste_joueurs):
        self.round = Round()
        joueurs = self.round.classer_par_score(liste_joueurs)
        matchs = self.round.generer_paires(joueurs)
        self.round.match.extend([self.round.nom, matchs])
        self.round.liste_des_matchs.extend([self.round.nom, matchs])
        VueRound.montrer_message(VueRound, matchs)
        VueRound.afficher_debut_round(VueRound, self.round.nom, self.round.date)
        return matchs, self.round

    def entrer_resultat_matchs(self, liste_matchs):
        """Permet au gestionnaire de rentrer les resultats"""
        for matchs in liste_matchs:
            VueRound.montrer_message(VueRound, matchs)
            choix_gagnant = VueRound.qui_gagne(VueRound)
            if choix_gagnant == 1:
                joueur_1 = matchs[0]
                joueur_1.score += 1
            elif choix_gagnant == 2:
                joueur_2 = matchs[1]
                joueur_2.score += 1
            elif choix_gagnant == 3:
                joueur_1 = matchs[0]
                joueur_1.score += 0.5
                joueur_2 = matchs[1]
                joueur_2.score += 0.5
