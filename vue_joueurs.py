import tournoi


def nom() -> str:
    return input("Nom du joueur: ").capitalize()


def prenom() -> str:
    return input("Prenom du joueur: ").capitalize()


def date_de_naissance() -> str:
    return input("Date de naissance du joueur. Format: jj/mm/aaaa: ")


def sexe() -> str:
    while True:
        choix = input("Entrer M pour les hommes et F pour les femmes: ").capitalize()
        longueur = choix.__len__()
        if longueur > 0 and longueur < 2:
            if choix == "M" or choix == "F":
                return choix
            else:
                print("Seulement F ou M.")
        else:
            print("Seulement un seul caractere.")


def classement() -> int:
    while True:
        choix = int(input("Classement du joueur: "))
        if choix >= 0:
            return choix
        else:
            print("Le classement d'un joueur ne peut pas etre negatif.")


def choix_utilisateur():
    return int(input("Taper 1 pour chercher par nom et prenom. Ou 2 \
pour choisir par id: "))


def choix_par_nom():
    return input("Entrer le nom du joueur: ").capitalize()


def choix_par_prenom():
    return input("Entrer le prenom du joueur: ").capitalize()


def choix_par_id():
    for row in tournoi.table_joueur:
        print(f"ID joueur: {row.doc_id} {row}")
    return int(input("Entrer l'id du joueur: "))


def modifier_classement() -> int:
    for row in tournoi.table_joueur:
        print(f"ID joueur: {row.doc_id} {row}")
    return int(input("Entrer l'id du joueur: "))


def nouveau_classement() -> int:
    return int(input("Entrer le nouveau classement du joueur: "))


def indice_joueur():
    for row in tournoi.table_joueur:
        print(f"ID joueur: {row.doc_id} {row}")


def main():
    date_de_naissance()


if __name__ == "__main__":
    main()
