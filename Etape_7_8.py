from Etape_1 import MiseFondsInitiale
from Etape_3 import VAEIACC

class VaFermeture:

    def __init__(self, actif: VAEIACC, mise_fonds: MiseFondsInitiale):
        self.actif = actif
        self.mise_fonds = mise_fonds

    def va_economie_ou_perte(self):
        fnacc = self.actif.calculateur_fnacc()
        r = self.actif.r
        taux_imp = self.mise_fonds.taux_imposition
        taux_global = self.mise_fonds.taux_global
        duree = self.mise_fonds.duree_projet

        va = ((fnacc - r) * taux_imp) / ((1 + taux_global) ** (duree + 1))
        return va