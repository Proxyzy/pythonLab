class Point:
    bottom_left_pt = None

    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)
        if Point.bottom_left_pt == None:
            Point.bottom_left_pt = self
        elif Point.bottom_left_pt.y > self.y:
            Point.bottom_left_pt = self
        elif Point.bottom_left_pt.y == self.y and Point.bottom_left_pt.x > self.x:
            Point.bottom_left_pt = self

    def __repr__(self):
        return f"(x = {self.x}, y = {self.y})"

    @classmethod
    def from_string(cls, text):
        t = text.split()
        return Point(int(t[2].replace(",", "")), int(t[5].replace(")", "")))

    @staticmethod
    def reset_btm_left():
        Point.bottom_left_pt = None


class InvisiblePoint(Point):
    def __init__(self, text):
        t = text.split()
        self.x = int(t[2].replace(",", ""))
        self.y = int(t[5].replace(")", ""))


n = int(input())
pts = []
for i in range(n):
    inp = input()
    if inp == "Reset bottom left":
        Point.reset_btm_left()
    else:
        command, text = inp.split(": ")
        if command == "Create":
            pts.append(Point.from_string(text))
        elif command == "Create invisible":
            pts.append(InvisiblePoint(text))
print(f"All points: ", end="")
print(*pts, sep=", ")
print(f"Bottom left point: {Point.bottom_left_pt}")
import pydoc

print(pydoc.render_doc(pts[0], renderer=pydoc.plaintext), dir(pts[0]))