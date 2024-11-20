

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} чирикает.")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} рычит.")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} шипит.")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

animals = [Bird("Воробей", 2), Mammal("Лев", 5), Reptile("Змея", 3)]
animal_sound(animals)

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []


    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлен {animal.name} в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Добавлен {staff_member.name} в качестве сотрудника зоопарка.")



class Staff:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Staff):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian(Staff):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

zoo = Zoo()
sparrow = Bird("Воробей", 2)
snake = Reptile("Змея", 1)

zoo.add_animal(sparrow)
zookeeper = ZooKeeper("Саша")
zoo.add_staff(zookeeper)

zoo.add_animal(snake)
veterinarian = Veterinarian("Света")
zoo.add_staff(veterinarian)


zookeeper.feed_animal(sparrow)
veterinarian.heal_animal(snake)

