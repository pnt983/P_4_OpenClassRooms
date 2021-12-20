import vue_joueurs
import joueur
from tinydb import TinyDB, Query

db = TinyDB("db.json")
user = Query()
table_joueur = db.table("Joueur")
table_tournoi = db.table("Tournoi")
table_joueur_par_tournoi = db.table("Joueur_du_tournoi")
table_rounds_par_tournoi = db.table("Rounds")


class ControllerJoueur:

    def __init__(self):
        self.vue_joueur = vue_joueurs.VueJoueur()

    def creer_joueur(self):
        infos = self.vue_joueur.creer_infos_joueur()
        self.joueur = joueur.Joueur(infos.get("nom"), infos.get("prenom"), infos.get("date_naissance"),
                                    joueur.Joueur.sexe(joueur.Joueur, infos.get("sexe")),
                                    joueur.Joueur.classement(joueur.Joueur, infos.get("classement")))
        serialise = {
            "nom": self.joueur.nom,
            "prenom": self.joueur.prenom,
            "naissance": self.joueur.date_de_naissance,
            "sexe": self.joueur.sexe_joueur,
            "classement": self.joueur.classement_joueur
        }
        table_joueur.upsert(serialise,
                            user.nom == self.joueur.nom and user.prenom == self.joueur.prenom)
        return serialise

    def entrer_joueur(self, nom_tournoi, lieu_tournoi):
        """ Enregistre un nouveau joueur ou recupere dans la base de donnees"""
        while True:
            choix = {1: "Creer nouveau joueur", 2: "Choisir joueur dans la base de donnee"}
            try:
                choix_utilisateur = int(input("Entrer 1 pour creer un joueur ou 2 pour \
choisir dans la base de donnees: "))
                if choix_utilisateur in choix:
                    if choix_utilisateur == 1:
                        creer_joueur = self.creer_joueur()
                        joueur.Joueur.ajouter_joueur_du_tournoi_a_db(joueur.Joueur, nom_tournoi, lieu_tournoi, creer_joueur)
                        return creer_joueur
                    elif choix_utilisateur == 2:
                        choix = vue_joueurs.VueJoueur.choix_par_id(vue_joueurs.VueJoueur)
                        joueur_recuperer = joueur.Joueur.recuperer_joueur_db(joueur.Joueur, choix)
                        joueur.Joueur.ajouter_joueur_du_tournoi_a_db(joueur.Joueur, nom_tournoi, lieu_tournoi, joueur_recuperer)
                        return joueur_recuperer
                    else:
                        print("Votre choix ne fait pas partie des options possibles.")
                else:
                    print("Le choix est incorrecte")
            except ValueError:
                print("Le choix n'est pas valide, veuillez reesayer")


def main():
    test = ControllerJoueur()
    resultat = test.entrer_joueur("test", "test2")
    print(resultat)
    print(type(resultat))


if __name__ == "__main__":
    main()
