class Restaurant:

    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restoranas dirba")


pavadinimas, tipas = input().split(", ")
restoranas = Restaurant(pavadinimas,  tipas)
restoranas.describe_restaurant()
print(restoranas.restaurant_name)
print(restoranas.cuisine_type)
restoranas.open_restaurant()