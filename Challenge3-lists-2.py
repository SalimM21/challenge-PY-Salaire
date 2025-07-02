# Compréhension de liste avec condition

def mots_communs_comprehension(chaine1, chaine2):
    mots_ch1 = chaine1.lower().split()
    mots_ch2 = chaine2.lower().split()
    
    # Liste des mots uniques de Ch1 qui sont aussi dans Ch2
    communs = list({mot for mot in mots_ch1 if mot in mots_ch2})
    return communs