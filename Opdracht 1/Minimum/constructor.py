class Cat:
    hungry = True
    lives = 9
    meowInterval = 5
    speed = 2

    def __init__(self, snelheid):
        self.speed = snelheid

    def meowSpeed(self):
        print("Meowing!")
        print("Meow interval is: ", self.meowInterval)

felix = Cat()
felix.meowSpeed()
print(felix.lives)