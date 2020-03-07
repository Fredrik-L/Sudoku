import numpy as np

def createRow(a,b,c,d,e,f,g,h,j):
    global grid
    row = [a,b,c,d,e,f,g,h,j]
    grid.append(row)
    
def possible(x,y,n):
    for i in range(0,9):
        if n == grid[x][i]:
            return False
    for i in range(0,9):
        if n == grid[i][y]:
            return False  

    boxX = (x//3) * 3
    boxY = (y//3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if n == grid[boxX + i][boxY + j]:
                
                print(f"hittade {n} i box{i},{j}, x är : {x} y är: {y}")
                return False
    return True
checks = 0
def solve():
    global grid
    global checks
    for x in range(9):
        for y in range(9):
            checks = checks + 1
            if(grid[x][y] == 0):
                for n in range(1,10):
                    if(possible(x,y,n) == True):
                        grid[x][y] = n
                        solve()
                        grid[x][y] = 0
                return
    print("Solved Sodoku:")
    print(np.matrix(grid))
    print("Trys: ", checks)


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

print("Unsolved Sodoku:")
print(np.matrix(grid))
solve()
