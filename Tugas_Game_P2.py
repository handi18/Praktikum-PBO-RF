import random

class Robot:

    def __init__(self, Name: str, HP: int, ATK: int):
        self.Name = Name
        self.HP = HP
        self.ATK = ATK

    def attack(self, other: 'Robot') -> None:
        damage = self.ATK
        other.HP -= damage
        print(f"{self.Name} menyerang {other.Name} dengan {damage} ATK")

    def defend(self, other: "Robot") -> None:
        defend_chance = random.random()
        damage = other.ATK
        if defend_chance < 0.5:
            print(f"{self.Name} bertahan dari {other.Name} dengan sempurna (0 damage)")
        else:
            defend_damage = damage // 2
            print(f"{self.Name} Bertahan dari {other.Name} dengan damage ({defend_damage} dmg)")
            other.HP -= defend_damage  # ini salah, seharusnya mengurangi HP robot yang diserang, bukan robot yang menyerang

    def status(self) -> None:
        print(f"{self.Name} - HP: {self.HP}, ATK: {self.ATK}")


class Game:

    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.ronde = 0

    def mulai_Game_n_lanjut(self):
        self.ronde += 1
        print(f"\n--- ronde {self.ronde} ---")

    def play_game(self) -> None:
        while self.robot1.HP > 0 and self.robot2.HP > 0:
            self.mulai_Game_n_lanjut()
            self.robot1.status()
            self.robot2.status()
            print("\nGiliran robot 1:")
            action = input("Apa yang ingin dilakukan? (attack:1/defend:2): ")
            if action == "1":
                self.robot1.attack(self.robot2)
            elif action == "2":
                self.robot1.defend(self.robot2)
            self.robot1.status()
            self.robot2.status()
            if self.robot2.HP <= 0:
                print(f"{self.robot2.Name} telah dikalahkan!")
                break
            print("\nGiliran robot 2:")
            action = input("Apa yang ingin dilakukan? (attack:1/defend:2): ")
            if action == "1":
                self.robot2.attack(self.robot1)
            elif action == "2":
                self.robot2.defend(self.robot1)
            self.robot1.status()
            self.robot2.status()
            if self.robot1.HP <= 0:
                print(f"{self.robot1.Name} telah dikalahkan!")
                break


if __name__ == "__main__":
    robot1 = Robot("Robot 1", 100, 20)
    robot2 = Robot("Robot 2", 120, 15)

    game = Game(robot1, robot2)
    game.play_game()

    # Print the game result
    if robot1.HP > 0:
        print(f"{robot1.Name} menang!")
    else:
        print(f"{robot2.Name} menang!")
