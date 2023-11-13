board1=[[7,8,0,4,0,0,1,2,0],
       [6,0,0,0,7,5,0,0,9],
       [0,0,0,6,0,1,0,7,8],
       [0,0,7,0,4,0,2,6,0],
       [0,0,1,0,5,0,9,3,0],
       [9,0,4,0,6,0,0,0,5],
       [0,7,0,3,0,0,0,1,2],
       [1,2,0,0,0,7,4,0,0],
       [0,4,9,2,0,6,0,0,7]]

def printBoard(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print('- - - - - - - - - - - -')
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print(" | ", end='')
            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end='')

def findEmptyPosition(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] ==0:
                return (row, column)
    return False

def checkValidity(board, entry, position):
    #check column
    for column in range(len(board[0])):
        if board[position[0]][column]==entry:
            return False
    #check row
    for row in range(len(board[0])):
        if board[row][position[1]]==entry:
            return False
    #check grid
    #make boxes
    boxes=[[],[],[],[],[],[],[],[],[]]
    box=-1
    for row in range(len(board)):
        for column in range(len(board)):
            if row<=2 and 0<column<=2:
                boxes[0].append(board[row][column])
            elif 2<row<=5 and 0<column<=2:
                boxes[1].append(board[row][column])
            elif 5<row<=8 and 0<column<=2:
                boxes[2].append(board[row][column])
            elif row<=2 and 2<column<=5:
                boxes[3].append(board[row][column])
            elif 2<row<=5 and 2<column<=5:
                boxes[4].append(board[row][column])
            elif 5<row<=8 and 2<column<=5:
                boxes[5].append(board[row][column])
            elif row<=2 and 5<column<=8:
                boxes[6].append(board[row][column])
            elif 2<row<=5 and 5<column<=8:
                boxes[7].append(board[row][column])
            elif 5<row<=8 and 5<column<=8:
                boxes[8].append(board[row][column])
    #check box position
    if position[0]<=2 and position[1]<=2:
        box=0
    elif 2<position[0]<=5 and position[1]<=2:
        box=1
    elif 5<position[0]<=8 and position[1]<=2:
        box=2
    elif position[0]<=2 and 2<position[1]<=5:
        box=3
    elif 2<position[0]<=5 and 2<position[1]<=5 :
        box=4
    elif 5<position[0]<=8 and 2<position[1]<=5:
        box=5
    elif position[0]<=2 and 5<position[1]<=8:
        box=6
    elif 2<position[0]<=5 and 5<position[1]<=8 :
        box=7
    elif 5<position[0]<=8 and 5<position[1]<=8:
        box=8
    if entry in boxes[box]:
        return False

    if board[position[0]][position[1]] ==0:
        return True
    else:
        return False

def solve(board):
    position=findEmptyPosition(board)
    if position==False:
        return True
    else:
        for entry in range(1,10):
            if checkValidity(board, entry, position):
                board[position[0]][position[1]]=entry
                if solve(board):
                    return True
                board[position[0]][position[1]]=0
    return False


solve(board1)
printBoard(board1)