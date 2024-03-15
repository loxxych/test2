class ChairLeg:
    def __init__(self, size):
        self.length = size

    def __mul__(self, other):
        self.length = self.length * other
        return self

    def __rmul__(self, other):
        self.length = self.length * other
        return self

    def __mod__(self, other):
        return self.length % other


chl = ChairLeg(15)
chl * 3
print(chl.length)
2 * chl
print(chl.length)
print(chl % 7)