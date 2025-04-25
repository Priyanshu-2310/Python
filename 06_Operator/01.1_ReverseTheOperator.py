class ReverseMath:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value + other.value


a = ReverseMath(10)
b = ReverseMath(5)

print(a - b)
