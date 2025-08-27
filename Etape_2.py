from Etape_1 import MiseFondsInitiale

class CalculateurAnnuitees:

    def __init__(self, mise_fonds=None):

        self.mise_fonds = mise_fonds or MiseFondsInitiale()
        self.taux_global = self.mise_fonds.taux_global

        self.temps_debut = int(input("Quelle est l'année de début de cette série d'annuitées? (le projet débute en l'an 0) "))
        self.temps_fin = int(input("Quel est l'année de fin de cette série d'annuitées? "))
        self.annuitees = float(input("Quel est le montant des annuitées? ").replace(" ", ""))
        self.taux_croissance = (float(input("Quel est le taux de croissance/décroissance en pourcentage? (chiffre négatif pour décroissance) ")) / 100)

    def calculateur_VA_simple(self):

        if self.taux_global == 0:
            raise ValueError("Le taux d'intérêts ne peut pas être 0")

        duree = self.temps_fin - self.temps_debut  # nb de périodes
        if duree <= 0:
            return 0.0

        # Formule de la VA d'une rente ordinaire (paiements constants)
        valeur_actualisee = (
                self.annuitees * (1 - (1 + self.taux_global) ** -duree) / self.taux_global
        )

        # Décaler dans le temps (si la série commence après t=0)
        valeur_actualisee /= (1 + self.taux_global) ** self.temps_debut

        return valeur_actualisee

    def calculateur_VA_croissance(self):

        if self.taux_global == 0:
            raise ValueError("Le taux d'intérêts ne peut pas être 0")

        duree = self.temps_fin - self.temps_debut
        if duree <= 0:
            return 0.0

        if self.taux_croissance == 0:
            # si croissance nulle → même résultat que VA simple
            return self.calculateur_VA_simple()

        # Formule VA d’une rente croissante
        valeur_actualisee = (
                (self.annuitees / (self.taux_global - self.taux_croissance))
                * (1 - ((1 + self.taux_croissance) / (1 + self.taux_global)) ** duree)
        )

        # Décalage dans le temps
        valeur_actualisee /= (1 + self.taux_global) ** self.temps_debut

        return valeur_actualisee