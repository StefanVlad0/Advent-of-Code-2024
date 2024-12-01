# Author: Vlad Stefan

# Problem 1: Absolute Differences
# Input: A file containing 2 columns of integers.
# Output: The sum of absolute differences between the two sorted columns.

left_column = []
right_column = []

try:
    with open("input.txt", "r") as file:
        for line in file:
            values = line.strip().split()
            if len(values) == 2:
                try:
                    left_column.append(int(values[0]))
                    right_column.append(int(values[1]))
                except ValueError:
                    print("Location IDs must be numbers")
                    exit()
except FileNotFoundError:
    print("File not found!")
    exit()

left_column.sort()
right_column.sort()

sum_diff = sum(abs(a - b) for a, b in zip(left_column, right_column))

print(sum_diff)
