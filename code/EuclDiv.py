-#This program performs the euclidian division of 2 integers and returns the quotient and the remainder.
-#It will allow us to use the error guessing technique and also the mutation testing technique to see if the way it is implemented
-#in Python is also good for another programming language.

def div_eucl(a,b):
    q = a//b    # Division entière
    r = a%b     # Opérateur 'modulo' qui renvoie le reste
    return (q,r)
