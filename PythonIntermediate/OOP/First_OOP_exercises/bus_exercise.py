# Create a Bus class that has a maximum capacity of passengers.
class Bus:
    max_passengers = 3
    passenger_list = []

    #Method to add a passenger to the bus,checking if the maximum capacity has been reached before adding.
    def add_passenger(self, Person): # Person is an instance of the Person class
        if len(self.passenger_list) < self.max_passengers:
            self.passenger_list.append(Person)
            print(f"\n{Person.name} has been added to the bus.")
        else:
            print(f"Cannot add {Person.name} passenger. Maximum capacity exceeded.\n")
    
    #Method to remove a passenger from the bus, checking if the passenger is on the bus before removing.
    def remove_passenger(self, Person):
        if Person in self.passenger_list:
            self.passenger_list.remove(Person)
            print(f"\n{Person.name} has been removed from the bus.")
        else:
            print(f"\n{Person.name} is not on the bus.")

# Create a Person class that has a name attribute.
class Person:
    def __init__(self, name):
        self.name = name

person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Charlie")
person4 = Person("David")

bus = Bus()
bus.add_passenger(person1)
bus.add_passenger(person2)
bus.add_passenger(person3)
bus.add_passenger(person4)

bus.remove_passenger(person3)
bus.remove_passenger(person1)
bus.remove_passenger(person2)
bus.remove_passenger(person4)