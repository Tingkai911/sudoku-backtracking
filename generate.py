from sudoku import print_board, solve, is_valid
import random

def main():
    #create an empty board 
    board = [[0]*9 for _ in range(9)]
    valid_sudoku = False

    while not valid_sudoku:
        try:
            generate(board)
            solve(board)
            valid_sudoku = True
        except RecursionError:
            valid_sudoku = False

    print_board(board)
    


#problem is that not every board can be solved
def generate(board):
    # generate random value to put at a random place
    count = 0
    while count < 17:
        row = random.randint(0,8)
        col = random.randint(0,8)
        value = random.randint(1,9)
        if board[row][col] == 0 and is_valid(board, value, row, col):
            board[row][col] = value
            count += 1

    

if __name__ == "__main__":
    main()