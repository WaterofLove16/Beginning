class Search:
    def __init__(self, array):
        self.array = array

    def sequence(self, key):
        for i in range(len(self.array)):
            if self.array == key:
                return True
            else: return False

    def binary(self, key):

    