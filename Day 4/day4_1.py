# Author: Vlad Stefan

# Problem 1:
# Input: A file containing a matrix of letters
# Output: The number of occurrences of the 'XMAS' word, considering all directions (horizontal, vertical, diagonal)

input_matrix = []

try:
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            input_matrix.append(line)
except FileNotFoundError:
    print("File not found")
    exit()

target_word = 'XMAS'

rows = len(input_matrix)
cols = len(input_matrix[0])
target_length = len(target_word)

directions = [
    (1, 0),  # right
    (-1, 0),  # left
    (0, 1),  # up
    (0, -1),  # down
    (1, 1),  # up-right
    (-1, 1),  # up-left
    (1, -1),  # down-right
    (-1, -1),  # down-left
]

count = 0

for x in range(rows):
    for y in range(cols):
        for dx, dy in directions:
            okay = True

            for i in range(target_length):
                nx = x + i * dx
                ny = y + i * dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if input_matrix[nx][ny] != target_word[i]:
                        okay = False  # not the same letter
                        break
                else:
                    okay = False  # not inside the matrix
                    break

            if okay:
                count += 1

print(count)
