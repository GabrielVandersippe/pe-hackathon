# Code qui definit une fonction, qui, à partir d'une excentricité et d'un demi grand axe, renvoie une liste de points qui décrit l'orbite

import numpy as np

def orbite(e, a, N = 1000):
    '''e : excentricité ; a : demi gd axe, N nb de points'''
    b = a * np.sqrt(1-e**2) #demi petit axe
    c = np.sqrt(a**2 - b**2) #distance séparant le centre et l'un des foyers


    X = np.arange(-a,a,2*a/N)

    Y = np.empty(2*N - 2)

    Y[:N] = b*np.sqrt(1-np.square(X/a))
    Y[N:] = -b*np.sqrt(1-np.square(X/a))[-2:0:-1]

    Mat = np.zeros((2*N-2,3))

    Mat[:N,0] = X-c
    Mat[N:,0] = (X-c)[-2:0:-1]
    Mat[:,1] = Y

    return Mat
