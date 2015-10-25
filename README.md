# spectral_partition
Spectral Partition Algorithm

Une implémentation de l'algorithme de partition spectrale utilisant le laplacien.

Cette implementation a été vérifiée avec le réseau facebook_recombined de la base snap. Elle trouve deux communautés de 754 et 3285 membres. Elle tourne en 4s sur ce réseau grâce notamment à :
- l'emploi de matrices sparse (économie de mémoire)
- le calcul des 2 plus petites valeurs propres et non de toutes. Cela se fait car la matrice est symétrique, donc grâce à scipy.sparse.linalg.eigsh qui permet de choisir de prendre les k plus grandes (option which='LM') ou k plus petites (option which='SM') valeurs propres. Ici cependant, on emploi également l'option sigma = 0 qui réecrit le problème aux valeurs propres en termes de matrice inverse (pour des raisons de stabilité numérique), d'où l'utilisation de which='LM' (on prend les plus grandes valeurs propres de la matrice inverse, puis on les inverse).

Les résultats donnent une connectivité de 40.
