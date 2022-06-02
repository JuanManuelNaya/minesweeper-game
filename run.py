import random

# Create a Board object to represent the minesweeper game
# This is so we can say "create a new board object", or
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # Create board
        # helper function
        self.board = self.make_new_board()  # plant the bombs
        self.assign_values_to_board()

        # initialize a se to keep track of wich locations we've uncovered
        # we'll save (row,col) tuples into this set
        self.dug = set()  # if we dig at 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):
        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:
        # [[None,None, ..., None],
        # [None,None, ..., None],
        # [...,                ],
        # [None,None, ..., None]]
        # we can see how this represents a board

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) # return a random integer N such that a <= N <= b
            row = loc // self.dim_size  # we want the number of times dim_size goes into loc to tell us
            col = loc % self.dim_size  # we want the remainder to tell us what index in that row to 

            if board[row][col] == '*':
                #We have already planted a bomb in that specific index so keep going
                continue
            board[row][col] = '*' # plant the bomb
            bombs_planted += 1 
        return board

    def assign_values_to_board(self):
        #now that we have the bombs planted, let's assign a numer 0-8 for all empy spaces which
        #represents how many neighboring bombs there are. we can precompute these and it'll save us some
        # effort checkking what's around the board later on
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.boar[r][c] == '*':
                    #if this is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum numer of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1) 
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        # make sure to not go out of bounds!

        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):  #checking below above
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1): #checking left and right
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at tthe location!
        # return True if successful dig, False if bomb dug

        # scenarios:
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dog at ;pcatopm wotj mp neighboring bombs -> recursively dig neighbors!

        self.dug.add((row, col)) #keep track that we dug here

        if self.board[row][col] == '*': # game ends
            return False
        elif self.board[row][col] > 0: # we dug at a location with neighbouring bombs, we can continue playing so reurn True
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):    # checking below above
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):  #checking left and right
                if (r, c) in self.dug:
                    continue  # don't dig where you have already dug
                self.dig(r, c)

        # if our initial dig didn't hit a bomb, we shouldn't hit a bomb here
        return True

    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns! 
        # return a string that shows the board to the player

        #Create a new array that represents what the user would see
        visible_board = [[None for _ in range (self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '



#Play game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: show the user the board and ask where they want to dig
    # Step 3a: if location is a bom, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # Step 4: repet steps 2 and 3a/b until there are no more plances to dig -> VICTORY!
    pass