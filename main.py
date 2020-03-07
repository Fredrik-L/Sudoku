import numpy as np
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


def createGrid2():
    grid = []
    row1 = [8,9,3,2,7,6,4,5,1]
    row2 = [2,7,6,4,5,1,8,9,3]
    row3 = [4,5,1,8,9,3,2,7,6]
    row4 = [5,1,8,9,3,2,7,6,4]
    row5 = [9,3,2,7,6,4,5,1,8]
    row6 = [7,6,4,5,1,8,9,3,2]
    row7 = [6,4,5,1,8,9,3,2,7]
    row8 = [1,8,9,3,2,7,6,4,5]
    row9 = [3,2,7,6,4,5,1,8,9]

    grid.append(row1)
    grid.append(row2)
    grid.append(row3)
    grid.append(row3)
    grid.append(row4)
    grid.append(row5)
    grid.append(row6)
    grid.append(row7)
    grid.append(row8)
    grid.append(row9)

    return grid


grid = createGrid2()
print(np.matrix(grid))