class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, oname, name, max_speed, mileage):
        Vehicle.__init__(self, name, max_speed, mileage)
        self.__oname = oname

    def get_owner(self):
        print(self.__oname)


b = Bus(*input().split())
b.get_owner()
print(f"{b.name}\n{b.max_speed}\n{b.mileage}")
