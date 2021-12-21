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

    @staticmethod
    def default_user_data():
        return "User1 User2 1900"


users = {}
id_counter = 0
n = int(input())
for i in range(n):
    input_string = input()
    if input_string == "Default user":
        id_counter += 1
        users[id_counter] = User.from_string(User.default_user_data())
    else:
        command, text = input_string.split(": ")
        if command == "Create":
            id_counter += 1
            users[id_counter] = User.from_string(text)
        elif command == "Delete":
            del users[int(text)]
for key, val in users.items():
    print(f"ID: {key}, {val.information()}")
print(User.total_users)