-#This program interacts with a user by asking to guess a number between 0 and 1001. The goal of the game
-# is to find the good number with the least attempts as possible.
-#This program is useful for testing abstract syntax tree methods because it has many loops.

from random import randrange
print("Ce jeu consiste à deviner un nombre compris entre 0 et 1000.\nPour abandonner taper 1001")

n=randrange(0,1001)
c=1
x=int(input("Essai n°1 : "))

while (x!=n) and (x!=1001):
    if (x<n):
        print("trop petit")
    else:
        print("trop grand")
    c=c+1
    x=int(input("Essai n°"+str(c)+" :"))

if x==n:
    print("Vous avez réussi en ",c,"essais")
else:
    print("Il fallait trouver ",n)
