class Calculator:

    def __init__(self):
        self.total = 0

    def add(self, num):
        self.total += num

    def subtract(self, num):
        self.total -= num

    def multiply(self, num):
        self.total *= num

    def divide(self, num):
        # TODO deal with the divide by zero problem
        self.total /= num

    def equals(self):
        return_value = self.total
        self.total = 0
        return return_value