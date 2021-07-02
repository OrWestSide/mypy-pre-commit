from typing import Type

from src.Pet import Pet


class PetFactory:
    def __init__(self, constructor: Type[Pet]):
        self.constructor = constructor

    def get_pet(self, name: str):
        return self.constructor(name)
