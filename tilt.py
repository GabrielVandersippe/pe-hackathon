import numpy as np


def tilt(points, alpha, D = (0,1,0)):
    '''L'objectif est à partir d'un ensemble de points en 2D, de la donnée d'un axe D et d'un angle alpha, de renvoyer l'ensemble des points après une rotation d'angle alpha selon D.
    points : tableau numpy de points [x, y, z=0]
    alpha : float en radian
    D : (x,y,z) D est la droite engendrée par le vecteur (x,y,z)
    '''
    if D[0] != 0:
        theta = np.arctan(D[1]/D[0])
    else:
        theta = np.pi/2
    phi = np.pi/2 - np.arctan(D[2]/np.sqrt(D[0]**2 + D[1]**2))
    @np.vectorize
    def rotation(point):
        R1 = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
        R2 = np.array([[np.cos(phi), 0, -np.sin(phi)], [0, 1, 0], [np.sin(phi), 0, np.cos(phi)]])
        R3 = np.array([[np.cos(alpha), -np.sin(alpha), 0], [np.sin(alpha), np.cos(alpha), 0], [0, 0, 1]])
        return np.dot(np.linalg.inv(np.dot(R2, R1)), np.dot(R3, np.dot(R2, np.dot(R1, point))))
    return rotation(points)
