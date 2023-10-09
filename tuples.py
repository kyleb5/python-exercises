zoo = (
    "lion",
    "tiger",
    "elephant",
    "giraffe",
    "panda",
    "koala",
    "dolphin",
    "cheetah",
    "red panda",
    "penguin"
)

# (first_child, second_child, third_child, fourth_child) = children

for animals in zoo:
    (first_animal, second_animal, third_animal, fourth_animal, fifth_animal,
     sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo

    print(animals)

animal_to_find = "elephant"
if animal_to_find in zoo:
    print(f'Found in')

print(zoo.index("giraffe"))
