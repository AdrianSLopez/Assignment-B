GAME_INCOMPLETE = 0
GAME_DRAW = 1
GAME_X = 2
GAME_O = 3

X = 1
O = -1
EMPTY = 0

  
def evaluate_game(board):
    """
    This function tests if a specific player wins.

    Possibilities:
    Three rows    [X X X] or [O O O]
    Three cols    [X X X] or [O O O]
    Two diagonals [X X X] or [O O O]

    Arguments:
    - board: the state of the current board

    Return:
    - GAME_INCOMPLETE, GAME_DRAW, GAME_X, or GAME_O

    """
    win_states = [[board[0][0], board[0][1], board[0][2]],
                  [board[1][0], board[1][1], board[1][2]],
                  [board[2][0], board[2][1], board[2][2]],
                  [board[0][0], board[1][0], board[2][0]],
                  [board[0][1], board[1][1], board[2][1]],
                  [board[0][2], board[1][2], board[2][2]],
                  [board[0][0], board[1][1], board[2][2]],
                  [board[2][0], board[1][1], board[0][2]]]

    if [X, X, X] in win_states:
        return GAME_X
    if [O, O, O] in win_states:
        return GAME_O
    for row in board:
        for i in row:
            if i == EMPTY:
                return GAME_INCOMPLETE
    return GAME_DRAW


def print_board(board):
    """
    This function print out the current board.

    Arguments:
    - board: the state of the current board

    """
    for row in range(len(board)):
        line = ""
        for col in range(len(board[row])):
            if board[row][col] == X:
                line = line + ' X '
            elif board[row][col] == O: 
                line = line + ' O '
            else:
                line = line + "   "
            if col < 2:
                line = line + "|"
        print(line)
        if row < 2:
            print("-----------")


def O_move(board):
    """
    This function plays the O player (The opponent).

    Presently I have made O simply return the first valid move I find
    If you like, you can make this function match your X function
    to watch two minimax agents duke it out
    But really, this can be defined to anything you want it to do for testing.
    I will only be testing "X_move"

    Arguments:
    - board: the state of the current board

    Return:
    - a tuple (i,j) with the row, col of O's chosen move
    """
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return (row, col)
    print("ERROR! No Valid Move!")

class Node:
    def __init__(self, board, level, visited, parent=None, chosenChild=None, x_position=None, score=None):
        self.board = board
        self.level = level
        self.visited = visited
        self.parent = parent
        self.chosenChild = chosenChild
        self.x_position = x_position
        self.score = score


# return an array of locations that are empty
def empty_spaces(board):
    emptySpaces = []

    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                emptySpaces.append((r, c))

    if len(emptySpaces) == 0:
        return None
    
    return emptySpaces

def X_move(board):
    points = [0, 0, 10, -10]
    root = Node(board, 1, False)
    q = [root]

    while len(q) != 0:
        currentNode = q.pop(0)

        board_evaluation = evaluate_game(currentNode.board)

        if board_evaluation == GAME_INCOMPLETE and not currentNode.visited:
            # currentNode has children
            boardEmptySpaces = empty_spaces(currentNode.board)
            children = []

            # Create child nodes based on empty spaces
            for space in boardEmptySpaces:
                child = Node(level=currentNode.level+1, parent=currentNode, visited=False, board=[[currentNode.board[0][0],currentNode.board[0][1],currentNode.board[0][2]],[currentNode.board[1][0],currentNode.board[1][1],currentNode.board[1][2]],[currentNode.board[2][0],currentNode.board[2][1],currentNode.board[2][2]]])

                # Update child's board with X/O move based on currentNode/parent's level
                if(currentNode.level%2 != 0): 
                    child.board[space[0]][space[1]] = X
                    child.x_position = space
                else:
                    child.board[space[0]][space[1]] = O

                children.append(child)
            
            currentNode.visited = True

            # Add parent to the end of children array. 
            # Once all children are explored, the parent(currentNode) will have it's score updated w/chosenChild node.
            # Which will be used to update it's parent's score
            children.append(currentNode)

            children.extend(q)
            q = children

            continue
        else:
            # root
            if(currentNode.parent == None): continue

            currentNode.score = (points[board_evaluation] - (currentNode.level-1)) if currentNode.score == None else currentNode.score

            # Compare (currentNode)child's score with parent's before going to sibling(if there are any) for th
            if currentNode.parent.score == None:
                # CurrentNode is Parent's first child node
                currentNode.parent.score = currentNode.score
                currentNode.parent.chosenChild = currentNode
                continue
            
            
            if currentNode.parent.level%2 != 0:
                # MAX
                if currentNode.score > currentNode.parent.score:
                    currentNode.parent.score = currentNode.score
                    currentNode.parent.chosenChild = currentNode
            else:
                # MIN
                if currentNode.score < currentNode.parent.score:
                    currentNode.parent.score = currentNode.score
                    currentNode.parent.chosenChild = currentNode

     
    # A chance an error might occur because None.x_position 
    print("ROOT NODE: ")
    print("Score: ", root.score)
    print("HAS BEST MOVE: ", False if root.chosenChild==None else True)
    print("Best move for X: ", None if root.chosenChild==None else root.chosenChild.x_position)
    return root.chosenChild.x_position        
            


board = [[X, EMPTY, X],
         [EMPTY, EMPTY, O],
         [EMPTY, O, EMPTY]]

game_winner = GAME_INCOMPLETE
# Game Loop
while game_winner == GAME_INCOMPLETE:
    i, j = X_move(board)
    board[i][j] = X
    print_board(board)
    game_winner = evaluate_game(board)
    if game_winner != GAME_INCOMPLETE:
        break
    i, j = O_move(board)
    board[i][j] = O
    print_board(board)
    game_winner = evaluate_game(board)

# Game is complete, announce winner
if game_winner == GAME_DRAW:
    print("Game was a Draw!")
elif game_winner == GAME_X:
    print("X Wins!")
else:
    print("O Wins!")
