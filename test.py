import debugpy
# This program takes a value in a list, multiples the value by 2, and adds the product to a variable total.
numbers = [2, 4, 6, 8] # add a breakpoint to this line
def times_two(values): # add a breakpoint to this line
    total = 0
    for num in numbers:
        total += (num * 2)
    return total
print(times_two(numbers))