from building import Building
from city import City

megalopolis = City("Nashville", "Kyle", 1995)
megalopolis.add_building(Building("Kyle", "395385th Street", 5))


for building in megalopolis.buildings:
    print(
        f"City Name: {megalopolis.name} Mayor: {megalopolis.mayor} Established: {megalopolis.established}")
    print(
        f"Building Name: {building.designer} Building Address: {building.address} Building Floor: {building.stories}")
