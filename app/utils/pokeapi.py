""" Pokeapi utils """
import requests

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']

def get_pokemon_stats(api_id):
    """
        Get pokemon stats from the API pokeapi
    """
    return get_pokemon_data(api_id)["stats"]

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    result = requests.get(f"{BASE_URL}/pokemon/{api_id}", timeout=10)
    if result.status_code > 199 and result.status_code < 300:
        return result.json()
    return None

def battle_pokemon(first_api_id, second_api_id) :
    """
        Do battle between 2 pokemons
    """
    premier_pokemon = get_pokemon_data(first_api_id)
    second_pokemon = get_pokemon_data(second_api_id)
    battle_result = 0
    if premier_pokemon and second_pokemon:
        battle_result = battle_compare_stats(premier_pokemon["stats"], second_pokemon["stats"])
        if battle_result > 0:
            return {"Pokemon gagnant":premier_pokemon["name"].capitalize()}
        if battle_result < 0:
            return {"Pokemon gagnant":second_pokemon["name"].capitalize()}
        return {"Égalité"}
    return None


def battle_compare_stats(premier_pokemon, second_pokemon):
    """
        Compare given stat between two pokemons
    """
    result = 0
    for i, stats in enumerate(premier_pokemon):
        result += stats["base_stat"] - second_pokemon[i]["base_stat"]
    return result
