import random
import re

class Board:
    def __init__(self, dim_size, num_mines):
        """
        Create the board. Helper function to plant mines.
        Initializ set to keep track locations. 
        Save (row,col) tuples in set
        """
        self.dim_size = dim_size
        self.num_mines = num_mines
        self.board = self.create_new_board() 
        self.allocate_values_to_board()
        self.dug = set() 

    def create_new_board(self):
        """
        Make new board based on dim size and num mines ( doing lists of lists)
        """
        # generate a new board
        board = [
            [None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
     
        mines_planted = 0
        while mines_planted < self.num_mines:
            loc = random.randint(0, self.dim_size**2 - 1)  
            row = loc // self.dim_size  
            col = loc % self.dim_size 

            if board[row][col] == '*':
                continue
            # Plant the mine
            board[row][col] = '*' 
            mines_planted += 1

        return board

    def allocate_values_to_board(self):
        """
        Assign numbers 0-8 for all empty spaces.
        It also represents how many neighborig mines there are.
        """
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                # if this is already a mine, nothing happens, continue
                if self.board[r][c] == '*':  
                    continue
                self.board[r][c] = self.obtain_num_neighboring_mines(r, c)

    def obtain_num_neighboring_mines(self, row, col):
        """
        Iterate through each neighboring positions and add number of mines.
        Have to make sure not go out of bounds.
        Positions to check as follows:
        top left: (row-1, col-1)
        top middle: (row-1, col)
        top right: (row-1, col+1)
        left: (row, col-1)
        right: (row, col+1)
        bottom left: (row+1, col-1)
        bottom middle: (row+1, col)
        bottom right: (row+1, col+1)

        """
        num_neighboring_mines = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                # our original location, don't check, continue
                if r == row and c == col:  
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_mines += 1

        return num_neighboring_mines

    def dig(self, row, col):
        """
        Dig at selected location.
        Return True if successful dig.
        Return False in case of mine dug.
        Different situations:
        hit a mine -> game over
        # dig at location with neighboring mine
         -> finish dig
        # dig at location with no neighboring mine
        -> recursively dig neighbors!

        """
        # keep track that we dug here
        self.dug.add((row, col))  

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    # don't dig where you've already dug
                    continue   
                self.dig(r, c)

        # if our initial dig didn't hit a mine, we *shouldn't* hit a mine here
        return True

    def __str__(self):
        """
        It will return a string that shows the board to the player.
        """
        # Create a new array that represents what the user would see
        visible_board = [
            [None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # Putting this together in a string
        str_pre = ''
        # Getting max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            str_pre += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            str_pre += ' |'.join(cells)
            str_pre += ' |\n'

        str_len = int(len(str_pre) / self.dim_size)
        str_pre = indices_row + '-'*str_len + '\n' + str_pre + '-'*str_len

        return str_pre

# play the game
def play(dim_size=10, num_mines=10):
    """
    Game mechanics:
    1- Create the board and plant the mines.
    2- Show the user the board and ask for position to dig.
    3a- If location is a mine, show Game Over message.
    3b- If location is not a mine, 
    dig recursively until each square is at least next to a mine
    4- Repeats steps 2 and 3a/b until there are no more plances to dig 
    -> This is a Victory

    """
    board = Board(dim_size, num_mines)
    secure = True 
    while len(board.dug) < board.dim_size ** 2 - num_mines:
        print(board)
        # 0,0 or 0, 0 or 0,    0
        user_input = re.split(
            ',(\\s)*', input("Time to dig. Input as row,col: "))  
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        # if it's valid, we dig
        secure = board.dig(row, col)
        if not secure:
            # mine dug
            # (game over)
            break 
    # 2 ways to end loop, lets check which one
    if secure:
        print("No more plances to dig -> You Won the Game!")
    else:
        print("You dug a mine! -> GAME OVER")
        # Reveal the whole board!
        board.dug = [
            (r, c) for r in range(board.dim_size) for c 
            in range(board.dim_size)
            ]
        print(board)
# good practice
if __name__ == '__main__': 
    play()