val = input ("Entrez un nombre : ")
try:
   val = int(val)
except ValueError:
   print("Vous devez choisir une valeur entre 0 et 99")

plural = "s "
plusDe = "Plus de"
bolee = " bolée"

songPart1 = "de cidre sur le mur, ";
songPart2 = "sans alcool. ";
songPart3 = "Bois en un et au suivant ! "
songPart4 = "de cidre sur le mur."
songPart5 = "\nVas au supermarché pour en acheter, 99 bolées de cidre sur le mur."

if val > 2 and val < 99 :
    print(str(val) + bolee + plural + songPart1 + str(val) + bolee + plural + songPart2)
    val = val - 1
    print(songPart3 + str(val) + bolee + plural + songPart4)
elif val == 2 :
    print(str(val) + bolee + plural + songPart1 + str(val) + bolee + plural + songPart2)
    val = val - 1
    print(songPart3 + str(val) + bolee + " " + songPart4)
elif val == 1 :
    print(str(val) + bolee + " " + songPart1 + str(val) + bolee + " " 
    + songPart2 + "\n" + songPart3 + plusDe + bolee + plural + songPart4)      
    # utilisation de f-strings 
elif val == 0 :
    print(f"{plusDe}{bolee}{plural}{songPart1}{songPart5}")  
else :
    print("Vous devez choisir une valeur entre 0 et 99")
