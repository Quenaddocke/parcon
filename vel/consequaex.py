class Quantity:
    apple = 1
    orange = 2
    grapes = 2
    
    def __index__(self):
        return self.apple + self.orange + self.grapes

quantity = Quantity()
binary = bin(quantity)
print(binary)  # Output: 0b101
