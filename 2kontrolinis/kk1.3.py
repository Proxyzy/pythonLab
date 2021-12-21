class User:
    total_users = 0

    def __init__(self, f_name, l_name, b_year):
        self.first_name = f_name
        self.last_name = l_name
        self.birth_year = b_year
        User.total_users += 1

    def information(self):
        return "Name: " + self.first_name + " " + self.last_name + ", Birth year: " + self.birth_year

    @classmethod
    def from_string(cls, text):
        return User(*text.split())

    def __del__(self):
        User.total_users -= 1


users = {}
n = int(input())
for i in range(n):
    command, text = input().split(": ")
    if command == "Create":
        users[User.total_users] = User.from_string(text)
for key, val in users.items():
    print(f"ID: {key}, {val.information()}")
print(User.total_users)
