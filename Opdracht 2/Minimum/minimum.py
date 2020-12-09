#<--- Nario --->
class Mario:
    name = "Mario"
    color = "red"
    speed = 10
    jump = 8
    coins = 15
    savedPrincess = False

    def stats(self):
        print(self.name + "'s speed is " + str(self.speed) + " and jump is " + str(self.jump))

    def sayTheLine(self):
        print("It'sa me, " + self.name)

#<--- Luigi (inherit Mario)--->
class Luigi(Mario):
    item = "fireflower"
    score = 200

    def __init__(self):
        Mario.name = "Luigi"
        Mario.color = "green"
        Mario.speed = 8
        Mario.jump = 10
        print("Let'sa go!")

    def stats(self):
        print(self.name + "'s speed is " + str(self.speed) + ", jump is " + str(self.jump) + " and item is " + self.item)

    def sayTheLine(self):
        super().sayTheLine
        print(self.name + " number one!")

    def helping(self):
        print("Helping Mario!")

MarioP = Mario()

print("Mario")
MarioP.stats()
MarioP.sayTheLine()

LuigiP = Luigi()

print("Luigi")
LuigiP.stats()
LuigiP.sayTheLine()
LuigiP.helping()