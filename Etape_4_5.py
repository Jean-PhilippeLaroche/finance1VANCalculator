from Etape_1 import MiseFondsInitiale

class VARevente:

    def __init__(self, mise_fonds=None):
        self.mise_fonds = mise_fonds or MiseFondsInitiale()
        self.taux_global = self.mise_fonds.taux_global
        self.duree_projet = self.mise_fonds.duree_projet
        self.valeur_recuperation = float(input("Quelles sont les valeurs de récupération "
                                               "au total à la fin du projet (n'inclue pas "
                                               "la revente d'actifs au début de l'année n+1)? ").replace(" ", ""))

    def va_revente(self):
        va = self.valeur_recuperation / ((1 + self.taux_global) ** self.duree_projet)
        return va