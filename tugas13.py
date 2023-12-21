class Animal:
    def __init__(self, name, food, habitat, reproduction):
        self.name = name
        self.food = food
        self.habitat = habitat
        self.reproduction = reproduction

animal1 = Animal("Singa", "Daging", "Padang Rumput", "melahirkan")
animal2 = Animal("Elang", "Tikus", "Pegunungan", "Bertelur")


print(f"{animal1.name} hidup di {animal1.habitat} Memakan {animal1.food}. BerkembangBiak dengan cara {animal1.reproduction}.")

print(f"{animal2.name} hidup di {animal2.habitat} Memakan {animal2.food}. BerkembangBiak dengan cara {animal2.reproduction}.")

# NO 2
class Rhino(Animal):
    def __init__(self, name, habitat, horn_size=0):
        super().__init__(name, "Plants", habitat, "Vivipar")
        self.horn_size = horn_size

    def grow_horn(self, size):
        self.horn_size += size
        print(f"{self.name}'memiliki panjang tanduk {self.horn_size} inches.")

class Fish(Animal):
    def __init__(self, name, habitat, fins=2):
        super().__init__(name, "Plankton", habitat, "Ovipar")
        self.fins = fins

    def swim(self):
        print(f"{self.name} itu berenang.")

class Snake(Animal):
    def __init__(self, name, habitat, length=0):
        super().__init__(name, "Small animals", habitat, "Ovipar")
        self.length = length

    def grow(self, length):
        self.length += length
        print(f"{self.name}'dapat bertumbuh hingga {self.length} inches.")


rhino = Rhino("Badak", "Savannah")
rhino.grow_horn(10)

fish = Fish("Ikan", "Laut")
fish.swim()

snake = Snake("Ular", "Hutan")
snake.grow(20)