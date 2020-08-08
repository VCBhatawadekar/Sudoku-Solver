def checknumber(y,x,n):
    """ This is a function which tells whether we can insert n at grid[y][x]"""
    global grid
    if n in grid[y]:
        return False
    for i in range(9):
        if grid[i][x]==n:
            return False
    basex = (x//3)*3
    basey = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[i+basey][j+basex] == n:
                return False
    return True
    pass

def solve():
    global grid
    for y in range(9): # for every row
        for x in range(9): # for every column
            if grid[y][x] == 0: # if there is an empty space i.e '0'
                for n in range(1,10): # try putting every digit from 1 to 9
                    if checknumber(y,x,n):
                        grid[y][x]=n
                        solve() # try adding n to that position and see if still it is possible to solve the puzzle
                        grid[y][x]=0 # since 'n' cannot be inserted make it empty and try next digit
                return # if no digit is possible to put then go back and try different digit to for previous cases

    for row in grid:
        print(row)

if __name__=="__main__":
    print("Give space seperated sudoku problem")
    print("Use 0 for blank spaces")
    grid = [] # This is my Sudoku grid
    for i in range(9):# input format
        s = list(map(int,input().split()))
        grid.append(s)
    solve() #here actual solving starts
