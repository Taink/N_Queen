# N_Queen
## À propos
C'est une implémentation en Python 3 du
[problème des huit dames](https://fr.wikipedia.org/wiki/Probl%C3%A8me_des_huit_dames).

## Installation
```shell
# Installation des dépendances
$ pip install -r requirements.txt
```

## Utilisation
Ce projet est avant tout à considérer dans une approche de développement dirigée par
les tests.  
À ce titre, les fichiers supportés sont des fichiers de test (via `pytest`).
```shell
# Lance tous les tests
$ pytest
```
> `pytest` cherchera tous les fichiers commençant par `test_` et exécutera tous les
> tests présents à l'intérieur.

## Notes
Un cycle de CI est normalement implémenté et permet de vérifier rapidement si la version
actuelle répond bien aux tests. La structure de ce cycle est dépendante des branches,
le projet étant subdivisé en 3 "sprints" correspondant aux jalons de notation du projet.  
Ce projet devrait respecter les normes indiquées par [gitmoji](https://gitmoji.dev/) pour
le nommage des commits.
