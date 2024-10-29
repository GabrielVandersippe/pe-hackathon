import numpy as np
import pandas as pd

df = pd.read_csv('Data_planets.csv', low_memory=False)
col = ['Planet Name', 'Eccentricity', 'Orbit Semi-Major Axis [au]', 'Inclination [deg]', 'Argument of Periastron [deg]']
df.set_index('rowid', inplace=True)
df_donnees_orbit = df[col]
df_donnees_orbit.dropna(axis=0, how='any', inplace=True)
by_star = (df[df['Number of Stars'] == 1]).groupby(by='Host Name')

def get_planetsinfos(star : str):
    df = pd.read_csv('Data_planets.csv', low_memory=False)
    col = ['Planet Name', 'Eccentricity', 'Orbit Semi-Major Axis [au]', 'Inclination [deg]', 'Argument of Periastron [deg]']
    df.set_index('rowid', inplace=True)
    df_donnees_orbit = df[col]
    df_donnees_orbit.dropna(axis=0, how='any', inplace=True)
    by_star = (df[df['Number of Stars'] == 1]).groupby(by='Host Name')
    list_index = by_star.get_group(star).index
    donnees_index = df_donnees_orbit.index
    intersec = list(set(list_index) & set(donnees_index))
    if not intersec :
        print('Pas de planètes exploitables pour des calculs dans ce système solaire')
        pass
    return df_donnees_orbit.loc[intersec]
