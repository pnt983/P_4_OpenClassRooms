from vues import vue_joueurs
from models.joueur import Joueur
from tinydb import TinyDB, Query

db = TinyDB("db.json")
user = Query()
table_joueur = db.table("Joueur")
table_tournoi = db.table("Tournoi")
table_joueur_par_tournoi = db.table("Joueur_du_tournoi")
table_rounds_par_tournoi = db.table("Rounds")


class ControllerJoueur:

    def __init__(self):
        pass

    def creer_joueur(self):
        """ Cree un joueur et l'ajoute a la db 'table_joueur' """
        infos = vue_joueurs.VueJoueur.creer_infos_joueur(vue_joueurs.VueJoueur)
        self.joueur = Joueur(infos.get("nom"), infos.get("prenom"), infos.get("date_naissance"),
                                    Joueur.sexe(Joueur, infos.get("sexe")),
                                    Joueur.classement(Joueur, infos.get("classement")))
        serialise = self.joueur.serialise_joueur(self.joueur)
        table_joueur.upsert(serialise,
                            user.nom == self.joueur.nom and user.prenom == self.joueur.prenom)
        return serialise

    def ajouter_joueur_au_tournoi(self, nom_tournoi, lieu_tournoi):
        """ Enregistre un nouveau joueur ou recupere dans la base de donnees pour l'ajouter au tournoi"""
        while True:
            choix = {1: "Creer nouveau joueur", 2: "Choisir joueur dans la base de donnee"}
            try:
                choix_utilisateur = vue_joueurs.VueJoueur.choix_ajouter_joueur(vue_joueurs.VueJoueur)
                if choix_utilisateur in choix:
                    if choix_utilisateur == 1:
                        creer_joueur = self.creer_joueur(ControllerJoueur)
                        Joueur.ajouter_joueur_du_tournoi_a_db(Joueur, nom_tournoi,
                                                                     lieu_tournoi, creer_joueur)
                        return creer_joueur
                    elif choix_utilisateur == 2:
                        choix = vue_joueurs.VueJoueur.choix_par_id(vue_joueurs.VueJoueur)
                        joueur_recuperer = Joueur.recuperer_joueur_db(Joueur, choix)
                        Joueur.ajouter_joueur_du_tournoi_a_db(Joueur, nom_tournoi,
                                                                     lieu_tournoi, joueur_recuperer)
                        return joueur_recuperer
                    else:
                        print("Votre choix ne fait pas partie des options possibles.")
                else:
                    print("Le choix est incorrecte")
            except ValueError:
                print("Le choix n'est pas valide, veuillez reesayer")


def main():
    test = ControllerJoueur()
    resultat = test.creer_joueur()
    print(resultat)
    print(type(resultat))


if __name__ == "__main__":
    main()
