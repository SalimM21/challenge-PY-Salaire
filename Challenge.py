
def horaire_sup():
     
    try:
        # Saisie des données
        nom = input("Entrez votre nom : ").strip()
        if not nom:
            raise ValueError("Le nom ne peut pas être vide")
        
        salaire_horaire = float(input("Entrez votre salaire horaire (dh) : "))
        if salaire_horaire <= 0:
            raise ValueError("Le salaire horaire doit être positif")
        
        heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
        if heures_travaillees < 0:
            raise ValueError("Les heures travaillées ne peuvent pas être négatives")

        # Calcul du salaire
        if heures_travaillees > 40:
            heures_supp = heures_travaillees - 40
            salaire_total = (40 * salaire_horaire) + (heures_supp * salaire_horaire * 1.5)
            detail = f"{heures_supp} heures sup à {salaire_horaire*1.5:.2f} dh/h"
        else:
            salaire_total = heures_travaillees * salaire_horaire
            detail = "Pas d'heures supplémentaires"

        # Affichage des résultats
        print("\n" + "-"*30)
        print(f"NOM : {nom.upper()}")
        print(f"SALAIRE TOTAL : {salaire_total:.2f} dh")
        print(f"DÉTAIL : {detail}")
        print("-"*30)

    except ValueError as e:
        print(f"\nERREUR : {e}")
        print("Veuillez relancer le programme avec des valeurs valides.")

# Appel de la fonction
# -----------------------------------------------------------
# Challenge : Fonction calculation() – somme et différence
def calculation(a, b):
    somme = a + b
    difference = a - b
    return somme, difference  

if __name__ == "__main__":
    horaire_sup()
    calculation(5, 6)

# Challenge : Mini-projets algorithmiques regroupés