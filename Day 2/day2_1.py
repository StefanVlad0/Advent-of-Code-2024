# Author: Vlad Stefan

# Problem 1:
# Input: A text file with lines of space-separated integers.
# Output: The count of lines where integers are strictly increasing or decreasing, with consecutive differences <= 3.


safe_reports = 0

try:
    with open("input.txt", "r") as file:
        for line in file:
            values = list(map(int, line.strip().split()))
            if (
                all(values[i] < values[i + 1] and abs(values[i] - values[i + 1]) <= 3 for i in range(len(values) - 1)) or
                all(values[i] > values[i + 1] and abs(values[i] - values[i + 1]) <= 3 for i in range(len(values) - 1))
            ):
                safe_reports += 1
except FileNotFoundError:
    print("File not found!")
    exit()

print(safe_reports)
