from __future__ import annotations
from typing import List


class AliveList(List["Animal"]):
    """Lista personalizada para armazenar animais vivos com __repr__ customizado."""

    def __repr__(self) -> str:
        """Retorna uma string legível de todos os animais vivos."""
        return "[" + ", ".join(repr(a) for a in self) + "]"


class Animal:
    """Classe base para todos os animais."""

    alive: AliveList = AliveList()

    def __init__(self, name: str, health: int = 100) -> None:
        """
        Inicializa um animal com nome e saúde.
        Adiciona o animal à lista Animal.alive.
        """
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        """Retorna uma representação legível do animal."""
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def _die_check(self) -> None:
        """
        Remove o animal de Animal.alive se a saúde for <= 0.
        Garante que health não seja negativo.
        """
        if self.health <= 0 and self in Animal.alive:
            self.health = 0
            Animal.alive.remove(self)


class Herbivore(Animal):
    """Animal herbívoro que pode se esconder para se proteger."""

    def hide(self) -> None:
        """Alterna o estado hidden do animal."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    """Animal carnívoro que pode atacar herbívoros."""

    def bite(self, other: Animal) -> None:
        """
        Ataca outro animal se for Herbivore e não estiver escondido.
        Não afeta outros Carnivores.
        """
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            other._die_check()
