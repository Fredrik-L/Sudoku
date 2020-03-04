def createGrid():
    grid = []
    i = 0
    while(i < 3):
        j = 0
        while(j < 3):
            grid.append(" ")
            j = j + 1
        i = i + 1
    return grid
grid = createGrid()
print(grid)