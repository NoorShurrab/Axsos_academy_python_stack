# Animal Class Documentation
The Animal class is the Base Class (Parent) that defines the common attributes and behaviors for all animals

### Attributes
1. animal_name: The name of the specific animal.
2.  age: The age of the animal.
3. health_level: Initialized to 10. Represents the physical well-being.
4. happiness_level: Initialized to 10. Represents the emotional state.

### Methods
1. __init__(self, animal_name, age, health_level=10, happiness_level=10)
     -  Initializes the core attributes for any animal instance.

2.  display_info(self)
    - Prints a formatted summary of the animal's name, age, health, and happiness levels.

3.  feed(self)
    - Increases both health_level and happiness_level by 10. This is the default feeding logic that can be overridden by subclasses.

## Zoo Class Documentation
### Attributes
1. zoo_name: The name of the zoo
2.animals: A list that stores animal objects (instances of Animal, Lion, Monkey, or Bear).

### Methods
1. __init__(self, zoo_name)
    - Initializes the zoo with a name and an empty list to hold animal instances.

2. add_animal(self, animal)
    - Receives an animal object as an argument.
    - Adds (appends) the animal to the self.animals list.
    - Prints a confirmation message including the animal's name.

3. display_all_animals(self)
    - Iterates through the self.animals list.
    - Calls the display_info() method for each animal object to show its current stats.

4. feed_all_animals(self)
    - Loops through all animals in the list.
    - Triggers the specific feed() method for each animal (demonstrating Polymorphism).
    - Updates health, happiness, and other specific levels for every animal in the collection.