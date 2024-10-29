import matplotlib.pyplot as plt
import numpy as np

# Tableau pour les 3 axes
# Création d'un tableau de 100 points entre -4*pi et 4*pi
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)  # Création du tableau de l'axe z entre -2 et 2
r = z**2 + 1
x = r * np.sin(theta)  # Création du tableau de l'axe x
y = r * np.cos(theta)  # Création du tableau de l'axe y

# Tracé du résultat en 3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')  # Affichage en 3D
ax.plot(x, y, z, label='Courbe')  # Tracé de la courbe 3D
plt.title("Ensemble des trajectoires du système")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.tight_layout()
plt.subplot()
plt.show()
