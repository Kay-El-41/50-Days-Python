class Car:
    def __init__(self, model, color, year, trans, electric):
        self.model = model
        self.Color = color
        self.Year = year
        self.Transmission = trans
        self.Electric = electric

    def print_car(self):
        print(f"car_model = {self.model}")
        print(f"Color = {self.Color}")
        print(f"Year = {self.Year}")
        print(f"Transmission = {self.Transmission}")
        print(f"Electric = {self.Electric}")


class BMW(Car):
    def __init__(self, model, color, year, trans, electric):
        Car.__init__(self, model, color, year, trans, electric)


bmw1 = BMW('x6', 'silver', 2018, 'Auto', False)
tesla1 = Car('S', 'beige', 2017, 'Auto', True)
ford1 = Car('focus', 'white', 2020, 'Auto', False)

bmw1.print_car()
# tesla1.print_car()
# ford1.print_car()