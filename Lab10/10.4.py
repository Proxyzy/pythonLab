class Students:
    def __init__(self, sno):
        self.sno = int(sno)

    def __add__(self, other):
        return Students(self.sno + other.sno)

    def __str__(self):
        return f"Bendras studentu skaicius: {self.sno}"


groups = list(map(Students, input().split()))
look_for = int(input())
print(f"Studentu skaicius {look_for} grupeje: {groups[look_for-1].sno}")
print(groups[0]+groups[1]+groups[2]+groups[3])
