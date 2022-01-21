class Point:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"(x = {self.x}, y = {self.y})"


n = int(input())
pts = []
for i in range(n):
    pts.append(Point(*input().split()))
print(pts)
import pydoc

print(pydoc.render_doc(pts[0], renderer=pydoc.plaintext), dir(pts[0]))