import random

def main():
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]
    
    print_board(board)
    solve(board)
    print_board(board)
    
#working
def print_board(board):
    for i in range(len(board)):
        if i%3 == 0:
            print("----------------------")
        for j in range(len(board[i])):
            if j%3 == 0:
                print("|", end="")
            print(board[i][j], end=" ")
            if j == 8:
                print("|")
        if i == 8:
            print("----------------------")

#working
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return [i, j]
    return None

numset = set()

#working
def solve(board):
    #base case
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    #recursive case (working)
    for num in range(1,10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            # try to see if we can finish the board with the current num
            if solve(board):
                return True
            # if cannot solve, we backtrack/reset to 0 and try again with another num
            else:
                board[row][col] = 0

    # #recursive case but more randomise (not working)
    # while len(numset) < 9:
    #     num = random.randint(1,9)
    #     numset.add(num)
    #     print(numset)
    #     if is_valid(board, num, row, col):
    #         board[row][col] = num
    #         if solve(board):
    #             return True
    #         else:
    #             board[row][col] = 0

    return False

#working
def is_valid (board, num, row, col):
    #check row
    for i in range(len(board[row])):
        if board[row][i] == num and col != i:
            return False
    
    #check column
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False
    
    #check box
    length = row - row%3
    width = col - col%3
    for i in range(length, length+3):
        for j in range(width, width+3):
            if board[i][j] == num and row != i and col != j:
                return False

    return True


if __name__ == "__main__":
    main()