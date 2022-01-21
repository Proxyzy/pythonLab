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


n = int(input())
pts = []
for i in range(n):
    pts.append(Point(*input().split()))
print(f"All points: ", end="")
print(*pts, sep=", ")
print(f"Bottom left point: {Point.bottom_left_pt}")
import pydoc

print(pydoc.render_doc(pts[0], renderer=pydoc.plaintext), dir(pts[0]))