class MiseFondsInitiale:

    def __init__(self):
       self.duree_projet = float(input("Quelle est la durée du projet en années? "))
       self.conversion_taux = input("Le taux d'intérêts donné est-il en année, en trimestre, en mois, en semaine ou en jour? ").strip().lower()
       self.taux_global = (float(input("Quel est le taux d'intérêts du projet en pourcentage? "))) / 100
       self.mise_initiale = float(input("Quelle est la mise de fonds initiale du projet? ").strip())
       self.taux_imposition = (float(input("Quel est le taux d'imposition de l'entreprise en pourcentage? "))) / 100
       self.taux_global = self._convertisseur_taux()

    def mise_de_fonds_initiale(self):
        mise = -1 * self.mise_initiale
        return mise

    def _convertisseur_taux(self):
        if self.conversion_taux == "année":
            return self.taux_global
        elif self.conversion_taux == "trimestre":
            return (1 + self.taux_global) ** 4 - 1
        elif self.conversion_taux == "mois":
            return (1 + self.taux_global) ** 12 - 1
        elif self.conversion_taux == "semaine":
            return (1 + self.taux_global) ** 52 - 1
        elif self.conversion_taux == "jour":
            return (1 + self.taux_global) ** 365 - 1
        else:
            raise ValueError("Le taux n'est pas valide")