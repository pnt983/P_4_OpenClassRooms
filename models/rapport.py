from operator import itemgetter


class Rapport:

    def __init__(self, db_table_joueur, db_table_tournoi, requete):
        self.user = requete
        self.table_joueur = db_table_joueur
        self.table_tournoi = db_table_tournoi

    def recuperer_table_joueur(self):
        joueur_dans_db = self.table_joueur.all()
        liste_joueurs = []
        for joueur in joueur_dans_db:
            deserialise = [
                joueur["nom"],
                joueur["prenom"],
                joueur["naissance"],
                joueur["sexe"],
                joueur["classement"]
            ]
            liste_joueurs.append(deserialise)
        return liste_joueurs

    def recuperer_joueurs_tournoi(self, nom_tournoi, lieu_tournoi):
        joueur_par_tournoi = self.table_tournoi.search(self.user.nom_du_tournoi == nom_tournoi and self.user.
                                                       lieu == lieu_tournoi)
        liste_joueurs = []
        for row in joueur_par_tournoi:
            for joueur in row["joueurs"]:
                deserialise = [
                    joueur["nom"],
                    joueur["prenom"],
                    joueur["naissance"],
                    joueur["sexe"],
                    joueur["classement"],
                    joueur["score"]
                ]
                liste_joueurs.append(deserialise)
            return liste_joueurs

    def recuperer_table_tournoi(self):
        tous_les_tournois = self.table_tournoi.all()
        liste_tournois = []
        for tournoi in tous_les_tournois:
            infos_tournoi = [tournoi["nom_du_tournoi"], tournoi["lieu"], tournoi["date"], tournoi["nombre_de_tour"],
                             tournoi["controle_du_temps"], tournoi["description"], tournoi["etat_tournoi"]]
            liste_tournois.append([infos_tournoi])
        return liste_tournois

    def recuperer_nom_tournois(self):
        table_tournoi = self.table_tournoi.all()
        liste_tournois = []
        for row in table_tournoi:
            infos_tournoi = [row["nom_du_tournoi"], row["lieu"], row["date"], row["nombre_de_tour"],
                             row["controle_du_temps"], row["description"], row["etat_tournoi"]]
            liste_tournois.append(infos_tournoi)
        return liste_tournois

    def recuperer_rounds_tournoi(self, nom_tournoi, lieu_tournoi):
        table_tournoi = self.table_tournoi.search(self.user.nom_du_tournoi == nom_tournoi and self.user.
                                                  lieu == lieu_tournoi)
        for row in table_tournoi:
            rounds = row["rounds"]
        return rounds

    def recuperer_matchs_tournoi(self, nom_tournoi, lieu_tournoi):
        table_tournoi = self.table_tournoi.search(self.user.nom_du_tournoi == nom_tournoi and self.user.
                                                  lieu == lieu_tournoi)
        liste_matchs = []
        for row in table_tournoi:
            for match in row["rounds"]:
                matchs = match["matchs_round"]
                liste_matchs.extend(matchs)
        return liste_matchs

    def classer_par_ordre_alphabetique(self, liste_joueurs, item: int = 0):
        liste_par_alphabet = sorted(liste_joueurs, key=itemgetter(item), reverse=False)
        return liste_par_alphabet

    def classer_par_classement(self, liste_joueurs, item: int = 4):
        liste_par_classement = sorted(liste_joueurs, key=itemgetter(item), reverse=True)
        return liste_par_classement
