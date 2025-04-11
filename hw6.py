#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Homework6:
    def isPowerOf(self, num, base):
        if num == 1:
            return True
        if num % base != 0:
            return False
        return self.isPowerOf(num // base, base)

# For testing your code uncomment below lines.
# l = Homework6()
# print(l.isPowerOf(81,3))
# Comment or delete the above test code before submitting.
