from Etape_1 import MiseFondsInitiale
from Etape_3 import VAEIACC

class VAImpotGainCapital:
    def __init__(self, actif: VAEIACC, mise_fonds: MiseFondsInitiale):
        self.vaeiacc = actif
        self.mise_fonds = mise_fonds

    def va_impot_gain_capital(self):
        va = (
            -1 * (((self.vaeiacc.valeur_vente - self.vaeiacc.cout_capital_initial)
                   * 0.6667 * self.vaeiacc.taux_imposition)
                  / ((1 + self.mise_fonds.taux_global) ** (self.mise_fonds.duree_projet + 1)))
        )
        return va