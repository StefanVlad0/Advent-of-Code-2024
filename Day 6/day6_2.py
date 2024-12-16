# Author: Vlad Stefan

# Problem 2:
# Input: a file containing a guard (^), and obstacles (#). If an obstacle is directly in front of a guard, it rotates 90 degrees. Otherwise, it moves forward.
# Output The number of distinct positions where adding a single obstacle (#) causes the guard to enter an infinite loop.

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
    states = set()  # to detect loops: (position, direction)

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#'

    while True:
        r, c = guard_pos

        # detect infinite loop
        current_state = (guard_pos, guard_symbol)
        if current_state in states:
            return True  # loop detected
        states.add(current_state)

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

    return False  # no loop detected


def detect_blocking_positions(grid):
    rows, cols = len(grid), len(grid[0])
    blocking_positions = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and (r, c) != find_guard_position(grid):
                grid[r][c] = '#'
                if move_guard(grid):
                    blocking_positions.append((r, c))
                    # print("Blocking position found at", (r, c))
                grid[r][c] = '.'

    return blocking_positions


def find_guard_position(grid):
    directions = {'^', '>', 'v', '<'}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] in directions:
                return (r, c)
    return None


blocking_positions = detect_blocking_positions(grid)
# print("Blocking positions:", blocking_positions)
print("Number of blocking positions:", len(blocking_positions))
