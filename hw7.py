class Passcodes:
    def count_passcodes(self, string):
        # Convert the string to a set of unique letters
        unique_letters = set(string)
        # The number of distinct passcodes of length 4 is the
        # number of unique letters raised to the power of 4
        return len(unique_letters) ** 4