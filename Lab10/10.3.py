class Students:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def info(self):
        print(f"{self.fname} {self.lname}")


class Marks(Students):
    def __init__(self, fname, lname, *marks):
        Students.__init__(self, fname, lname)
        self.marks = marks

    def info(self):
        Students.info(self)
        print(*self.marks)


fname, lname = input().split()
marks = list(map(int, input().split()))
m = Marks(fname, lname, *marks)
m.info()