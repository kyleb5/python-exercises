from building import Building


class City:
    def __init__(self, name, mayor, established):
        self.name = name
        self.mayor = mayor
        self.established = established
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)
