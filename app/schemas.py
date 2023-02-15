"""Schemas for the API."""
# pylint: disable=too-few-public-methods
from datetime import date
from typing import  List, Optional, Union
from pydantic import BaseModel

#
#  ITEM
#
class ItemBase(BaseModel):
    """Item schema."""
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    """Item schema for creation."""

class Item(ItemBase):
    """Item schema for response."""
    id: int
    trainer_id: int

    class Config:
        """Pydantic config."""
        orm_mode = True

#
#  POKEMON
#
class PokemonBase(BaseModel):
    """Pokemon schema."""
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase):
    """Pokemon schema for creation."""

class Pokemon(PokemonBase):
    """Pokemon schema for response."""
    id: int
    name: str
    trainer_id: int

    class Config:
        """Pydantic config."""
        orm_mode = True
#
#  TRAINER
#
class TrainerBase(BaseModel):
    """Trainer schema."""
    name: str
    birthdate: date

class TrainerCreate(TrainerBase):
    """Trainer schema for creation."""

class Trainer(TrainerBase):
    """Trainer schema for response."""
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config:
        """Pydantic config."""
        orm_mode = True
