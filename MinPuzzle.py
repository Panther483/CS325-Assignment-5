def minEffort(puzzle): # where puzzle is a 2d matrix
    r = len(puzzle)
    c = len(puzzle[0])

    stack = [(0, 0, 0, {(0, 0)})]
    min_effort = float('inf')

    while stack:
        row, col, current_effort, path = stack.pop()
        if row == r - 1 and col == c - 1:
            min_effort = min(min_effort, current_effort)
            continue

        n = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]
        for new_row, new_col in n:
            if (0 <= new_row < r and 0 <= new_col < c and (new_row, new_col) not in path):
                dif = abs(puzzle[row][col] - puzzle[new_row][new_col])
                new_effort = max(current_effort, dif)
                if new_effort < min_effort:
                    new_path = path.copy()
                    new_path.add((new_row, new_col))
                    stack.append((new_row, new_col, new_effort, new_path))
    return min_effort