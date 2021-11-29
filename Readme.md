# Projet Info3A

Il peut arriver que l'exécution du programme bloque, dans ce cas il faut faire un keyboard interrupt et le relancer.

Il est nécessaire d'avoir la dernière version de Python installée, le programme peut ne pas fonctionner sinon.
Le programme nécessite d'avoir mathplotlib d'installé, voir la partie "Installation".

## Installation
- pip install -r requirements.txt

Usage : py main.py display "nombre d'itérations"

## Exemples :
- py main.py                &nbsp;&nbsp;&nbsp;Effectue une itération, l'affichage est activé
- py main.py True           &nbsp;&nbsp;&nbsp;Effectue une itération, l'affichage est activé
- py main.py True 10        &nbsp;&nbsp;&nbsp;Effectue 10 itérations, l'affichage est activé
- py main.py False          &nbsp;&nbsp;&nbsp;Effectue une itérations, l'affichage est désactivé
- py main.py False 10       &nbsp;&nbsp;&nbsp;Effectue 10 itération, l'affichage est désactivé