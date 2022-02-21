# Shoot clash

![Lines of code](https://img.shields.io/tokei/lines/github/Pas-de-sushi/shoot-clash)
![GitHub](https://img.shields.io/github/license/Pas-de-sushi/shoot-clash)

Jeu de tir et de plateformes créé pour un projet scolaire.

## Installation
Le jeu utilise [Poetry](https://python-poetry.org/) pour la gestion des dépendances. Il est recommandé de l'installer, mais installer manuellement `pygame` devrait aussi fonctionner.

Pour démarrer le jeu, il faut lancer le fichier `run.py` à la racine.
```
$ poetry install && poetry shell  # Si vous utilisez Poetry, sinon `pip install pygame`
$ python run.py
```

## Instructions
Le personnage doit détruire tous les ennemis et se rendre sur la porte pour terminer la partie. Les ennemis apparaissent progressivement.

Le personnage se déplace avec les touches `Flèche gauche` et `Flèche droite`. Il peut sauter en appuyant sur `Flèche haut`. Pour tirer, il faut utiliser la touche `Espace` (on peut rester appuyé pour tirer en continu).

### Système de rechargement
Le jeu comporte un système de rechargement pour empêcher le joueur de tirer en continu. L'état du rechargement est affiché au dessus du joueur, sous la barre de vie.

La barre augmente lorsque le joueur tire. Tant qu'elle est blanche, le joueur peut tirer.

![image](https://user-images.githubusercontent.com/22115890/141473637-a6b8fd77-78e9-4149-9fc5-09f3eaa6d0a5.png)

Si la barre atteint sa taille maximale, elle devient rouge et le joueur doit attendre qu'elle diminue pour tirer à nouveau.

![image](https://user-images.githubusercontent.com/22115890/141473746-e1fb0793-3596-4b1b-89fe-cf4819ec5e59.png)

La barre de rechargement commence à descendre automatiquement après une seconde si on ne tire pas. Le temps pour qu'elle diminue entièrement dépend de l'arme choisie.

### Choix des armes
Le joueur peut choisir une arme au début de la partie avec les flèches de droite et de gauche du clavier. Chaque arme a des caractéristiques différentes :

![assault_riffle](assets/guns/assault_riffle.png) : Fusil à cadence rapide et dégats faibles

![pistol](assets/guns/pistol.png) : Pistolet à cadence lente et dégats élevés

## Capture d'écran du jeu
![image](https://user-images.githubusercontent.com/37936816/141463899-8e70fd70-e682-466b-8889-cbbe5ee141b1.png)

## Licence
Le jeu est disponible sous licence [ISC](LICENSE), ce qui signifie que vous pouvez le redistribuer librement. Consultez le dossier `/assets` pour les licences des images et sons utilisés.
