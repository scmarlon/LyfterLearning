from datetime import datetime, date

class User():
    #date of birth attribute
    date_of_birth:date
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    #property decorator to get the age of the user
    @property
    def age(self):
        # Implementation for calculating age based on date_of_birth
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

def validate_age(func):
    def wrapper(user, *args):
        if user.age < 18:
            raise ValueError("The user is not old enough.\n")
        return func(user, *args)
    return wrapper

#example

#decorator for validating age before accessing a restricted area
@validate_age
def access_restricted_area(user):
    print("Access granted to the restricted area.")

user1 = User(date_of_birth=date(2011, 5, 15)) 
print(f"User's age: {user1.age}")  # This will print the user's age

try:
    access_restricted_area(user1)
except ValueError as e:
    print(e)  # This will raise a ValueError since the user is under 18

user2 = User(date_of_birth=date(2007, 8, 10))
print(f"User's age: {user2.age}")  # This will print the user's

try:
    access_restricted_area(user2)
except ValueError as e:
    print(e)  # This will not raise an error since the user is over 18

