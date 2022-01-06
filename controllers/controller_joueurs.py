from vues.vue_joueurs import VueJoueur
from models.joueur import Joueur
from . import controller_app


class ControllerJoueur:

    def __init__(self):
        self.db = controller_app.ControllerApp().table_joueur
        self.query = controller_app.ControllerApp().user

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

    def modifier_classement_joueur(self) -> str:    # A revoir
        """L'utilisateur peut modifier le classement d'un joueur par son ID"""
        while True:
            try:
                joueur_a_modifier = VueJoueur.modifier_classement(VueJoueur)
                joueur_trouve = self.db.get(doc_id=joueur_a_modifier)
                if joueur_trouve is not None:
                    nouveau_classement = VueJoueur.nouveau_classement(VueJoueur)
                    self.db.update({"classement": nouveau_classement}, doc_ids=[joueur_a_modifier])
                    return joueur_trouve
                else:
                    VueJoueur.message_erreur(VueJoueur)
            except ValueError:
                VueJoueur.message_erreur(VueJoueur)


def main():
    test = ControllerJoueur()
    resultat = test.modifier_classement_joueur()
    print(resultat)
    print(type(resultat))


if __name__ == "__main__":
    main()
