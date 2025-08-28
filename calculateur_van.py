from Etape_1 import MiseFondsInitiale
from Etape_2 import CalculateurAnnuitees
from Etape_3 import VAEIACC
from Etape_4_5 import VARevente
from Etape_6 import VAImpotGainCapital
from Etape_7_8 import VaFermeture


class CalculateurVAN:

    def __init__(self):
        # saisie unique des paramètres du projet
        self.mise_fonds = MiseFondsInitiale()
        self.nombre_mise_fonds = int(input("Combien y a-t-il de bloc de mise de fonds différents? "))

        # objets liés au projet (utilisent mise_fonds)
        self.nombre_annuitees = int(input("Combien y a-t-il de séries d'annuitées différentes? "))

        self.va_revente_obj = VARevente(self.mise_fonds)

        self.nombre_actif = int(input("Combien d'actifs ont été utilisé pendant le projet? "))
        self.actifs_vaeiacc = []
        self.actifs_vaimpot = []
        self.actifs_vafermeture = []

        # pour stocker les séries d'annuités après saisie et calcul
        self.series_annuitees = []

        self.mises_fonds = []

    def valeur_etape_1(self):
        total = 0
        self.mises_fonds = []  # on garde en mémoire chaque mise

        for i in range(self.nombre_mise_fonds):
            print(f"\n--- Bloc de mise de fonds {i + 1} (étape 1) ---")
            mise = MiseFondsInitiale()  # saisie des infos pour ce bloc
            self.mises_fonds.append(mise)

            # calcul immédiat
            valeur = mise.mise_de_fonds_initiale()
            print(f"Valeur actualisée de la mise de fonds {i + 1}: {valeur:.2f}")

            total += valeur

        print(f"\nTotal des mises de fonds (étape 1) : {total:.2f}")
        return total

    def valeur_etape_2(self):
        total = 0
        self.series_annuitees = []

        for i in range(self.nombre_annuitees):
            print(f"\n--- Série d'annuités {i + 1} (étape 2) ---")
            annuitee = CalculateurAnnuitees(self.mise_fonds)  # saisie série par série
            self.series_annuitees.append(annuitee)

            # calcul immédiat
            if annuitee.taux_croissance == 0:
                valeur = annuitee.calculateur_VA_simple()
            else:
                valeur = annuitee.calculateur_VA_croissance()

            print(f"Valeur actualisée de la série {i + 1}: {valeur:.2f}")
            total += valeur

        print(f"\nTotal des séries d'annuités (étape 2) : {total:.2f}")
        return total

    def valeur_etape_3(self):
        """
        Crée (si nécessaire) et utilise une instance VAEIACC par actif.
        Les objets sont créés une seule fois et stockés dans self.actifs_vaeiacc.
        """
        if not self.actifs_vaeiacc:
            # créer les actifs (saisie des caractéristiques une seule fois)
            for i in range(self.nombre_actif):
                print(f"--- Actif {i + 1} (étape 3) ---")
                actif = VAEIACC(self.mise_fonds)
                self.actifs_vaeiacc.append(actif)

        # somme des VAEIACC (ne recrée pas les actifs)
        somme = 0
        for actif in self.actifs_vaeiacc:
            somme += actif.calculateur_vaeiacc()
        return -1 * somme  # signe négatif tel que dans ta logique originale

    def valeur_etape_4_5(self):
        return self.va_revente_obj.va_revente()

    def valeur_etape_6(self):
        """
        Calcule l'impôt sur gain en capital pour *chaque actif déjà créé*.
        Si les actifs n'existent pas encore, on appelle valeur_etape_3() pour les créer.
        """
        if not self.actifs_vaeiacc:
            # garantit que les actifs existent
            self.valeur_etape_3()

        self.actifs_vaimpot = []
        total = 0
        for i, actif in enumerate(self.actifs_vaeiacc, start=1):
            va_impot_obj = VAImpotGainCapital(actif, self.mise_fonds)
            self.actifs_vaimpot.append(va_impot_obj)
            total += va_impot_obj.va_impot_gain_capital()
        return total

    def valeur_etape_7_8(self):
        """
        Pour chaque actif créé, si fermeture_categorie == "oui", on calcule VaFermeture.
        Retourne la somme (0 si aucun actif concerné).
        """
        if not self.actifs_vaeiacc:
            self.valeur_etape_3()

        self.actifs_vafermeture = []
        valeurs = []
        for i, actif in enumerate(self.actifs_vaeiacc, start=1):
            if actif.fermeture_categorie == "oui":
                fermeture_obj = VaFermeture(actif, self.mise_fonds)
                self.actifs_vafermeture.append(fermeture_obj)
                valeurs.append(fermeture_obj.va_economie_ou_perte())

        return sum(valeurs) if valeurs else 0

    def valeur_totale(self):
        """
        Somme des étapes (1..7/8). Si une étape renvoie None, on la considère comme 0.
        On appelle les étapes dans l'ordre pour garantir la création des actifs.
        """
        et1 = self.valeur_etape_1() or 0
        et2 = self.valeur_etape_2() or 0
        et3 = self.valeur_etape_3() or 0
        et45 = self.valeur_etape_4_5() or 0
        et6 = self.valeur_etape_6() or 0
        et78 = self.valeur_etape_7_8() or 0

        return et1 + et2 + et3 + et45 + et6 + et78