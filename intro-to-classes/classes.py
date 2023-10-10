class Pizza:
    def __init__(self):
        self.size = ""
        self.style = ""
        self.crust_type = ""
        self.toppings = ""

    def add_topping(self, topping):
        self.toppings += " " + topping
        print(f"You have added {topping}")

    def description(self):
        print(
            f'Description of your pizza - size: {self.size} crust type: {self.crust_type} toppings: {self.toppings}')


meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.add_topping("CHEESE")
meat_lovers.description()
