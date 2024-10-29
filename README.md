# pe-hackathon


**OBJECTIF : Représenter, pour une étoile donnée, les trajectoires des planètes autour**

Todo : 
- Rassembler les planètes par leur étoile, et qui n'ont qu'une étoile, les trier pour savoir si elles sont correctes (Quentin)
- Trouver les orbites des planètes autour de leur astre (Gabriel et Eliott)
    Relation entre excentricité e, et demi-grand axe a :
    b = a*sqrt(1-e²)
    l'ellipse vérifie alors x²/a² + y²/b² = 1
- Représenter les ellipses dans un graphe 3D matplotlib, avec l'étoile au centre (Enzo)
- Peut-être faire changer la couleur des points en fonction des raies spectrales ?


**Réalisation : programme qui prend un nom d'étoile et qui renvoie, si possible, la représentation spatiale du système stellaire correspondant**

Il suffit d'appeler la fonction `trace_system`, du fichier `final` sur un nom d'étoile.
Essayer avec `'nu Oph'`, `'WASP-47'`, `'TOI-700'`, `'TOI-270'` ou encore (et surtout) `'TOI-1136'` pour des résultats satisfaisants.
