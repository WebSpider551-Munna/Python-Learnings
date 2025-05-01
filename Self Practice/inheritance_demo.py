# Base class
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {self.name}")

    def speak(self):
        print(f"{self.name} makes a sound.")

    def eat(self):
        print(f"{self.name} is eating.")

# Derived class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the __init__ method of the base class (Animal)
        super().__init__(name)
        self.breed = breed
        print(f"Dog created: {self.name}, Breed: {self.breed}")

    # Override the speak method from the base class
    def speak(self):
        print(f"{self.name} barks.")

    # Add a new method specific to Dog
    def fetch(self):
        print(f"{self.name} is fetching the ball.")

# --- Demonstration ---

# Create an instance of the derived class (Dog)
my_dog = Dog("Buddy", "Golden Retriever")
print("-" * 20)

# Call methods from the base class (Animal)
my_dog.eat()
print("-" * 20)

# Call the overridden method from the derived class (Dog)
my_dog.speak()
print("-" * 20)

# Call a method specific to the derived class (Dog)
my_dog.fetch()
print("-" * 20)

# Demonstrate polymorphism with a generic Animal instance
generic_animal = Animal("Generic Creature")
generic_animal.speak()
generic_animal.eat()
