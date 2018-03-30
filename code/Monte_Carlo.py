from random import random

n=int(input(" donner le nombre de tirs souhaité n = "))
compt=0


for i in range (0,n):
    x = random()
    y = random()
    if ((x**2+y**2)**0.5) < 1 :
        compt=compt+1

print(" approximation de pi : ",4*compt/n)
