
class CreerTournoi:
    def __init__(self):
        pass

    def nom_tournoi(self) -> str:  # Fonction creer car sinon il me le redemande pas pour plusieurs tournois crees
        return input("Entree le nom de votre tournoi: ").capitalize()

    def lieu_tournoi(self) -> str:
        return input("Entree lieu du tournoi: ").capitalize()

    def nb_tours(self) -> str:
        while True:
            try:
                choix_utilisateur = input("Entree le nombre de tours voulu. Si vous voulez 4 \
tours, appuyer directement sur entree:")
                if not choix_utilisateur:
                    return "4"
                elif int(choix_utilisateur):
                    return f"{choix_utilisateur}"
                else:
                    print("Veuillez choisir un nombre. Les lettres ne sont pas autorises !")
            except ValueError:
                print("Veuillez choisir un nombre. Les lettres ne sont pas autorises !")

    def controle_temps(self):
        choix = {1: "Bullet", 2: "Blitz", 3: "Coup rapide"}
        while True:
            try:
                print("Taper 1 pour choisir Bullet, 2 pour choisir Blitz ou 3 pour choisir Coup rapide")
                choix_utilisateur = int(input("Entrer 1, 2 ou 3: "))
                if choix_utilisateur in choix:
                    return choix[choix_utilisateur]
                else:
                    print(f"Le choix {choix_utilisateur} ne fais pas partie des options possibles")
            except ValueError:
                print("Les lettres ne sont pas acceptees, veuillez saisir 1, 2 ou 3 pour faire votre choix")

    def description(self) -> str:  # J'ai cree une fonction pour pouvoir choisir l'ordre du print
        return input("Mot du directeur: ").capitalize()


def main():
    pass


if __name__ == "__main__":
    main()
