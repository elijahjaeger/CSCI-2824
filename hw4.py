#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Homework4:
    def largeCount(self, nums):
        result = []
        for x in nums:
            count = 0
            for y in nums:
                if y > x:
                    count += 1
            result.append(count)
        return result
        # Start your code from here

# For testing your code uncomment below lines.
# l = Homework4()
# print(l.largeCount([8,1,2,2,3]))
# Comment or delete the above test code before submitting.

