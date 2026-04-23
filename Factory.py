class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"


class AnimalFactory:
    def get_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal")


# Usage
factory = AnimalFactory()
animal = factory.get_animal("dog")
print(animal.speak())

cat = factory.get_animal("cat")
print(cat.speak())

#cow = factory.get_animal("cow")#ValueError