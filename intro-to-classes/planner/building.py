import datetime


class Building:
    def __init__(self, designer, address, stories):
        self.designer = designer
        self.address = address
        self.stories = stories

    def construct(self, date_constructed):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, owner):
        self.owner = owner


buildings = []

building1 = Building("Architect1", "123 Main Street", 5)
buildings.append(building1)

building2 = Building("Architect2", "1234 Main Street", 8)
buildings.append(building2)

building3 = Building("Architect3", "12345 Main Street", 21)
buildings.append(building3)

building4 = Building("Architect4", "12356 Main Street", 15)
buildings.append(building4)

building5 = Building("Architect5", "1234567 Main Street", 20)
buildings.append(building5)

purchase_date = datetime.datetime(2022, 5, 10)

building1.purchase("Real Estate Magnate1")
building1.construct(purchase_date)

building2.purchase("Real Estate Magnate2")
building2.construct(purchase_date)

building3.purchase("Real Estate Magnate3")
building3.construct(purchase_date)

building4.purchase("Real Estate Magnate4")
building4.construct(purchase_date)

building5.purchase("Real Estate Magnate5")
building5.construct(purchase_date)

for building in buildings:
    print(f"{building.address} was purchased by {building.owner} on {building.date_constructed.strftime('%m/%d/%Y')} and has {building.stories} stories.")
