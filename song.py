# Entrée utilisateur

# affichage dans le terminal

val = input ("Entrez un nombre : ")

# affiche le message d'erreur si la val n'est pas un entier

try:
   val = int(val)
except ValueError:
   print("Vous devez choisir une valeur entre 0 et 99")

# mes variables

plural = "s "
more = "Plus de"
bowl = " bolée"

songPart1 = "de cidre sur le mur, "
songPart2 = "sans alcool. "
songPart3 = "Bois en un et au suivant ! "
songPart4 = "de cidre sur le mur."
songPart5 = "Vas au supermarché pour en acheter, 99 bolées de cidre sur le mur."

# mes conditions

if val > 2 and val <= 99 :
    # je convertis la val en chaîne de caractère str(val)
    print(str(val) + bowl + plural + songPart1 + str(val) + bowl + plural + songPart2)
    # décrémentation
    val -= 1
    print(songPart3 + str(val) + bowl + plural + songPart4)
elif val == 2 :
    print(str(val) + bowl + plural + songPart1 + str(val) + bowl + plural + songPart2)
    val -= 1
    print(songPart3 + str(val) + bowl + " " + songPart4)
elif val == 1 :
    print(str(val) + bowl + " " + songPart1 + str(val) + bowl + " " 
    + songPart2 + "\n" + songPart3 + more + bowl + plural + songPart4)      

# utilisation de f-strings 

elif val == 0 :
    print(f"{more}{bowl}{plural}{songPart1}\n{songPart5}")  
else :
    # message d'aide pour l'utilisateur
    print("Vous devez choisir une valeur entre 0 et 99")
