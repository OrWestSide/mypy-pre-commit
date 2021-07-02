from src.Cat import Cat
from src.Dog import Dog
from src.PetFactory import PetFactory


if __name__ == "__main__":
    cat_shop = PetFactory(Cat)
    my_cat = cat_shop.get_pet("Tonia")
    my_cat.speak()

    dog_shop = PetFactory(Dog)
    my_dog = dog_shop.get_pet("Shelby")
    my_dog.speak()
