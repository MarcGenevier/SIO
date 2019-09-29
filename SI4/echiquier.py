# Exercice 1
C_MAX = 8
L_MAX = 8
NORD = 1
EST = 2
SUD = 3
OUEST = 4

ligne = int(input("Saisir la ligne :"))

if ligne < 1 or ligne > L_MAX :
    print("Ligne Incorrecte.")
else:
    colonne = int(input("Saisir la colonne :"))
    if colonne > C_MAX or colonne < 1:
        print("Colonne incorrecte.")
    else:
        print("Coordonnées correctes.")

# Exercice 2
C_MAX = 8
L_MAX = 8
NORD = 1
EST = 2
SUD = 3
OUEST = 4

ligne = int(input("Saisir la ligne :"))

if ligne < 1 or ligne > L_MAX :
    print("Ligne Incorrecte.")
else:
    colonne = int(input("Saisir la colonne :"))
    if colonne > C_MAX or colonne < 1:
        print("Colonne incorrecte.")
    else:
        
        if ligne == 1 or ligne == L_MAX or colonne == 1 or colonne == C_MAX :
            print("Sur le bord.")
        else:
            print("n'est pas sur le bord.")

# Exercice 3
C_MAX = 8
L_MAX = 8
NORD = 1
EST = 2
SUD = 3
OUEST = 4

ligne = int(input("Saisir la ligne :"))

if ligne < 1 or ligne > L_MAX :
    print("Ligne Incorrecte.")
else:
    colonne = int(input("Saisir la colonne :"))
    if colonne > C_MAX or colonne < 1:
        print("Colonne incorrecte.")
    else:
        
        if ligne == 1 or ligne == L_MAX or colonne == 1 or colonne == C_MAX :
            print("Sur le bord.")
        else:
            print("n'est pas sur le bord.")
            
        if ligne == 1 and colonne == 1 or ligne == L_MAX and colonne == 1 or ligne == 1 and colonne == C_MAX or ligne == L_MAX and colonne == C_MAX :
            print("c'est un angle")



# Exercice 4
C_MAX = 8
L_MAX = 8
NORD = 1
EST = 2
SUD = 3
OUEST = 4




colonne = int(input("Saisir la colonne :"))
ligne = int(input("Saisir la ligne :"))

if ligne < 1 or ligne > L_MAX :
    print("Ligne Incorrecte.")
else:
    
    if colonne > C_MAX or colonne < 1:
        print("Colonne incorrecte.")
    else:
        
        if ligne == 1 or ligne == L_MAX or colonne == 1 or colonne == C_MAX :
            print("Sur le bord.")
        else:
            print("n'est pas sur le bord.")
            if ligne == 1 and colonne == 1 or ligne == L_MAX and colonne == 1 or ligne == 1 and colonne == C_MAX or ligne == L_MAX and colonne == C_MAX :
                print("c'est un angle")
            if colonne == 2 or colonne == 4 or colonne == 6 or colonne == 8 and ligne == 2 or ligne == 4 or ligne == 6 or ligne == 8 :
               print("La case est noire.")
            else:
                if colonne == 1 or colonne == 3 or colonne == 5 or colonne == 7 and ligne == 1 or ligne == 3 or ligne == 5 or ligne == 7 :
                    print("La case est blanche")
                

        
        