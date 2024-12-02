# Author: Vlad Stefan

# Problem 2:
# Input: A text file with lines of space-separated integers.
# Output: The number of lines that are either already safe (strictly increasing or decreasing with differences <=3) or can be made safe by removing exactly one value.

def is_safe(sequence):
    """Check if a sequence is safe (strictly increasing or decreasing with differences <= 3)."""
    return (
        all(sequence[i] < sequence[i + 1] and abs(sequence[i] - sequence[i + 1]) <= 3 for i in range(len(sequence) - 1)) or
        all(sequence[i] > sequence[i + 1] and abs(sequence[i] - sequence[i + 1]) <= 3 for i in range(len(sequence) - 1))
    )


safe_reports = 0

try:
    with open("input.txt", "r") as file:
        for line in file:
            values = list(map(int, line.strip().split()))
            if is_safe(values):
                safe_reports += 1
                continue
            for i in range(len(values)):
                modified_values = values[:i] + values[i + 1:]
                if is_safe(modified_values):
                    safe_reports += 1
                    break
except FileNotFoundError:
    print("File not found!")
    exit()

print(safe_reports)
