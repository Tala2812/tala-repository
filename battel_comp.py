import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и ведет к {damage} единиц потери здоровья.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден!")
                print(f"Победитель: {self.player.name}")
                break
            print(f"{self.computer.name} имеет {self.computer.health} здоровья.\n")

            # Ход компьютера
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} побежден!")
                print(f"Победитель: {self.computer.name}")
                break
            print(f"{self.player.name} имеет {self.player.health} здоровья.\n")

def main():
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()

if __name__ == "__main__":
    main()