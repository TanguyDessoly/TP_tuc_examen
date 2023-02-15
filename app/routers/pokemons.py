from random import randint
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.utils import get_db
from ..utils.pokeapi import battle_pokemon, get_pokemon_data

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100000, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100000
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons

@router.get("/fight/{premierPokemon}/{secondPokemon}")
def pokemons_battle(premierPokemon: int, secondPokemon: int):
    """
        Return the winner of a fight between two pokemons
    """
    return battle_pokemon(premierPokemon, secondPokemon)


@router.get("/random")
def pokemons_random():
    """
        Return 3 random pokemons
    """
    pokemons: list[dict, dict, dict] = []
    while len(pokemons) != 3:
        pokemon = get_pokemon_data(randint(1, 1279))
        if pokemon not in pokemons and pokemon is not None:
            pokemons.append(pokemon)
    return pokemons