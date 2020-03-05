
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

def createRow(a, b, c):
    global grid
    row = [a,b,c]
    grid.append(row)
    
def possible(x,y,n):
    for i in range(3):
        if n == grid[x][i]:
            print("Denna finns på rad")
            return False
        if n == grid[i][y]:
            print("Dena finns på kolumnen")
            return False
        
    for i in range(3):
        for j in range(3):
            if n == grid[i][j]:
                print("Detta finns i boxen")
                return False
    return True

grid = []
createRow(1,2,3)
createRow(4,0,6)
createRow(7,8,9)

solved = False
while(solved == False):
    n = 1
    print(n)
    if (possible(1,1,n) == True):
        grid[1][1] = n
        solved = True
    print("\n",grid[0], "\n", grid[1], "\n", grid[2])
    n = n + 1
    if n == 20:
        solved = True