class Restaurant:

    def __init__(self):
        self.number_served = 0

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self):
        self.number_served = self.number_served + 1



x, n = input().split()
restoranas = Restaurant()
print(restoranas.number_served)
restoranas.set_number_served(int(x))
print(restoranas.number_served)
for i in range(int(n)):
    restoranas.increment_number_served()
print(restoranas.number_served)