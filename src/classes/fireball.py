from pygame import Vector2

from src.classes.entity import Entity

class Fireball(Entity):
    def __init__(self, target, screen, position, size):
        super().__init__(screen, position, "fireball", size)
        self.target = target

    def move(self):
        direction = Vector2(self.target) - self.position
        movement = direction.normalize() * 0.5
        self.move_without_collision(movement)
        pass

    def is_colliding(self, entity):
        from src.classes.skeleton import Skeleton
        if isinstance(entity, Skeleton) or isinstance(entity, Fireball):
            return False

        return super().is_colliding(entity)
