import copy,time,os, random
grid = [[0,0,0,0,0] for i in range(5)]

DEAD_STATE = 0
ALIVE_STATE = 1

def validate(grid: list[list[int]]) -> bool:
    change = False
    initGrid = copy.deepcopy(grid)
    for rowIDX, row in enumerate(grid):
        for colIDX, state in enumerate(row):
            neighbors = [(1,0),(-1,0),(0,-1),(0,1), (1,1),(1,-1),(-1,1),(-1,-1)]
            ALIVE_NEIGHBORS = 0
            DEAD_NEIGHBORS = 0
            for neighbor in neighbors:
                y,x = neighbor
                newY, newX = rowIDX+y, colIDX+x
                if newY in (-1,len(grid)) or newX in (-1,len(row)): break
                item = initGrid[newY][newX]
                if item == ALIVE_STATE: ALIVE_NEIGHBORS+=1
                elif item == DEAD_STATE: DEAD_NEIGHBORS+=1
                else: raise(BaseException)
            
            if (ALIVE_NEIGHBORS < 2 or ALIVE_NEIGHBORS > 3) and state == ALIVE_STATE:
                grid[rowIDX][colIDX] = DEAD_STATE
                change=True
            elif (ALIVE_NEIGHBORS == 3 and state == DEAD_STATE):
                grid[rowIDX][colIDX] = ALIVE_STATE
                change=True
            
    return change

def render(grid: list[list[int]], aliveCharacter="#", deadCharacter=".") -> str:
    newString = "-"*(len(grid[0])+2)+"\n"
    for row in grid:
        newString+="|"
        for col in row:
            newString+= aliveCharacter if col == ALIVE_STATE else deadCharacter
        newString+="|\n"
    newString += "-"*(len(grid[0])+2)
    return newString

def generateRandomBoard(height:int, width: int) -> list[list[int]]:
    return [[1 if random.randint(0,1) == 1 else 0 for _ in range(width)] for _ in range(height)]

randBoard = generateRandomBoard(100,100)

isRunning = True

while isRunning:
    with open("GameOfLife/output.txt","w") as file:
        isRunning = validate(randBoard)
        res = (render(randBoard))
        file.write(res)
        file.close()
    time.sleep(0.1)
    
with open("GameOfLife/output.txt","w") as file: file.write("")