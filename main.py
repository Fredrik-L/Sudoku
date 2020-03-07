import numpy as np
def printGrid():
    global grid
    print(np.matrix(grid[0]))
    print(np.matrix(grid[1]))
    print(np.matrix(grid[2]))
    print(np.matrix(grid[3]))
    print(np.matrix(grid[4]))
    print(np.matrix(grid[5]))
    print(np.matrix(grid[6]))
    print(np.matrix(grid[7]))
    print(np.matrix(grid[8]))
    print("-------------------")
    #print("\n",grid[0], "\n", grid[1], "\n", grid[2])

def createRow(a,b,c,d,e,f,g,h,j):
    global grid
    row = [a,b,c,d,e,f,g,h,j]
    grid.append(row)
    
def possible(x,y,n):
    for i in range(9):
        if n == grid[x][i]:
            return False
        if n == grid[i][y]:
            return False  
    if x <= 2 and y <= 2:
        startIndex = 0
        rangeIndex = 3
    elif x > 2 and x <= 5 and y > 2 and y <= 5:
        startIndex = 3
        rangeIndex = 6
    else:
        startIndex = 6
        rangeIndex = 9

    for i in range(startIndex,rangeIndex):
        for j in range(startIndex,rangeIndex):
            if n == grid[i][j]:
                
                print(f"hittade {n} i box{i},{j}, x är : {x} y är: {y}")
                return False
    return True

grid = []

createRow(9,0,7,5,4,1,8,0,6)
createRow(5,3,1,9,6,8,7,4,2)
createRow(0,6,8,2,7,3,1,9,5)
createRow(6,7,5,3,9,4,2,1,8)
createRow(1,8,0,7,2,5,3,6,4)
createRow(2,4,3,8,1,6,9,5,7)
createRow(8,0,6,1,5,7,4,2,3)
createRow(3,5,2,4,8,9,6,7,1)
createRow(0,1,4,6,3,2,5,8,9)



printGrid()
def solve():
    global grid
    for x in range(9):
        for y in range(9):
            if(grid[x][y] == 0):
                for n in range(1,10):
                    if(possible(x,y,n) == True):
                        grid[x][y] = n
    printGrid()

solve()
