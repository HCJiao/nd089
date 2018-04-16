number = 0
square = 0
limit = 40
while square < limit:
    nearest_square = square
    number += 1
    square = number ** 2
print(nearest_square)