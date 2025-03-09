import random
0
class Robot:

    def __init__(self, Name: str, HP: int, ATK: int):
        self.Name = Name
        self.HP = HP
        self.ATK = ATK

    def attack(self, other: 'Robot') -> None:
        other.HP -= self.ATK
        print(f"{self.Name} menyerang {other.Name} dengan {self.ATK} ATK")

    def status(self) -> None:
        print(f"{self.Name} - HP: {self.HP}, ATK: {self.ATK}")

class game:

    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.ronde = 0
    
    def mulai_Game_n_lanjut(self):
        self.ronde += 1
        print(f"\n--- ronde {self.ronde} ---")


if __name__ == "__main__":
    robot1 = Robot("Robot 1", 100, 20)
    robot2 = Robot("Robot 2", 120, 15)

    game = game(robot1, robot2)

    while robot1.HP > 0 and robot2.HP > 0:
        game.mulai_Game_n_lanjut()
        robot1.status()
        robot2.status()

        action = {
            "1":"attack",
            "2":"defend"
            }

        print("\nGiliran robot 1:")
        action = input("Apa yang ingin dilakukan? (attack:1/defend:2): ")
        if action.lower() == "1":
            robot1.attack(robot2)
        elif action.lower() == "2":
            print("Robot 1 bertahan.")
        else:
            print("Aksi tidak valid.")

        if robot2.HP > 0:
            print("\nGiliran robot 2:")
            action = input("Apa yang ingin dilakukan? (attack:1/defend:2): ")
            if action.lower() == "1":
                robot2.attack(robot1)
            elif action.lower() == "2":
                print("Robot 2 bertahan.")
            else:
                print("Aksi tidak valid.")

    # Print the game result
    if robot1.HP > 0:
        print(f"{robot1.Name} wins!")
    else:
        print(f"{robot2.Name} wins!")

