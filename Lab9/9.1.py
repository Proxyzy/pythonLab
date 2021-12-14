class Studentas:
    def __init__(self, vardas, pavarde, pazymiai):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pazymiai = pazymiai

    def stud_info(self):
        print(f"{sum(self.pazymiai)/len(self.pazymiai)}")

    def add_mark(self, pazimys):
        self.pazymiai.append(pazimys)

    def do_changes(self, marks):
        if marks != -1:
            self.add_mark(marks)
        else:
            self.stud_info()

    def paieska(self, vardas, pavarde):
        if(self.vardas == vardas and self.pavarde == pavarde):
            return(True)




studentai = list()
n = int(input())
for i in range(n):
    vardas, pavarde, pazymiai = input().split()
    pazymiai =  eval(pazymiai)
    studentai.append(Studentas(vardas, pavarde, pazymiai))

q = int(input())
for i in range(q):
    komanda, *argumentai = input().split()
    for i in range(n):
        if studentai[i].paieska(argumentai[0], argumentai[1]):
            if 2 >= len(argumentai):
                studentai[i].do_changes(-1)
            else:
                studentai[i].do_changes(int(argumentai[2]))