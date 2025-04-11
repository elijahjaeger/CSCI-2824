#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Power:
    def isPowerTwo(self, number):
        if ((number & number-1) == 0):
            return True
        else:
            return False
# For testing your code uncomment below lines.

p = Power()
print(p.isPowerTwo(4))
print(p.isPowerTwo(17))

# Comment or delete the above test code before submitting.