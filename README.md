---------------------------------------------------

# Instructions.

## Etape 1 :

Cloner le repository dans un fichier propre. \
(Utiliser un environnement au besoin)

`$ git clone [lien du repository)`

Charger les modules du fichier requirements.txt.

`$ pip install -r requirements.txt`

## Etape 2 :

Lancer le code

`$ python main.py`

Suivre les instructions affichées sur le terminal.

---------------------------------------------------

# Informations.

### IMPORTANT:

Etapes à suivre pour une bonne gestion du tournois : \
1 - Menu joueurs : créer les joueurs \
2 - Menu tournois : créer un tournois

Vous pourrez quitter un tournois qu'à sa création ou à la fin de chaque round.\
Pour y revenir, menu tournois -> tournois en cours. \
Si 1 seul tournois est en cours, le programme reprend automatiquement ce \
tournois.\
Si plusieurs sont en cours, vous pourrez choisir lequel reprendre.

### Sauvegarde, chargement des données :

La sauvegarde et le chargement des données se fait durant le code. \
Le programme re-créé une instance du tournois en cours choisi. \
Pas de fichier supplémentaire de sauvegarde.

### Création d'un rapport :

La création d'un rapport pour un joueur, une liste de joueur, un tournois ou \
une liste de tournois se réalise sous la forme d'un fichier .txt dans les sous \
dossiers correspondant ./data/... .

Les rapports d'une entité unique se nomment avec son nom (pour un tournois) \
et son ine (pour un joueur). Ex : AB12345.txt ou tournois_all_stars.txt

Les rapports d'une liste d'entités se nomment ainsi : \
-> tournois.txt et joueurs.txt

### Génération rapport html flake8 :

Un premier rapport est déjà édité et disponible dans le dossier flake_report. \
Pour générer un nouveau rapport, placez vous dans le dossier chess/ \
lancez cette ligne de commande :

`flake8 --format=html --htmldir=flake_report`

-----------------

#### Bon jeu, et que le meilleur gagne !
