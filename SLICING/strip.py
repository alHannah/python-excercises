numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(numbers[0:5])  # returns 1, 2, 3, 4, 5
print(numbers[1:])  # returns 2, 3, 4, 5, 6, 7, 8, 9, 0
print(numbers[:1])  # returns 1
print(numbers[0::5])  # returns [1, 6]
print(numbers[1::])  # returns [2, 3, 4, 5, 6, 7, 8, 9, 0]
print(numbers[::1])  # returns [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


# start:stop:step

# Example with three parts
print(numbers[1:8:2])  # Output: [2, 4, 6, 8]

# Example with two parts (step defaulting to 1)
print(numbers[2:7])  # Output: [3, 4, 5, 6, 7]

# Example with step only (start and stop defaulting to beginning and end of the list)
print(numbers[::3])  # Output: [1, 4, 7, 0]