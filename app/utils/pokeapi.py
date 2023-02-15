import requests

base_url = "https://pokeapi.co/api/v2"


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
    result = requests.get(f"{base_url}/pokemon/{api_id}", timeout=10)
    if result.status_code > 199 and result.status_code < 300:
        return result.json()
    return None

def battle_pokemon(first_api_id, second_api_id) :
    """
        Do battle between 2 pokemons
    """
    premierPokemon = get_pokemon_data(first_api_id)
    secondPokemon = get_pokemon_data(second_api_id)
    battle_result = 0    
    if premierPokemon and secondPokemon:
        battle_result = battle_compare_stats(premierPokemon["stats"], secondPokemon["stats"])
        if battle_result > 0:
            return {"Pokemon gagnant":premierPokemon["name"].capitalize()}
        if battle_result < 0:
            return {"Pokemon gagnant":secondPokemon["name"].capitalize()}
        else:
            return {"Égalité"}
    return None


def battle_compare_stats(premierPokemon, secondPokemon):
    """
        Compare given stat between two pokemons
    """
    result = 0
    for i, stats in enumerate(premierPokemon):
        result += stats["base_stat"] - secondPokemon[i]["base_stat"]
    return result