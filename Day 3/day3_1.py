# Author: Vlad Stefan

# Problem 1
# Input: A string containing valid mul(X,Y) instructions (1-3 digit numbers) mixed with invalid patterns.
# Output: The sum of the results of all valid mul instructions.

total = 0

try:
    with open("input.txt", "r") as file:
        memory = file.read()
        tokens = memory.split("mul")
        for token in tokens[1:]:  # the first token can't be a valid mul
            if token.startswith("(") and ")" in token:
                try:
                    args = token[1:token.index(")")].split(",")
                    if len(args) == 2:  # one comma inside mul
                        if all(arg.isdigit() and 1 <= len(arg) <= 3 for arg in args):
                            x, y = int(args[0]), int(args[1])
                            total += x * y
                except ValueError:
                    continue
except FileNotFoundError:
    print("File not found!")
    exit()

print(total)
