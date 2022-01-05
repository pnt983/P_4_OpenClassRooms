from models.tournoi import Tournoi
from vues.vue_tournoi import VueTournoi
from .controller_joueurs import ControllerJoueur


class ControleurTournoi:

    def __init__(self):
        self.vue_tournoi = VueTournoi()

    def creer_tournoi(self):
        self.tournoi = Tournoi(VueTournoi.creer_nom_tournoi(VueTournoi),
                               VueTournoi.creer_lieu_tournoi(VueTournoi),
                               VueTournoi.creer_description_tournoi(VueTournoi),
                               VueTournoi.nombre_tours_tournoi(VueTournoi),
                               VueTournoi.controle_temps(VueTournoi))
        Tournoi.enregistrer_tournoi(Tournoi, self.tournoi)
        return self.tournoi

    def ajouter_joueur_au_tournoi(self, nom, lieu, nombre_joueur: int = 8):
        choix_nombre_joueurs = VueTournoi.choisir_nombre_joueurs(VueTournoi)
        liste_joueurs = []
        if not choix_nombre_joueurs:
            i = 0
            for i in range(nombre_joueur):
                nouveau_joueur = ControllerJoueur.ajouter_joueur_au_tournoi(ControllerJoueur, nom, lieu)
                liste_joueurs.append(nouveau_joueur)
                i += 1
        else:
            i = 0
            for i in range(int(choix_nombre_joueurs)):
                nouveau_joueur = ControllerJoueur.ajouter_joueur_au_tournoi(ControllerJoueur, nom, lieu)
                liste_joueurs.append(nouveau_joueur)
                i += 1
        return liste_joueurs


def main():
    test = ControleurTournoi()
    result = test.creer_tournoi()
    print(type(result))


if __name__ == "__main__":
    main()
