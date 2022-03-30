from colorama import init, Fore

init(autoreset=True)


option_principale = ["1- Gerer les tournois", "2- Gerer les joueurs", "3- Gerer les rapport", "4- Quitter le logiciel"]
option_tournoi = ["1- Creer un nouveau tournoi", "2- Reprendre un tournoi", "3- Revenir au menu principal"]
option_joueur = ["1- Enregistrer un joueur dans la base de données", "2- Modifier le classement d'un joueur", "3- Revenir \
au menu principal"]
option_rapport = ["1- Voir tous les joueurs de la base de donnees", "2- Voir tous les joueurs d'un tournoi", "3- Voir \
tous les tournois", "4- Voir tous les tours d'un tournoi", "5- Voir tous les matchs d'un tournoi", "6- Revenir au menu \
principal"]


class Menu:

    def __init__(self, titre, options):
        self.titre = titre
        self.options = options

    def afficher(self):
        while True:
            print(Fore.BLUE + f"\n*************** {self.titre} ***************\n")
            for option in self.options:
                print(Fore.GREEN + option + "\n")
            choix_utilisateur = input(Fore.MAGENTA + "Entrer le numero de votre choix: " + Fore.RESET)
            try:
                if int(choix_utilisateur) > 0 and int(choix_utilisateur) <= len(self.options):
                    return choix_utilisateur
                else:
                    print("Choix incorrect !")
            except ValueError:
                print("Seul les chiffres sont acceptés.")


if __name__ == "__main__":
    pass
