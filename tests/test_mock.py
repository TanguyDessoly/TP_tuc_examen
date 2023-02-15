"""Test the mock of the pokeapi."""
# pylint: disable=E0401
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_and_get_trainer():
    """Test the creation of a trainer and the get of this trainer."""
    new_id = len(client.get("/trainers").json())
    response = client.post("/trainers/", json={"name": "Abderwan", "birthdate": "2002-06-10"})
    assert response.status_code == 200
    assert response.json() == {"name": "Abderwan",
    "birthdate": "2002-06-10",
    "id": new_id,
    "inventory": [],
    "pokemons": []}

def test_create_and_get_pokemon_(mocker):
    """Test the creation of a pokemon and the get of this pokemon."""
    new_id = len(client.get("/pokemons").json())
    mocker.patch("app.utils.pokeapi.get_pokemon_data", return_value={"name": "ivysaur", "id": 2})
    response = client.post("/trainers/2/pokemon/", json={"api_id": 2, "custom_name": "Bulbi"})
    assert response.status_code == 200
    assert response.json() == {"api_id": 2,
    "custom_name": "Bulbi",
    "id": new_id,
    "name": "ivysaur",
    "trainer_id": 2}

def test_pokemon_fight(mocker):
    """Test the fight between two pokemons."""
    mocker.patch("app.utils.pokeapi.battle_compare_stats", return_value=1)
    response = client.get("/pokemons/fight/1/2")
    assert response.status_code == 200
    assert response.json() == {"Pokemon gagnant": "Bulbasaur"}

def test_pokemon_draw(mocker):
    """Test the draw between two pokemons."""
    mocker.patch("app.utils.pokeapi.battle_compare_stats", return_value=0)
    response = client.get("/pokemons/fight/1/1")
    assert response.status_code == 200
    assert response.json() == ["Égalité"]

def test_api_alive(mocker):
    """Test the pokeapi is alive."""
    alive = mocker.patch("app.utils.pokeapi.get_pokemon_name", return_value="Bulbasaur")
    assert alive.return_value == "Bulbasaur"
