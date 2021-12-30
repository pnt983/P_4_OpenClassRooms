from models.tournoi import Tournoi
from vues.vue_tournoi import VueTournoi
from .controller_joueurs import ControllerJoueur


class ControleurTournoi:

    def __init__(self):
        self.vue_tournoi = VueTournoi()

    def creer_tournoi(self):
        infos = self.vue_tournoi.creer_info_tournoi()
        self.tournoi = Tournoi(infos.get("nom"), infos.get("lieu"), infos.get("description"),
                               self.nb_tours(infos.get("nombre_tours")),
                               self.controle_temps(infos.get("controle_temps")))
        Tournoi.enregistrer_tournoi(Tournoi, self.tournoi)
        return self.tournoi

    def nb_tours(self, nombre_tours) -> str:   # Revoir pour la boucle infinie
        try:
            choix_utilisateur = nombre_tours
            if nombre_tours.strip() == '':
                return 4
            elif int(choix_utilisateur):
                return nombre_tours
            else:
                VueTournoi.message_erreur(VueTournoi)
                return 4
        except ValueError:
            VueTournoi.message_erreur(VueTournoi)
            return 4

    def controle_temps(self, choix_input):   # Revoir pour la boucle infinie
        choix = {1: "Bullet", 2: "Blitz", 3: "Coup rapide"}
        try:
            choix_utilisateur = choix_input
            if choix_utilisateur in choix:
                return choix[choix_utilisateur]
            else:
                VueTournoi.message_erreur(VueTournoi)
        except ValueError:
            VueTournoi.message_erreur(VueTournoi)

    def ajouter_joueur_au_tournoi(self, nom, lieu, nombre_joueur: int = 8):
        choix_nombre_joueurs = VueTournoi.choisir_nombre_joueur(VueTournoi)
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
