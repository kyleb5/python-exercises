import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 11))

numbers_1_to_10 = range(1, 11)

for number in numbers_1_to_10:
    # check if the number exists in the my_randoms list
    # if so, print(f'my_randoms list contains {number}')
    # else print(f'my_randoms list does not contain {number}')
    print(f'my_randoms list contains {number}')
    print(f'my_random list does not contain {number}')
