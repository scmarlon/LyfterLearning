class Fly():
    def fly(self):
        print("I can fly")

class Sing():
    def sing(self):
        print("I can sing")

class eat():
    def eat(self):
        print("I can eat")

class Animal(Fly, Sing, eat):
    pass
print("Blue bird:")
blue_bird = Animal()
blue_bird.fly()  # I can fly
blue_bird.sing()  # I can sing
blue_bird.eat()  # I can eat
print("________________\nMorpho butterfly:")
morpho_butterfly = Animal()
morpho_butterfly.fly()  # I can fly
morpho_butterfly.eat()  # I can eat