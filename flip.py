import random
coinHead = random.randint(1,2)
if coinHead == 1:
    value = "Heads"
else:
    value = "Tails"
print("Your coin flip landed on:", value)