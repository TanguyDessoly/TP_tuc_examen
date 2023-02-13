## BARAN Rémi - DERHILLE Erwan - DESSOLY Tanguy - LABADIE Pierre 

yann.coornaert1@mail-formateur.net

python -m virtualenv venv
source venv/bin/activate 
pip install -r requirements.txt
uvicorn main:app --reload 
locust --config=.locust.conf

Un fichier readme indiquant le groupe et décrivant ce qui a était réalisé, permettant de fournir des informations si nécessaires.

## Code
- [X] Création d'un endpoint qui permet de faire combattre 2 pokémons en fournissant leur ID.
- [X] Endpoint qui liste 3 pokémons aléatoires ( avec affichage des stats )

## Locust
- [ ] Rédaction d'un scénario ( pertinent )
- [ ] Un exemple de test de performance à réaliser fourni via un .locust.conf.

## Pylint
- [ ] Note minimal de 8.5/10

## Unittest
- [ ] 7 tests unitaires

- [ ] 5 tests unitaires mocks

## Coverage
- [ ] 85% 