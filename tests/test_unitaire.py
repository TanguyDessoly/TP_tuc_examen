from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_remi():
    response = client.get("trainers/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Rémi", "birthdate": "2002-06-20", "id":1, "inventory": [{'description': 'Permet de soigner un pokemon à la hauteur de 50% de ses PV', 'id': 1, 'name': 'Potion de vie', 'trainer_id': 1}], 'pokemons': [{'api_id': 2, 'custom_name': 'Eve', 'id': 1, 'name': 'Ivysaur', "trainer_id": 1}, {'api_id': 2, 'custom_name': 'Venus', 'id': 2, 'name': 'Venusaur', "trainer_id": 1}]}

def test_random_is_three():
    response = client.get("/pokemons/random/")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json()[0] == {"name": "Potion de vie", "description": "Permet de soigner un pokemon à la hauteur de 50% de ses PV", "id": 0, "trainer_id": 0}

def test_get_pokemons():
    response = client.get("/pokemons")
    assert response.status_code == 200
    assert response.json()[0] == {"api_id": 1, "custom_name": "Balba", "id": 0, "name": "Balbusaur", "trainer_id": 0}

def test_fight():
    response = client.get("/pokemons/fight/1/2")
    assert response.status_code == 200
    assert response.json() == {"Pokemon gagnant": "Ivysaur"}

def test_draw():
    response = client.get("/pokemons/fight/2/2")
    assert response.status_code == 200
    assert response.json() == ["Égalité"]