#Code qui definit une fonction, qui, à partir d'une excentricité et d'un demi grand axe, renvoie une liste de points qui décrit l'orbite

import numpy as np

def orbite(e, a, N = 1000):
    '''e : excentricité ; a : demi gd axe, N nb de points'''
    b = a * np.sqrt(1-e**2) #demi petit axe
    c = np.sqrt(a**2 - b**2) #distance séparant le centre et l'un des foyers


    X = np.arange(-a,a,2*a/N)

    Y = np.empty(2*N - 2)

    Y[:N] = b*np.sqrt(1-np.square(X/a))
    Y[N:] = -b*np.sqrt(1-np.square(X/a))[1:-1]

    return (X-c,Y)