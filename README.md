# pe-hackathon


**OBJECTIF : Représenter, pour une étoile donnée, les trajectoires des planètes autour**

Todo : 
- Rassembler les planètes par leur étoile, et qui n'ont qu'une étoile, les trier pour savoir si elles sont correctes (Quentin)
- Les transformer en une sous data-frame à rentourner (Quentin)
- Trouver les orbites des planètes autour de leur astre (Gabriel et Eliott)
    Relation entre excentricité e, et demi-grand axe a :
    b = a*sqrt(1-e²)
    l'ellipse vérifie alors x²/a² + y²/b² = 1
- Ecrire une fonction qui trace en 2D une ellipse à partir de a et e (Gabriel)
- Ecrire une fonction qui, à un ensemble de points, lui applique une rotation d'un certain angle donné par rapport à un axe quelconque (Eliott)
- Rassembler toutes les fonctions précédentes pour pouvoir exploiter la base de données (Gabriel et Quentin)
- Représenter les ellipses dans un graphe 3D matplotlib, avec l'étoile au centre (Enzo)
- Rendre le graphique interactif (Enzo et Gabriel)
- Peut-être faire changer la couleur des points en fonction de la couleur de la planète ?


**Réalisation : programme qui prend un nom d'étoile et qui renvoie, si possible, la représentation spatiale du système stellaire correspondant**

Il suffit d'appeler la fonction `trace_system`, du fichier `final` sur un nom d'étoile.
Essayer avec `'nu Oph'`, `'WASP-47'`, `'TOI-700'`, `'TOI-270'` ou encore (et surtout) `'TOI-1136'` pour des résultats satisfaisants.
