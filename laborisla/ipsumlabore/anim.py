class Instance:
    def __init__(self, data):
        self.data = data

def canMerge(instance1, instance2):
    if isinstance(instance1, Instance) and isinstance(instance2, Instance):
        return True
    else:
        return False

# Example usage
instance1 = Instance("data1")
instance2 = Instance("data2")
print(canMerge(instance1, instance2))  # Output: True
