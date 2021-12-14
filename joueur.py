import tournoi
import vue_joueurs
from operator import itemgetter


class Joueur:
    """Enregistrer les nouveaux joueurs ou charger ceux enregistrés dans la base de donnees"""

    def __init__(self):
        self.nom = vue_joueurs.nom()
        self.prenom = vue_joueurs.prenom()
        self.date_de_naissance = vue_joueurs.date_de_naissance()
        self.sexe = vue_joueurs.sexe()
        self.classement = vue_joueurs.classement()

    def entrer_joueur(self, nom_tournoi, lieu_tournoi):   # Peut-etre a mettre dans Tournoi ou dans Controller
        """ Enregistre un nouveau joueur ou recupere dans la base de donnees"""
        while True:
            choix = {1: "Creer nouveau joueur", 2: "Choisir joueur dans la base de donnee"}
            try:
                choix_utilisateur = int(input("Entrer 1 pour creer un joueur ou 2 pour \
choisir dans la base de donnees: "))
                if choix_utilisateur in choix:
                    if choix_utilisateur == 1:
                        creer_joueur = Joueur()
                        ajouter_a_db_joueur = creer_joueur.ajouter_joueur_db()
                        chercher_id = tournoi.table_joueur.get(doc_id=ajouter_a_db_joueur)
                        Joueur.ajouter_joueur_du_tournoi_a_db(Joueur, nom_tournoi, lieu_tournoi, chercher_id)
                        return ajouter_a_db_joueur
                    elif choix_utilisateur == 2:
                        joueur_recuperer = Joueur.recuperer_joueur_db(Joueur)
                        Joueur.ajouter_joueur_du_tournoi_a_db(Joueur, nom_tournoi, lieu_tournoi, joueur_recuperer)
                        return joueur_recuperer
                    else:
                        print("Votre choix ne fait pas partie des options possibles.")
                else:
                    print("Le choix est incorrecte")
            except ValueError:
                print("Le choix n'est pas valide, veuillez reesayer")

    def ajouter_joueur_db(self) -> list:
        """ Serialise le joueur et l'ajoute a la base de donnees 'Joueur' """
        serialise_joueur = {
            "nom": self.nom,
            "prenom": self.prenom,
            "naissance": self.date_de_naissance,
            "sexe": self.sexe,
            "classement": self.classement
        }
        tournoi.table_joueur.upsert(serialise_joueur,
                                    tournoi.user.nom == self.nom and tournoi.user.prenom == self.prenom)
        id_joueur = tournoi.table_joueur.get(tournoi.user.nom == self.nom and tournoi.user.prenom == self.prenom)
        return id_joueur.doc_id

    def ajouter_joueur_du_tournoi_a_db(self, nom_tournoi, lieu_tournoi, joueur_recuperer):
        """Ajoute le joueur a la table 'table_joueur_par_tournoi' de la db"""
        info_joueur = joueur_recuperer
        serialise_joueur = {
            "nom_du_tournoi": nom_tournoi + "," + lieu_tournoi,
            "nom": info_joueur["nom"],
            "prenom": info_joueur["prenom"],
            "naissance": info_joueur["naissance"],
            "sexe": info_joueur["sexe"],
            "classement": info_joueur["classement"],
            "score": 0
        }
        tournoi.table_joueur_par_tournoi.insert(serialise_joueur)
        return serialise_joueur

    def modifier_classement_joueur(self) -> str:
        """L'utilisateur peut modifier le classement d'un joueur par son ID"""
        while True:
            try:
                joueur_a_modifier = vue_joueurs.modifier_classement()
                joueur_trouve = tournoi.table_joueur.get(doc_id=joueur_a_modifier)
                if joueur_trouve is not None:
                    nouveau_classement = vue_joueurs.nouveau_classement()
                    tournoi.table_joueur.update({"classement": nouveau_classement}, doc_ids=[joueur_a_modifier])
                    return joueur_trouve
                else:
                    print("L'id ne fait pas partie de la DB.")
            except ValueError:
                print("Seulement les chiffres et les nombres sont acceptés")

    def recuperer_joueur_db(self):
        """ Recupere le joueur dans la base de donnees soit par 'nom et prenom' soit par 'id' """
        while True:
            choix_utilisateur = vue_joueurs.choix_utilisateur()
            if choix_utilisateur == 1:
                choix_nom = vue_joueurs.choix_par_nom()
                choix_prenom = vue_joueurs.choix_par_prenom()
                chercher_nom = tournoi.table_joueur.search(
                    (tournoi.user.nom == choix_nom) & (tournoi.user.prenom == choix_prenom))
                if chercher_nom != []:
                    print(chercher_nom)
                    return chercher_nom
                else:
                    print("Le joueur n'est pas enregistrer dans la DB")
            elif choix_utilisateur == 2:
                choix = vue_joueurs.choix_par_id()
                chercher_id = tournoi.table_joueur.get(doc_id=choix)
                if chercher_id != []:
                    print(chercher_id)
                    return chercher_id
                else:
                    print("Le joueur n'est pas enregistrer dans la DB")
            else:
                print("La recherche ne fait pas partie de la base de donnee")

    def classer_par_classement(self, table_db):
        """Pour que dans le rapport, les joueurs soient classés par ordre de classement"""
        liste_joueur = []
        for row in table_db:
            deserialise_joueur = [
                row["nom"],
                row["prenom"],
                row["naissance"],
                row["sexe"],
                row["classement"]
            ]
            liste_joueur.append(deserialise_joueur)
        liste_par_classement = sorted(liste_joueur, key=itemgetter(4), reverse=True)
        return liste_par_classement

    def classer_par_ordre_alphabetique(self, table_db):
        """Pour que dans le rapport, les joueurs soient classés par ordre alphabetique"""
        liste_joueur = []
        for row in table_db:
            deserialise_joueur = [
                row["nom"],
                row["prenom"],
                row["naissance"],
                row["sexe"],
                row["classement"]
            ]
            liste_joueur.append(deserialise_joueur)
        liste_par_ordre_alphabetique = sorted(liste_joueur, key=itemgetter(0))
        return liste_par_ordre_alphabetique

    def indice_joueur(self):
        """ Montre l'id du joueur"""
        vue_joueurs.indice_joueur()


def main():
    Joueur.indice_joueur(Joueur)


if __name__ == "__main__":
    main()
