class Dog:
    name = ""
    sound = ""

    def __init__(self, str, sound):
        self.name = str
        self.sound = sound

    #def make_sound(self):
        #print("Woof Woof")

    def movefast(self):
        print("Runs")

    def moveslow(self):
        print("Walks")

#originally wrote sound as a def but changed to the innit