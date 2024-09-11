class Quantity:
    def __init__(self, value = 0):
        self.value = value

    def __add__(self, other):
        return Quantity(self.value + other.value)

    def __sub__(self, other):
        return Quantity(self.value - other.value)

    def __mul__(self, other):
        return Quantity(self.value * other.value)

    def __pow__(self, other):
        return Quantity(self.value ** other.value)

    def __truediv__(self, other):
        return Quantity(self.value / other.value)

    def __floordiv__(self, other):
        return Quantity(self.value // other.value)

    def __mod__(self, other):
        return Quantity(self.value % other.value)

    def __str__(self):
        return f'Quantity[{str(self.value)}]'

