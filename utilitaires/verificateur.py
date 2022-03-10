from . import database


class Verification:
    """"Verification des inputs"""

    def verifier_input_remplit(fonction):
        def wrapper(*args, **kwargs):
            while True:
                resultat = fonction(*args, **kwargs)
                if len(resultat) > 0:
                    return resultat
                else:
                    print("Le champs ne peut pas etre vide.")
        return wrapper

    def verifier_sexe(fonction):
        def wrapper(*args, **kwargs):
            while True:
                resultat = fonction(*args, **kwargs)
                if len(resultat) < 2 and len(resultat) > 0:
                    if resultat == "M" or resultat == "F":
                        return resultat
                else:
                    print("Entrer seulement la lettre 'f' ou 'm'.")
        return wrapper

    def verifier_classement(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    resultat = fonction(*args, **kwargs)
                    if int(resultat) >= 0:
                        return resultat
                    else:
                        print("Le classement ne peut pas etre négatif.")
                except ValueError:
                    ValueError(print("Le champs ne peut pas etre vide."))
        return wrapper

    def verifier_date_naissance(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    resultat = fonction(*args, **kwargs)
                    if len(resultat) == 10:
                        if int(resultat[0:2]) > 0 and int(resultat[0:2]) <= 31:
                            if int(resultat[3:5]) > 0 and int(resultat[3:5]) <= 12:
                                if int(resultat[6:10]) > 1900 and int(resultat[6:10]) < 2022:
                                    return resultat
                    else:
                        print("Veuillez respecter le format jj/mm/aaaa.")
                except ValueError:
                    ValueError(print("Le champs ne peut pas etre vide"))
        return wrapper

    def verifier_nombre_tours(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    choix_utilisateur = fonction(*args, **kwargs)
                    if len(choix_utilisateur) == 0:
                        return 4
                    else:
                        int(choix_utilisateur)
                        return choix_utilisateur
                except ValueError:
                    print("Entrer seulement un chiffre ou un nombre.")
        return wrapper

    def verifier_controle_temps(fonction):
        def wrapper(*args, **kwargs):
            while True:
                choix = {1: "Bullet", 2: "Blitz", 3: "Coup rapide"}
                try:
                    choix_utilisateur = fonction(*args, **kwargs)
                    if choix_utilisateur in choix:
                        return choix[choix_utilisateur]
                    else:
                        print("Choix incorrect.")
                except ValueError:
                    print("Veuillez choisir parmi les choix disponibles.")
        return wrapper

    def verifier_qui_gagne(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    choix_utilisateur = fonction(*args, **kwargs)
                    if choix_utilisateur == 1:
                        return choix_utilisateur
                    elif choix_utilisateur == 2:
                        return choix_utilisateur
                    elif choix_utilisateur == 3:
                        return choix_utilisateur
                    else:
                        print("Choix incorrect.")
                except ValueError:
                    print("Veuillez choisir parmi les choix disponibles.")
        return wrapper

    def verifier_alphabetique_ou_classement(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    choix_utilisateur = fonction(*args, **kwargs)
                    if choix_utilisateur == 1:
                        return choix_utilisateur
                    elif choix_utilisateur == 2:
                        return choix_utilisateur
                except ValueError:
                    print("Veuillez choisir parmi les choix disponibles.")
        return wrapper

    def verifier_nom_dans_db(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    choix_utilisateur = fonction(*args, **kwargs)
                    table_db = database.TABLE_TOURNOI.all()
                    liste_noms = []
                    for row in table_db:
                        nom_tournoi = row["nom_du_tournoi"]
                        liste_noms.append(nom_tournoi)
                    if choix_utilisateur in liste_noms:
                        return choix_utilisateur
                    else:
                        print("Le choix n'est pas valide.")
                except ValueError:
                    print("Veuillez choisir parmi les choix disponibles.")
        return wrapper

    def verifier_lieu_dans_db(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    choix_utilisateur = fonction(*args, **kwargs)
                    table_db = database.TABLE_TOURNOI.all()
                    liste_lieux = []
                    for row in table_db:
                        nom_tournoi = row["lieu"]
                        liste_lieux.append(nom_tournoi)
                    if choix_utilisateur in liste_lieux:
                        return choix_utilisateur
                    else:
                        print("Le choix n'est pas valide.")
                except ValueError:
                    print("Veuillez choisir parmi les choix disponibles.")
        return wrapper

    def verifier_doc_id(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    choix_utilisateur = fonction(*args, **kwargs)
                    table_joueur = database.TABLE_JOUEUR
                    liste_ids = []
                    for row in table_joueur:
                        liste_ids.append(row.doc_id)
                    if choix_utilisateur in liste_ids:
                        return choix_utilisateur
                    else:
                        print("Le choix n'est pas valide.")
                except ValueError:
                    print("Veuillez choisir parmi les choix disponibles.")
        return wrapper

    def verifier_nom_tournoi(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    choix_utilisateur = fonction(*args, **kwargs)
                    tous_les_tournois = database.TABLE_TOURNOI.all()
                    liste_tournois_encours = []
                    for tournoi in tous_les_tournois:
                        if tournoi["etat_tournoi"] == "en_cours":
                            infos_tournoi = tournoi["nom_du_tournoi"]
                            liste_tournois_encours.append(infos_tournoi)
                    if choix_utilisateur in liste_tournois_encours:
                        return choix_utilisateur
                    else:
                        print("Le choix n'est pas valide.")
                except ValueError:
                    print("Veuillez choisir parmi les choix disponibles.")
        return wrapper

    def verifier_lieu_tournoi(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    choix_utilisateur = fonction(*args, **kwargs)
                    tous_les_tournois = database.TABLE_TOURNOI.all()
                    liste_tournois_encours = []
                    for tournoi in tous_les_tournois:
                        if tournoi["etat_tournoi"] == "en_cours":
                            infos_tournoi = tournoi["lieu"]
                            liste_tournois_encours.append(infos_tournoi)
                    if choix_utilisateur in liste_tournois_encours:
                        return choix_utilisateur
                    else:
                        print("Le choix n'est pas valide.")
                except ValueError:
                    print("Veuillez choisir parmi les choix disponibles.")
        return wrapper

    def verifier_nombre_joueurs(fonction):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    choix_nombre_joueurs = fonction(*args, **kwargs)
                    if not choix_nombre_joueurs:
                        return 8
                    elif (int(choix_nombre_joueurs) % 2) == 0:
                        return int(choix_nombre_joueurs)
                    else:
                        print("Entrer uniquement un chiffre pair")
                except ValueError:
                    print("Uniquement les chiffres sont acceptés")
        return wrapper
