class Robot():
    def __init__(self,nom):
        self.nom = nom

    def marcheRobot(self,x,y):
        print(f"Je me déplace vers x = {x}, y = {y}")

    def communiquerRobot(self,parole):
        print(f"Bonjour je m appel{self.nom}")

    def reparationRobot(self):
        print(f"Reparation")

if __name__ == "__main__":
    robot1 = Robot(nom="A")
    robot2 = Robot(nom="B")
    print(robot1)
    print(robot2)