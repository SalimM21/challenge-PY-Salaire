
import math


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

# -----------------------------------------------------------
# Challenge : Fonction calculation() – somme et différence
def calculation(a, b):
    somme = a + b
    difference = a - b
    return somme, difference
  
# Appel de la fonction
if __name__ == "__main__":
    horaire_sup()
    calculation(5, 6)

# -----------------------------------------------------------
# Challenge : Mini-projets algorithmiques regroupés

def calcul_factorielle():
    try:
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
    except ValueError:
        print("Veuillez saisir un nombre entier valide.")

# -------------------------
def table_multiplication():
    try:
        m = int(input("Saisissez un nombre entier m: "))
        print(f"Table de multiplication de {m}:")
        multiplicateur = 1
        while multiplicateur <= 10:
            resultat = m * multiplicateur
            print(f"{m} × {multiplicateur} = {resultat}")
            multiplicateur += 1
    except ValueError:
        print("Veuillez saisir un nombre entier valide.")

def verifier_carre_parfait():
    
    try:
        L = int(input("Saisissez un nombre entier L: "))
        if L < 0:
            print(f"{L} n'est pas un carré parfait (nombre négatif).")
            return
        
        racine = int(math.sqrt(L))
        if racine * racine == L:
            print(f"{L} est un carré parfait (√{L} = {racine}).")
        else:
            print(f"{L} n'est pas un carré parfait.")
    except ValueError:
        print("Veuillez saisir un nombre entier valide.")

def afficher_caracteres():
    """Fonction 4: Affiche chaque caractère d'une chaîne un par un"""
    print("\n=== AFFICHAGE CARACTÈRES ===")
    chaine = input("Saisissez une chaîne de caractères: ")
    print("Caractères de la chaîne:")
    for i, caractere in enumerate(chaine):
        print(f"Position {i}: '{caractere}'")

def mot_le_plus_long():
    """Fonction 5: Trouve et affiche le mot le plus long d'une phrase"""
    print("\n=== MOT LE PLUS LONG ===")
    phrase = input("Saisissez une phrase: ")
    mots = phrase.split()
    
    if not mots:
        print("Aucun mot trouvé dans la phrase.")
        return
    
    mot_long = max(mots, key=len)
    print(f"Le mot le plus long est: '{mot_long}' ({len(mot_long)} caractères)")

def compter_occurrences():
    """Fonction 6: Compte les occurrences de chaque caractère dans une chaîne"""
    print("\n=== COMPTAGE DES OCCURRENCES ===")
    ch = input("Saisissez une chaîne de caractères Ch: ")
    
    # Dictionnaire pour stocker les occurrences
    occurrences = {}
    
    # Compter chaque caractère
    for caractere in ch:
        if caractere in occurrences:
            occurrences[caractere] += 1
        else:
            occurrences[caractere] = 1
    
    # Afficher les résultats
    print("Occurrences des caractères:")
    for caractere, nombre in sorted(occurrences.items()):
        if caractere == ' ':
            print(f"Le caractère 'espace' figure {nombre} fois dans la chaîne ch.")
        else:
            print(f"Le caractère \"{caractere}\" figure {nombre} fois dans la chaîne ch.")

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