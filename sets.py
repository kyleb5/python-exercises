# Using set() to create a set
languages = set()

# Using curly braces allows you to initialize the set with values
languages = {'english', 'mandarin chinese',
             'spanish', 'english', 'spanish', 'portugese'}
print(languages)

showroom = set()
new_cars = set()

showroom = {'350z', 'GT3RS', 'M3', 'F250'}
new_cars = {'M4', 'M5'}
print(showroom)
print(len(showroom))
showroom.add('F150')
print(showroom)
print(len(showroom))
showroom.update(new_cars)
print(showroom)
print(len(showroom))
showroom.remove('350z')
print(showroom)
print(len(showroom))
