from src.Pet import Pet


class Cat(Pet):
    def speak(self):
        print(f"{self.name} says meow")
