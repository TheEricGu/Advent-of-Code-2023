with open('pipe-maze-input.txt', 'r') as input_file:
    lines = input_file.readlines()
grid = [list(line.strip()) for line in lines] # convert into grid
row_s, col_s = next((row, col) for row, line in enumerate(grid) for col, char in enumerate(line) if char == 'S') # next() finds first occurrence of S
r, c = row_s, col_s
scanned = set()
steps = 1 
while True:
    directions = [(1, 0, 'S|7F', '|JL'), (-1, 0, 'S|JL', '|7F'), (0, 1, 'S-LF', '-J7'), (0, -1, 'S-J7', '-FL')]
    for dr, dc, valid_chars, next_chars in directions:
        if (0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) # in bounds
            and grid[r][c] in valid_chars and grid[r + dr][c + dc] in next_chars # valid maze path
            and (r + dr, c + dc) not in scanned): # not retracing
            scanned.add((r + dr, c + dc))
            r, c = r + dr, c + dc
            break
    else: # else condition if for loop goes to completion (you are 1 before completing loop to 'S')
        print(steps // 2)
        break
    steps += 1