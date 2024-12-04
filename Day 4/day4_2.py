# Author: Vlad Stefan

# Problem 2:
# Input: A file containing a matrix of letters
# Output: The number of occurrences of the 'X-MAS', meaning two 'MAS' in the shape of an 'X'

input_matrix = []

try:
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            input_matrix.append(line)
except FileNotFoundError:
    print("File not found")
    exit()

rows = len(input_matrix)
cols = len(input_matrix[0])

up_left_x = -1
up_left_y = 1
down_right_x = 1
down_right_y = -1
up_right_x = 1
up_right_y = 1
down_left_x = -1
down_left_y = -1

count = 0

for x in range(1, rows - 1):
    for y in range(1, cols - 1):
        okay = True
        if input_matrix[x][y] == 'A':
            up_left = input_matrix[x + up_left_x][y + up_left_y]
            down_right = input_matrix[x + down_right_x][y + down_right_y]
            up_right = input_matrix[x + up_right_x][y + up_right_y]
            down_left = input_matrix[x + down_left_x][y + down_left_y]

            if up_left in "MS" and down_right in "MS" and up_left != down_right:
                if up_right in "MS" and down_left in "MS" and up_right != down_left:
                    count += 1

print(count)
