my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}

numbers = [1, 2, 3, 4, 5]

print([num * num for num in numbers])

for key, value in my_family.items():
    print(f'{value["name"]} is my {key} and is {value["age"]} years old')

{print(f'{value["name"]} is my {key} and is {value["age"]} years old')
 for key, value in my_family.items()}
