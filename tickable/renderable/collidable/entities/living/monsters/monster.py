import random

from pygame import Vector2

from tickable.renderable.collidable.entities.living.living_entity import LivingEntity
from tickable.renderable.collidable.entities.living.players.player import get_players

class Monster(LivingEntity):
    attack_interval = 1.0

    def __init__(self, position: tuple[int, int], monster: str, size: int, health: int, game: "Game"):
        super().__init__(position, "monsters/" + monster, size, health, game)
        self.attack_timer = 0
        self.game = game

    def tick(self):
        super().tick()
        self.ai_tick()

        self.attack_timer += self.game.dt

        if self.attack_timer >= self.attack_interval:
            self.attack_timer = 0
            self.attack()

    def ai_tick(self):
        pass

    def attack(self):
        players = list(filter(lambda p: self.sees_other(p), get_players()))
        player_count = len(players)

        if player_count == 0:
            return

        player = list(sorted(players, key=lambda p: self.position.distance_squared_to(p.position)))[0]
        self.attack_entity(player)
        pass

    def attack_entity(self, entity: LivingEntity):
        pass
