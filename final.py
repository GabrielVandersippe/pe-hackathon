import numpy as np
import pandas as pd
import matplotlib as plt
from Planets_to_orbits import planets_to_orbits
from tri import get_planetsinfos

def trace_system(star : str):
    df = get_planetsinfos(star)
    D = planets_to_orbits(df)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')  # Affichage en 3D
    for planet,coord in D.items :
        ax.plot(coord[0], coord[1], coord[2], label= planet)
    plt.title("Système stellaire")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.tight_layout()
    plt.subplot()
    plt.show()
