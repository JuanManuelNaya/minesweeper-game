import random
import re

# lets create a board object to represent the minesweeper game
# this is so that we can just say "create a new board object", or
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_mines):
        """
        Create the board. Helper function to plant mines.
        Initializ set to keep track locations. 
        Save (row,col) tuples in set
        """
        self.dim_size = dim_size
        self.num_mines = num_mines
        self.board = self.create_new_board() # plant the bombs
        self.allocate_values_to_board()
        self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}

    def create_new_board(self):
        """
        Make new board based on dim size and num bombs ( doing lists of lists)
        """
        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None, ..., None],
        #  [None, None, ..., None],
        #  [...                  ],
        #  [None, None, ..., None]]
        # we can see how this represents a board!

     
        mines_planted = 0
        while mines_planted < self.num_mines:
            loc = random.randint(0, self.dim_size**2 - 1) # return a random integer N such that a <= N <= b
            row = loc // self.dim_size  # we want the number of times dim_size goes into loc to tell us what row to look at
            col = loc % self.dim_size  # we want the remainder to tell us what index in that row to look at

            if board[row][col] == '*':
                # this means we've actually planted a bomb there already so keep going
                continue

            board[row][col] = '*' # plant the bomb
            mines_planted += 1

        return board

    def allocate_values_to_board(self):
        """
        Assign numbers 0-8 for all empty spaces.
        It also represents how many neighborig bombs there are.
        """
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] = self.obtain_num_neighboring_bombs(r, c)

    def obtain_num_neighboring_bombs(self, row, col):
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
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
        """
        Dig at selected location.
        Return True if successful dig.
        Return False in case of mine dug.
        Different situations:
        hit a mine -> game over
        # dig at location with neighboring mine -> finish dig
        # dig at location with no neighboring mine -> recursively dig neighbors!

        """
        self.dug.add((row, col)) # keep track that we dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue # don't dig where you've already dug
                self.dig(r, c)

        # if our initial dig didn't hit a mine, we *shouldn't* hit a mine here
        return True

    def __str__(self):
        """
        It will return a string that shows the board to the player.
        """
      
        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
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
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

# play the game
def play(dim_size=10, num_mines=10):
    """
    Game mechanics:
    1- Create the board and plant the mines.
    2- Show the user the board and ask for position to dig.
    3a- If location is a mine, show Game Over message.
    3b- If location is not a bomb, dig recursively until each square is at least next to a bomb
    4- Repeats steps 2 and 3a/b until there are no more plances to dig -> This is a Victory

    """
    board = Board(dim_size, num_mines)
    secure = True 
    while len(board.dug) < board.dim_size ** 2 - num_mines:
        print(board)
        # 0,0 or 0, 0 or 0,    0
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        # if it's valid, we dig
        secure = board.dig(row, col)
        if not secure:
            # dug a bomb ahhhhhhh
            break # (game over rip)

    # 2 ways to end loop, lets check which one
    if secure:
        print("No more plances to dig -> You Won the Game!")
    else:
        print("You dug a mine! -> GAME OVER")
        # let's reveal the whole board!
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__': # good practice :)
    play()