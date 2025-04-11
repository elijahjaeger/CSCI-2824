#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Triangles:
    def isRightAngledTriangle(self, x1, y1, x2, y2, x3, y3):
        area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        if area == 0:
            return False
        side1 = (x2 - x1)**2 + (y2 - y1)**2
        side2 = (x3 - x2)**2 + (y3 - y2)**2
        side3 = (x1 - x3)**2 + (y1 - y3)**2

        sides = [side1, side2, side3]
        sides.sort()

        return sides[0] + sides[1] == sides[2]
# For testing your code uncomment below lines.

# t = Triangles()
# print(t.isRightAngledTriangle(0, 0, 3, 0, 0, 4))

# Comment or delete the above test code before submitting.