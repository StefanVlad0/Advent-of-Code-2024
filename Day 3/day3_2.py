# Author: Vlad Stefan

# Problem 2
# Input: A string with mul(X,Y) instructions and do()/don't() statements that enable or disable future mul operations. Initially, mul is enabled.
# Output: The sum of results from valid and enabled mul instructions.

total = 0
is_enabled = True

try:
    with open("input.txt", "r") as file:
        memory = file.read()
        tokens = memory.split("mul")
        for token in tokens[1:]:
            if is_enabled and token.startswith("(") and ")" in token:
                try:
                    args = token[1:token.index(")")].split(",")
                    if len(args) == 2:  # one comma inside mul
                        if all(arg.isdigit() and 1 <= len(arg) <= 3 for arg in args):
                            x, y = int(args[0]), int(args[1])
                            total += x * y
                except ValueError:
                    continue
            if "do()" in token or "don't()" in token:
                if token.rfind("do()") > token.rfind("don't()"):
                    is_enabled = True
                else:
                    is_enabled = False
except FileNotFoundError:
    print("File not found!")
    exit()

print(total)
