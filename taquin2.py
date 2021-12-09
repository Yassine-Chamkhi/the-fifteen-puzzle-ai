#y printi el board bel mezyen
def printBoard(board):
    i=1
    for t in board:
        for p in t:
            if i%3 != 0:
                print(p, end =" ")
            else:
                print(p)
            i=i+1


resultBoard = [[0,1,2], [3,4,5],[6,7,8]]

# THESES INITIAL BOARDS EITHER DON'T WORK OR TAKE WAY TOO MUCH TIME
# El theni, ken tbadlou el resultBoard yebda mel 1 youfa fel 0, works with BFS in 71000+ steps
#initialBoard = [[7,2,4],[5,0,6],[8,3,1]]
#initialBoard = [[3,6,7],[5,2,1],[4,8,0]]


# THESE INITIAL BOARDS ARE SO SIMPLE AND WORK
#initialBoard = [[1,2,5],[3,4,0],[6,7,8]]
initialBoard = [[1,2,5],[3,0,4],[6,7,8]]
#printBoard(initialBoard)

#This function returns an array of possible movemements (in order: TOP LEFT RIGHT BOTTOM) AND
#the last two indexes are the position of 0 in the matrix (line, column)
def mvtsAndPosition(board):
    mvtsAndPos = [1,1,1,1, 0, 0]
    for lineNb, line in enumerate(board):
        if line.count(0) > 0:
            column = line.index(0)
            mvtsAndPos[4] = lineNb
            mvtsAndPos[5] = column
            if(lineNb == 0):
                mvtsAndPos[0] = 0
            elif lineNb == 2:
                mvtsAndPos[3] = 0
            if column == 0:
                mvtsAndPos[1] = 0
            elif column == 2:
                mvtsAndPos[2] = 0
    return mvtsAndPos



def moveTop(board, line, column):
    board[line][column] = board[line-1][column]
    board[line-1][column] = 0

def moveBottom(board, line, column):
    board[line][column] = board[line+1][column]
    board[line+1][column] = 0

def moveRight(board, line, column):
    board[line][column] = board[line][column+1]
    board[line][column+1] = 0

def moveLeft(board, line, column):
    board[line][column] = board[line][column-1]
    board[line][column-1] = 0

#This function returns the possible nodes that can be explored from current
def possibleBoards(board):
    pb = []
    temp = list(map(list, board))
    info = mvtsAndPosition(board)
    line = info[4]
    column = info[5]
    #Chose to start with left because nothing is left of my sanity
    if info[1] == 1:
        temp = list(map(list, board))
        moveLeft(temp, line, column)
        pb.append(temp)
        
    if info[2] == 1:
        temp = list(map(list, board))
        moveRight(temp, line, column)
        pb.append(temp)

    if info[0] == 1:
        temp = list(map(list, board))
        moveTop(temp, line, column)
        pb.append(temp)

    if info[3] == 1:
        temp = list(map(list, board))
        moveBottom(temp, line, column)
        pb.append(temp)
    return pb

# print("Possible boards")
# for b in possibleBoards(initialBoard):
#     printBoard(b)
#     print("---")


#BREADTH FIRST SEARCH
def BFS(board):
    print('Breadth First Search Started')
    queue = []
    queue.append(board)
    for b in queue:
        printBoard(b)
        print("-----")
        if b == resultBoard:
            print("Hooray, BFS found it in", queue.index(b), " steps!")
            break
        else:
            pbs = possibleBoards(b)
            if(pbs):
                for pb in pbs:
                    if pb not in queue:
                        queue.append(pb)
BFS(initialBoard)




#DEPTH FIRST SEARCH, 
def DFS(board, pile):
    if(board not in pile):
        pile.append(board)
        index = pile.index(board)
        printBoard(board)
        print("-----")
        if board == resultBoard:
            print("Hooray, DFS found it in ", pile.index(board)," steps!")
            return True
        else:
            pbs = possibleBoards(board)
            if pbs:
                for pb in pbs:
                    if(DFS(pb, pile)):
                            return True
DFS(initialBoard, [])

#haka l'iteratif ma aamaltoush
#def DFSI(board, pile, depth):