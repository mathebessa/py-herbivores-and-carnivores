from __future__ import annotations
from typing import List


class Animal:
    alive: List[Animal] = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        names = [animal.name for animal in Animal.alive]
        return f"Alive animals: {names}"

    def _die_check(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            self.health = 0
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            other._die_check()
