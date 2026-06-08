# Head Class
class Head:
    def __init__(self):
        pass

    def __str__(self):
        return "This is Head"

# Torso Class
class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg

#Arm Class
class Arm:
    def __init__(self, hand):
        self.hand = hand
    
    def __str__(self):
        return "This is Arm with " + str(self.hand)

#Hand Class
class Hand:
    def __init__(self):
        pass
    def __str__(self):
        return "This is Hand"

#Leg Class
class Leg:
    def __init__(self, feet):
        self.feet = feet

    def __str__(self):
        return "This is Leg with " + str(self.feet)

#Feet Class
class Feet:
    def __init__(self):
        pass
    def __str__(self):
        return "This is Feet"

# Human Class
class Human:
    def __init__(self):
        self.head = Head()
        self.right_hand = Hand()
        self.left_hand = Hand()

        self.right_arm = Arm(self.right_hand)
        self.left_arm = Arm(self.left_hand)
        self.right_feet = Feet()
        self.left_feet = Feet()
        self.right_leg = Leg(self.right_feet)
        self.left_leg = Leg(self.left_feet)
        self.torso = Torso(self.head, self.left_arm, self.right_arm, self.left_leg, self.right_leg)

    def introduce(self):
        print(f"Hello, I am a human.{self.torso.left_arm}")

# Create instances of body parts
human = Human()

print(human.torso.left_arm)

introduce = human.introduce()