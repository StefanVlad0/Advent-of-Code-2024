# Author: Vlad Stefan

# Problem 2: Similarity Score
# Input: A file containing 2 columns of integers.
# Output: The similarity score, calculated as the sum of each number in the left column multiplied by its occurrence count in the right column.

from collections import Counter

left_count = []
right_count = []

try:
    with open("input.txt", "r") as file:
        for line in file:
            values = line.strip().split()
            if len(values) == 2:
                try:
                    left_count.append(int(values[0]))
                    right_count.append(int(values[1]))
                except ValueError:
                    print("Location IDs must be numbers")
                    exit()
except FileNotFoundError:
    print("File not found!")
    exit()

right_count = Counter(right_count)

similarity_score = sum(num * right_count[num] for num in left_count)

print(similarity_score)
