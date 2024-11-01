# +
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Planets_to_orbits import planets_to_orbits
from tri import get_planetsinfos

# %matplotlib widget
# -

def trace_system(star : str):
    df = get_planetsinfos(star)
    D = planets_to_orbits(df)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')  # Affichage en 3D
    for planet,coord in D.items() :
        ax.plot(coord[:,0], coord[:,1], coord[:,2], label= planet)

    plt.plot(0,0,0, color = "yellow", marker = "o") 

    plt.title(f"Système {star}")
    ax.set_xlabel('X [ua]')
    ax.set_ylabel('Y [ua]')
    ax.set_zlabel('Z [ua]')
    ax.legend()
    ax.grid(False)
    plt.tight_layout()
    plt.subplot()
    plt.show()


trace_system("TOI-1136")


