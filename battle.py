from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "Богатырь наносит удар мечом."

    def get_name(self):
        return "меч"


class Bow(Weapon):
    def attack(self):
        return "Богатырь стреляет из лука."

    def get_name(self):
        return "лук"


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.get_name()}.")

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())
        else:
            print(f"{self.name} не вооружен!")


class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"{self.name} побежден!")


# Реализация боя
def battle(fighter: Fighter, monster: Monster):
    fighter.attack()
    monster.defeat()


# Демонстрация работы программы
if __name__ == "__main__":

    fighter = Fighter("Богатырь")
    monster = Monster("Соловей-разбойник")

    sword = Sword()
    fighter.change_weapon(sword)
    battle(fighter, monster)

   
    bow = Bow()
    fighter.change_weapon(bow)
    battle(fighter, monster)