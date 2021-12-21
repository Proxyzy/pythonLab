class User:
    def __init__(self, f_name, l_name, b_year):
        self.first_name = f_name
        self.last_name = l_name
        self.birth_year = b_year

    def information(self):
        return "Name: " + self.first_name + " " + self.last_name + ", Birth year: " + self.birth_year

users = []
n = int(input())
for i in range(n):
    users.append(User(*input().split()))
for i in range(n):
    print(users[i].information())