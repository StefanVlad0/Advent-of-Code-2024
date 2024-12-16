# Author: Vlad Stefan

# Problem 1:
# Input: a file containing a guard (^), and obstacles (#). If an obstacle is directly in front of a guard, it rotates 90 degrees. Otherwise, it moves forward.
# Output The number of distinct blocks that guards visits until it left the grid.

# the matrix grid
grid = [
    list(line.strip()) for line in open('input.txt')
]


def move_guard(grid):
    rows, cols = len(grid), len(grid[0])

    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    symbols = ['^', '>', 'v', '<']
    guard_pos, guard_dir, guard_symbol = None, None, None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = directions[grid[r][c]]
                guard_symbol = grid[r][c]
                break
        if guard_pos:
            break

    visited = set()

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#'

    while True:
        r, c = guard_pos

        if is_valid(r, c):
            visited.add((r, c))

        # check the next position
        dr, dc = guard_dir
        next_r, next_c = r + dr, c + dc
        if next_r == -1 or next_r == rows or next_c == -1 or next_c == cols:
            break

        if not is_valid(next_r, next_c):
            # change direction
            current_symbol_idx = symbols.index(guard_symbol)
            guard_symbol = symbols[(current_symbol_idx + 1) % 4]
            guard_dir = directions[guard_symbol]
        else:
            # move according to the direction
            guard_pos = (next_r, next_c)

    return len(visited)


result = move_guard(grid)
print("Distinct positions visited:", result)
