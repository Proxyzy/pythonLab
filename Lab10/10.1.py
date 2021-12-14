class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

name, max_speed, mileage = input().split()
b = Bus(name, max_speed, mileage)
print(f"{b.name}\n{b.max_speed}\n{b.mileage}")