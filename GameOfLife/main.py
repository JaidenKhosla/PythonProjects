import sys,random,pprint, os

rows = columns = 10
quantity = 0.1 #float(sys.argv[1])
if quantity > 1: raise ValueError("Quantity should be between 0 and 1")

grid = [[1 if random.random() <= quantity else 0 for _ in range(columns)] for _ in range(rows)]

def validate(y: int, x: int, grid: list) -> bool:
    neighbors = [(y-1,x-1),(y+1,x+1), (y-1, x+1), (y+1, x-1), (y-1,x), (y+1, x), (y, x+1),(y, x-1)]
    alive = 0
    for neighbor in neighbors:
        y2,x2 = neighbor  
        if not (0 <= y2 < rows and 0 <= x2 < columns):
            print("JHJDFJJF")
            continue
        item = grid[y2][x2]
        if item == 1:
            alive+=1
    if item == 1 and (alive < 2 or alive > 3):
        grid[y][x] = 0
    elif item == 0 and alive == 3:
        grid[y][x] = 1
    
def prettyPrint(grid:list[list[int]]) -> str:
    newString = ""
    for y in range(rows):
        for x in range(columns):
            newString+=str(grid[y][x])+" "
        newString+='\n'
    return newString
        
while True:
    for y in range(rows):
        for x in range(columns):
            validate(y,x,grid)
            print(prettyPrint(grid), end="\r")
            os.system("clear")

    
    