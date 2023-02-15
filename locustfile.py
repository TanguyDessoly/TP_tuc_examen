from locust import HttpUser, task, between
from app import actions
from fastapi import Depends
from app.utils.utils import get_db
import random

class User(HttpUser):
    wait_time = between(1,3)

    created_trainer: int
    opponent_trainer: int = 0

    created_pokemon: int
    opponent_pokemon: int = random.randint(1, 100)
    
    @task
    def test_start(self):
    # Create a trainer*
        response = self.client.post("/trainers/", json={"name": "Abderwan", "birthdate": "2002-12-28"})
        self.created_trainer = response.json()["id"]

    @task
    def add_created_trainer_item(self):
        actions.add_trainer_item(Depends(get_db), {"name": "Potion", "quantity": 5}, self.created_trainer)
        
    @task
    def add_created_trainer_pokemon(self):
        response = self.client.post("/trainers/"+str(self.created_trainer)+"/pokemon/", json={"api_id": 1, "custom_name": "Boulebazar"})
        self.created_pokemon = response.json()["id"]

    @task
    def make_created_pokemon_fight(self):
        response = self.client.get("/pokemons/fight/"+str(self.created_pokemon)+"/"+str(self.opponent_pokemon)).json()


