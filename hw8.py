#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Homework8:
    def has_permutation_as_substring(self, str1, str2):
        if len(str1) > len(str2):
            return False

        # count letters we need
        need = [0] * 26
        for ch in str1:
            need[ord(ch) - 97] += 1

        # sliding window counts
        window = [0] * 26
        left = 0
        for right, ch in enumerate(str2):
            window[ord(ch) - 97] += 1

            # shrink window to size len(str1)
            if right - left + 1 > len(str1):
                window[ord(str2[left]) - 97] -= 1
                left += 1

            # check match
            if window == need:
                return True

        return False


# For testing your code uncomment below lines.
# l = Homework8()
# print(l.has_permutation_as_substring("absc", "eidbcaoo"))  # Expected output: False
# print(l.has_permutation_as_substring("prb", "cbrpm"))     # Expected output: True
# Comment or delete the above test code before submitting.
