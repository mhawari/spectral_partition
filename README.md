# spectral_partition
Spectral Partition Algorithm

Une implémentation de l'algorithme de partition spectrale utilisant le laplacien.

Cette implementation a été vérifiée avec le réseau facebook_recombined de la base snap. Elle trouve deux communautés de 754 et 3285 membres. Elle tourne en 4s sur ce réseau grâce notamment à :
- l'emploi de matrices sparse (économie de mémoire)
- le calcul des 2 plus petites valeurs propres et non de toutes. Cela se fait car la matrice est symétrique, donc grâce à
