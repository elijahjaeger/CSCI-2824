#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class LocalMinima: 
    def find_local_minima(self, array, left, right):
        '''
        array - Takes a list of integers
        left - Start index of the list
        right - End index of the list
        '''
        if left == right:
            return left
        mid = (left + right) // 2
        left_val = array[mid - 1] if mid > left else float('inf')
        right_val = array[mid + 1] if mid < right else float('inf')
        if array[mid] <= left_val and array[mid] <= right_val:
            return mid
        if mid > left and array[mid] > left_val:
            return self.find_local_minima(array, left, mid - 1)
        return self.find_local_minima(array, mid + 1, right)
        
# For testing your code uncomment below lines.
# m = LocalMinima()
# print(m.find_local_minima([3, 1, 2, 3], 0, 3))
# Comment or delete the above test code before submitting.

