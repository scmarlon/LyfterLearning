class Fly():
    def fly(self):
        print("I can fly")

class Sing():
    def sing(self):
        print("I can sing")

class Eat():
    def eat(self):
        print("I can eat")

class BlueBird(Fly, Sing, Eat):
    pass

class MorphoButterfly(Fly, Eat):
    pass

print("\nBlue bird:")
blue_bird = BlueBird()
blue_bird.fly()  # I can fly
blue_bird.sing()  # I can sing
blue_bird.eat()  # I can eat
print("________________\nMorpho butterfly:")
morpho_butterfly = MorphoButterfly()
morpho_butterfly.fly()  # I can fly
morpho_butterfly.eat()  # I can eat