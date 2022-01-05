from vues.vue_joueurs import VueJoueur
from models.joueur import Joueur


class ControllerJoueur:

    def __init__(self):
        pass

    def creer_joueur(self):
        """ Cree un joueur et l'ajoute a la db 'table_joueur' """
        self.joueur = Joueur(VueJoueur.creer_nom_joueur(VueJoueur),
                             VueJoueur.creer_prenom_joueur(VueJoueur),
                             VueJoueur.creer_date_naissance_joueur(VueJoueur),
                             VueJoueur.creer_sexe_joueur(VueJoueur),
                             VueJoueur.creer_classement_joueur(VueJoueur))
        serialise = self.joueur.serialise_joueur(self.joueur)
        Joueur.enregistrer_joueur_dans_db(Joueur, serialise, self.joueur.nom, self.joueur.prenom)
        return serialise


def main():
    test = ControllerJoueur()
    resultat = test.creer_joueur()
    print(resultat)
    print(type(resultat))


if __name__ == "__main__":
    main()
