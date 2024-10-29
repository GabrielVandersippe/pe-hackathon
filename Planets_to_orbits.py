#Programme qui, à partir d'une sous data-frame contenant une liste de planètes et leur position, renvoie un dictionnaire des orbites

import numpy as np
from Equation import orbite
from tilt import tilt

def planets_to_orbits(df, N = 1000):
    L = df.index()
    D = {}
    for planet in L:

        e = df.loc[planet,'Eccentricity']
        a = df.loc[planet,'Orbit Semi-Major Axis [au]']
        alpha = df.loc[planet, 'Inclination [deg]']
        beta = df.loc[planet, 'Argument of Periastron [deg]']

        points = orbite(e, a, N)
        points = tilt(points,(0,1,0), alpha)
        points = tilt(points,(-np.sin(alpha),0,np.cos(alpha)),beta)

        D[planet] = points