# python function
# Function and variable names are snake case instead of camel case
def create_person(first_name, last_name, age, occupation):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "occupation": occupation,
    }


melissa = create_person("Melissa", "Bell", 25, "Software Developer")


def list_person(**person):
    for key, value in person.items():
        print(f"{key} is {value}")


melissa = list_person(first_name="Melissa", last_name="Bell",
                      age=25, occupation="Software Developer")

# ChickenMonkey
# Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.
numbers = range(1, 101)
for num in numbers:
    print(num)
# For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number.
for num in numbers:
    if num % 5 == 0:
        print('Chicken')
    else:
        print(num)
# For the multiples of seven (7, 14, 21, etc.) print "Monkey".
for num in numbers:
    if num % 7 == 0:
        print('Money')
    else:
        print(num)
# For numbers which are multiples of both five and seven print "ChickenMonkey".
# To determine if a number can be evenly divided by 5 or 7, use the Python modulo operator.
for num in numbers:
    if num % 5 & num % 7 == 0:
        print('ChickenMonkey')
    else:
        print(num)

# Activities for Kids
# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take varying number of children's names as the argument.


def run(name):
    print(name, "is running")


def swing(name):
    print(name, "is swinging")


def slide(name):
    print(name, "is sliding")


def hide_and_seek(name):
    print(name, "is hiding")


# Running kids: Pam, Sam, Andrea, Will
run("Pam, Sam, Andrea, Will")
# Swinging kids: Marybeth, Ariel, Kevin, Courtney
swing("Marybeth, Ariel, Kevin, Courtney")
# Sliding kids: Mike, Jack, Jennifer, Earl
slide("Mike, Jack, Jennifer, Earl")
# Hiding kids: Henry, Heather, Hayley, Hugh
hide_and_seek("Henry, Heather, Hayley, Hugh")
