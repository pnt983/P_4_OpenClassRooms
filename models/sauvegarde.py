from typing import Protocol
from tinydb import TinyDB, Query


class InterfaceTable(Protocol):
    """ Interface pour DB """

    def sauvegarder(self):
        ...

    def mettre_a_jour_joueur(self):
        ...

    def chercher_tournoi(self):
        ...

    def all(self):
        ...


class TableTiny(InterfaceTable):
    """ Implemente les methodes TinyDB """

    def __init__(self, db: TinyDB, user: Query, table_nom: str):
        self.table = db.table(table_nom)
        self.user = user

    def sauvegarder(self, data):
        id = self.table.insert(data)
        return id

    # def all(self):
    #     tous = self.table.all()
    #     montrer = print(tous)
    #     return montrer
