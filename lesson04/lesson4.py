# Lesson 4
fence1 = input("Enter number of planks for side 1 of your fence: ")
fence1 = len(fence1)
fence2 = input("Enter number of planks for side 2 of your fence: ")
fence2 = len(fence2)
fence3 = input("Enter number of planks for side 3 of your fence: ")
fence3 = len(fence3)

total = fence1 + fence2 + fence3
print(total)


if total <= 12:
    remainder = 12 - total
else: remainder = total % 12 
print(remainder)

import math
cost = 14.95 * math.ceil(total / 12)
print(cost)
    
