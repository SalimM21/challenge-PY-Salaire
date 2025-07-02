
from ast import Return
import math

def horaire_sup(mon, salaire_horaire, heures_travaillees):

        # Calcul du salaire
    if heures_travaillees > 40:
        heures_supp = heures_travaillees - 40
        salaire_total = (40 * salaire_horaire) + (heures_supp * salaire_horaire * 1.5)
        detail = f"{heures_supp} heures sup à {salaire_horaire*1.5:.2f} dh/h"
    else:
        salaire_total = heures_travaillees * salaire_horaire
        detail = "Pas d'heures supplémentaires"

Return salaie_total, detail # type: ignore

# -----------------------------------------------------------
# Challenge : Fonction calculation() – somme et différence
def calculation(a, b):
    somme = a + b
    difference = a - b
    return somme, difference
  

horaire_sup("salim", 100, 45)
print(calculation(5, 6))

# -----------------------------------------------------------
# Challenge : Mini-projets algorithmiques regroupés

def calcul_factorielle():

    n = int(input("Saisissez un nombre entier n: "))
    if n < 0:
        print("La factorielle n'est pas définie pour les nombres négatifs.")
        return
        
    factorielle = 1
    i = 1
    while i <= n:
        factorielle *= i
        i += 1
        
    print(f"La factorielle de {n} est: {factorielle}")


# -----------------------------------------------------------
def table_multiplication():

        m = int(input("Saisissez un nombre entier m: "))
        print(f"Table de multiplication de {m}:")
        multiplicateur = 1
        while multiplicateur <= 10:
            resultat = m * multiplicateur
            print(f"{m} × {multiplicateur} = {resultat}")
            multiplicateur += 1

# -----------------------------------------------------------
def verifier_carre_parfait():
        
        L = int(input("Saisissez un nombre entier L: "))
        if L < 0:
            print(f"{L} n'est pas un carré parfait (nombre négatif).")
            return
        
        racine = int(math.sqrt(L))
        if racine * racine == L:
            print(f"{L} est un carré parfait (√{L} = {racine}).")
        else:
            print(f"{L} n'est pas un carré parfait.")

# -----------------------------------------------------------
def afficher_caracteres():
    
    print("\n=== AFFICHAGE CARACTÈRES ===")
    chaine = input("Saisissez une chaîne de caractères: ")
    for caractere in chaine:
        print(caractere)

# -----------------------------------------------------------
def mot_le_plus_long():
    
    print("\n=== MOT LE PLUS LONG ===")
    phrase = input("Saisissez une phrase: ")
    mots = phrase.split()
    
    mot_long = ""
    for mot in mots:
        if len(mot) > len(mot_long):
            mot_long = mot
    
    print(f"Le mot le plus long est: '{mot_long}'")

# -----------------------------------------------------------
def compter_occurrences():
    
    print("\n=== COMPTAGE DES OCCURRENCES ===")
    ch = input("Saisissez une chaîne de caractères Ch: ")
    
    for caractere in sorted(set(ch)):
        print(f"Le caractère \"{caractere}\" figure {ch.count(caractere)} fois dans la chaîne ch.")

# -----------------------------------------------------------
def menu_principal():
    """Menu principal pour exécuter les différentes fonctions"""
    while True:
        print("\n" + "="*50)
        print("MENU PRINCIPAL - EXERCICES PYTHON")
        print("="*50)
        print("1. Calcul de factorielle")
        print("2. Table de multiplication")
        print("3. Vérifier carré parfait")
        print("4. Afficher caractères")
        print("5. Mot le plus long")
        print("6. Compter occurrences")
        print("0. Quitter")
        
        try:
            choix = int(input("\nChoisissez une option (0-6): "))
            
            if choix == 1:
                calcul_factorielle()
            elif choix == 2:
                table_multiplication()
            elif choix == 3:
                verifier_carre_parfait()
            elif choix == 4:
                afficher_caracteres()
            elif choix == 5:
                mot_le_plus_long()
            elif choix == 6:
                compter_occurrences()
            elif choix == 0:
                print("Au revoir!")
                break
            else:
                print("Option invalide. Veuillez choisir entre 0 et 6.")
        except ValueError:
            print("Veuillez saisir un nombre valide.")
# Point d'entrée du programme
if __name__ == "__main__":
    menu_principal()