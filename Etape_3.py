from Etape_1 import MiseFondsInitiale


class VAEIACC:

    def __init__(self, mise_fonds=None):
        self.mise_fonds = mise_fonds or MiseFondsInitiale()
        self.taux_imposition = self.mise_fonds.taux_imposition
        self.cout_capital_initial = float(input("Quel est le coût en capital initial de l'actif? ").replace(" ", ""))
        self.taux_acc = (float(input("Quel est le taux d'ACC pour cette catégorie d'actif en pourcentage? "))) / 100
        self.valeur_vente = float(input("Quelle est la valeur de revente de l'actif? ").replace(" ", ""))
        self.r = min(self.cout_capital_initial, self.valeur_vente)
        self.taux_actualisation = (float(input("Quel est le taux d'actualisation en pourcentage? "))) / 100
        self.duree_vie_actif = (float(input("Quelle est la durée de vie de l'actif en années? ")))
        self.fermeture_categorie = input("Est-ce qu'il y a une fermeture de catégorie? (Oui/Non) ").strip().lower()

    def calculateur_fnacc(self):
        fnacc = (self.cout_capital_initial * (1 - (1.5 * self.taux_acc))
                 * ((1 - self.taux_acc) ** (self.duree_vie_actif - 1)))
        return fnacc

    def calculateur_vaeiacc(self):
        if self.fermeture_categorie == "oui":
            vaeiacc = (
                    (self.cout_capital_initial * self.taux_acc * self.taux_imposition)
                    / (self.taux_actualisation + self.taux_acc)
                    * ((1 + (1.5 * self.taux_actualisation))
                       / (1 + self.taux_actualisation))
                    - ((self.calculateur_fnacc() * self.taux_acc * self.taux_imposition)
                       / (self.taux_actualisation + self.taux_acc))
                    * (1 / ((1 + self.taux_actualisation) ** self.duree_vie_actif)
                       ))
            return vaeiacc

        else:

            vaeiacc = (
                    (self.cout_capital_initial * self.taux_acc * self.taux_imposition)
                    / (self.taux_actualisation + self.taux_acc)
                    * ((1 + (1.5 * self.taux_actualisation))
                    / (1 + self.taux_actualisation))
                    - ((self.r * self.taux_acc * self.taux_imposition)
                    / (self.taux_actualisation + self.taux_acc))
                    * (1 / ((1 + self.taux_actualisation) ** self.duree_vie_actif)
                        ))
            return vaeiacc