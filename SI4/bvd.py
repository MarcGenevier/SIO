colonne = int(input("Saisir la colonne :"))
ligne = int(input("Saisir la ligne :"))
C_MAX = 8
L_MAX = 8

if colonne > C_MAX or colonne < 1 and ligne < 1 or ligne > L_MAX :
    print("Coordonnées incorrectes.")
if colonne == 2 or colonne == 4 or colonne == 6 or colonne == 8 and ligne == 2 or ligne == 4 or ligne == 6 or ligne == 8 :
    print("La case est noire.")
else:
    if colonne == 1 or colonne == 3 or colonne == 5 or colonne == 7 and ligne == 1 or ligne == 3 or ligne == 5 or ligne == 7 :
     print("La case est blanche")
                