from vues.vue_round import VueRound
from models.round import Round


class ControllerRound:

    def __init__(self):
        self.round = None

    def creer_premier_round(self, liste_joueurs):
        self.round = Round(VueRound.creer_nom_round())
        joueurs = self.round.classer_par_classement(liste_joueurs)
        self.round.creer_premieres_paires(joueurs)
        self.round.liste_des_matchs.extend([self.round.nom, self.round.matchs])
        VueRound.afficher_les_matchs(self.round.matchs)
        VueRound.afficher_debut_round(self.round.nom, self.round.date)
        return self.round

    def creer_les_rounds_suivant(self, liste_joueurs):
        self.round = Round(VueRound.creer_nom_round())
        joueurs = self.round.classer_par_score(liste_joueurs)
        self.round.generer_paires(joueurs)
        self.round.liste_des_matchs.extend([self.round.nom, self.round.matchs])
        VueRound.afficher_les_matchs(self.round.matchs)
        VueRound.afficher_debut_round(self.round.nom, self.round.date)
        return self.round

    def entrer_resultat_matchs(self, liste_matchs):
        """Permet au gestionnaire de rentrer les resultats"""
        for match in liste_matchs:
            VueRound.montrer_message(match)
            choix_gagnant = VueRound.entrer_resultat()
            if choix_gagnant == 1:
                match.joueur_score_1._score += 1
                match.joueur_score_1.joueur.score += 1
            elif choix_gagnant == 2:
                match.joueur_score_2._score += 1
                match.joueur_score_2.joueur.score += 1
            elif choix_gagnant == 3:
                match.joueur_score_1._score += 0.5
                match.joueur_score_1.joueur.score += 0.5
                match.joueur_score_2._score += 0.5
                match.joueur_score_2.joueur.score += 0.5

    def creer_rounds_reprise(self, round: Round, liste_joueurs):
        self.round = round
        joueurs = self.round.classer_par_score(liste_joueurs)
        self.round.generer_paires(joueurs)
        VueRound.afficher_les_matchs(self.round.matchs)
        return self.round
