class Animal:
    def __init__(self, animal_name, age, health_level = 10, happiness_level = 10):
        self.animal_name = animal_name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def display_info(self):
        print(f"Name: {self.animal_name}, Age: {self.age}, Health Level: {self.health_level}, Happiness Level: {self.happiness_level}")

    def feed(self):
        self.health_level += 10
        self.happiness_level += 10
    
class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.volume = 10 
    def feed(self):
        self.health_level += 10
        self.happiness_level += 20
        print(f"{self.animal_name} the Lion is happy!")

class Monkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.energy_level = 10
    def feed(self):
        self.health_level += 10
        self.happiness_level += 15
        self.energy_level += 5
        print(f"{self.animal_name} the Monkey is happy!")


class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sleepiness_level = 10
    def feed(self):
        self.health_level += 10
        self.happiness_level += 5
        self.sleepiness_level += 10
        print(f"{self.animal_name} the Bear is happy!")

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.animal_name} has been added to {self.zoo_name}.")
    def display_all_animals(self):
        print(f"Animals in {self.zoo_name}:")
        for animal in self.animals:
            animal.display_info()


dog = Zoo("City Zoo")
dog.add_animal(Animal("Dog", 5))
dog.display_all_animals()
