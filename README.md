## BARAN Rémi - DERHILLE Erwan - DESSOLY Tanguy - LABADIE Pierre 

Ce fork a pour but de réaliser le projet de fin de formation de la formation Python TEST de l'EPSI.

Nous avons implémenter un système de combat de pokémon en utilisant l'API de POKEAPI.

Le système de combat se base sur les statistiques des pokémons. Le pokémon qui a le plus de statistiques supérieures gagne le combat.

De plus, un endpoint listant 3 pokémons aléatoires a été implémenté.

Un locustfile a été créé pour tester le système d'insertion (utilisateur, pokemon et item) dans la base de données ainsi que des endpoints (combat).

Le locustconf simule la sortie du jeu avec 1000 utilisateurs sur une heure à la hauteur de 6 utilisateurs par secondes.

Nous avons améliorer le code en utilisant pylint afin de détecter les erreurs et les problèmes de code, en améliorant la documentation également.

Les tests ont un coverage de 95%.

Nous avons ajouté des tests unitaires et des tests unitaires mocks pour tester les fonctions de l'application.

### Mail contact professeur
yann.coornaert1@mail-formateur.net


### Lancement du projet
```python -m virtualenv venv```
```source venv/bin/activate ```
```pip install -r requirements.txt```
```uvicorn main:app --reload ```


### Coverage
```coverage run -m pytest --profile # remplace la commande python```
```coverage html # génère le rapport en html```

# Spécifications
Un fichier readme indiquant le groupe et décrivant ce qui a était réalisé, permettant de fournir des informations si nécessaires.

## Code
- [X] Création d'un endpoint qui permet de faire combattre 2 pokémons en fournissant leur ID.
- [X] Endpoint qui liste 3 pokémons aléatoires ( avec affichage des stats )

## Locust
```locust --config=.locust.conf```
- [X] Rédaction d'un scénario ( pertinent )
- [X] Un exemple de test de performance à réaliser fourni via un .locust.conf.
![graph](graph.png)

## Pylint
```pylint application/ tests/```
- [ ] Note minimal de 8.5/10

## Pytest
```python -m pytest```
- [X] 7 tests unitaires
- [X] 5 tests unitaires mocks

## Coverage
- [X] 85% -> 95% ! 