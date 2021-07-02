from src.Pet import Pet


class Dog(Pet):
    def speak(self):
        print(f"{self.name} says woof")
