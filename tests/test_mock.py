from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_and_get_trainer():
    newId = len(client.get("/trainers").json())
    response = client.post("/trainers/", json={"name": "Abderwan", "birthdate": "2002-06-10"})
    assert response.status_code == 200
    assert response.json() == {"name": "Abderwan", "birthdate": "2002-06-10", "id": newId, "inventory": [], "pokemons": []}

def test_create_and_get_pokemon_(mocker):
    newId = len(client.get("/pokemons").json())
    mocker.patch("app.utils.pokeapi.get_pokemon_data", return_value={"name": "ivysaur", "id": 2})
    response = client.post("/trainers/2/pokemon/", json={"api_id": 2, "custom_name": "Bulbi"})
    assert response.status_code == 200
    assert response.json() == {"api_id": 2, "custom_name": "Bulbi", "id": newId, "name": "ivysaur", "trainer_id": 2}

def test_pokemon_fight(mocker):
    mocker.patch("app.utils.pokeapi.battle_compare_stats", return_value=1)
    response = client.get("/pokemons/fight/1/2")
    assert response.status_code == 200
    assert response.json() == {"Pokemon gagnant": "Bulbasaur"}

def test_pokemon_draw(mocker):
    mocker.patch("app.utils.pokeapi.battle_compare_stats", return_value=0)
    response = client.get("/pokemons/fight/1/1")
    assert response.status_code == 200
    assert response.json() == ["Égalité"]

def test_api_alive(mocker):
    alive = mocker.patch("app.utils.pokeapi.get_pokemon_name", return_value="Bulbasaur")
    assert alive.return_value == "Bulbasaur"