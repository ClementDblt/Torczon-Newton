# Projet d'algorithmique et complexité

Implémentation et application de la [méthode de torczon](https://ufrsciencestech.u-bourgogne.fr/master1/mi1-tc5/PROJETS_ALGO/UTILITIES/11b-sans-derivee.pdf) et de la [méthode de newton](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Newton) dans le but de déterminer des cercles tangent entre eux et à un triangle.

*Il peut arriver que l'exécution du programme bloque, dans ce cas il faut faire un keyboard interrupt et le relancer.*

## Installation
Ce programme nécessite la version 3.9.6 ou supérieur de python ainsi que matplotlib.

- pip install -r requirements.txt

Usage : py main.py display "nombre d'itérations"

## Exemples :
- py main.py                &nbsp;&nbsp;&nbsp;Effectue une itération, l'affichage est activé
- py main.py True           &nbsp;&nbsp;&nbsp;Effectue une itération, l'affichage est activé
- py main.py True 10        &nbsp;&nbsp;&nbsp;Effectue 10 itérations, l'affichage est activé
- py main.py False          &nbsp;&nbsp;&nbsp;Effectue une itérations, l'affichage est désactivé
- py main.py False 10       &nbsp;&nbsp;&nbsp;Effectue 10 itération, l'affichage est désactivé 