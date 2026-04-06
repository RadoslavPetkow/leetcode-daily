grid = [[1,4],[2,3]]

total = 0
for row in grid:
    total += sum(row)

top = 0
for i in range(len(grid) - 1):
    top += sum(grid[i])
    bottom = total - top
    if top == bottom:
        print(True)
        break
else:
    cols = [0] * len(grid[0])

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            cols[j] += grid[i][j]

    left = 0
    found = False
    for j in range(len(cols) - 1):
        left += cols[j]
        right = total - left
        if left == right:
            found = True
            break

    print(found)