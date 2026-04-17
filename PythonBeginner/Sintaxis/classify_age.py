# Exercise: Classify a person based on their age
name = input("Please enter your name: ")
lastname = input("Please enter your lastname: ")
age = int(input("Please enter your age: "))

if age <= 2:
    print(f"\n{name} {lastname} is a baby.")
elif age <= 10:
    print(f"\n{name} {lastname} is a child.")
elif age <=13:
    print(f"\n{name} {lastname} is a pre-teen.")
elif age <= 19:
    print(f"\n{name} {lastname} is a teenager.")
elif age <=30:
    print(f"\n{name} {lastname} is a young adult.")
elif age <= 65:
    print(f"\n{name} {lastname} is an adult.")
else:
    print(f"\n{name} {lastname} is an elder.")