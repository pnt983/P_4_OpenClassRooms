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

    def recuperer_joueur_par_id(self, liste_matchs):
        liste_joueurs = []
        for row in liste_matchs["Matchs"]:
            joueur_id = row[0]
            if row[1] == 0:
                resultat = "Perdu"
            elif row[1] == 1:
                resultat = "Gagné"
            elif row[1] == 0.5:
                resultat = "Egalité"
            for element in self.table_joueur:
                if joueur_id == element["id"][0]:
                    joueur = element["nom"], element["prenom"], resultat
                    liste_joueurs.append(joueur)
        return liste_joueurs

    def recuperer_rounds_tournoi(self, nom_tournoi, lieu_tournoi):
        table_tournoi = self.table_tournoi.search(self.user.nom_du_tournoi == nom_tournoi and self.user.
                                                  lieu == lieu_tournoi)
        for rounds in table_tournoi:
            liste_rounds = []
            for round in rounds["rounds"]:
                liste_matchs = []
                info_round = round["nom_round"], round["date_debut_round"], round["date_fin_round"]
                liste_rounds.append(info_round)
                for row in round["matchs_round"]:
                    match = self.recuperer_joueur_par_id(row)
                    liste_matchs.append(match)
                liste_rounds.extend(liste_matchs)
        return liste_rounds

    def recuperer_matchs_tournoi(self, nom_tournoi, lieu_tournoi):
        table_tournoi = self.table_tournoi.search(self.user.nom_du_tournoi == nom_tournoi and self.user.
                                                  lieu == lieu_tournoi)
        liste_matchs = []
        for rounds in table_tournoi:
            for round in rounds["rounds"]:
                for row in round["matchs_round"]:
                    match = self.recuperer_joueur_par_id(row)
                    liste_matchs.append(match)
        return liste_matchs

    def classer_par_ordre_alphabetique(self, liste_joueurs, item: int = 0):
        liste_par_alphabet = sorted(liste_joueurs, key=itemgetter(item), reverse=False)
        return liste_par_alphabet

    def classer_par_classement(self, liste_joueurs, item: int = 4):
        liste_par_classement = sorted(liste_joueurs, key=itemgetter(item), reverse=True)
        return liste_par_classement
