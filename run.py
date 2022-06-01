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
        self.board = self.make_new_board() # plant the bombs

        # initialize a se to keep track of wich locations we've uncovered
        # we'll save (row,col) tuples into this set
        self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):
        # Construct a new board based on the dim size and num bombs
        # we should contruct the list of lists here
        # We have a 2-D board, list of lists is most natural

        # generate a new board
        board = = [[None for _ in range(self.dim_size)] for _ in range(seld.dim_size)]
        # this creates an array like this:
        # [[None,None, ..., None],
        # [None,None, ..., None],
        # [...,                ],
        # [None,None, ..., None]]
        # we can see how this represents a board

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2-1) # return a random integer N such that a <= N <= b

#Play game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    # Step 2: show the user the board and ask where they want to dig
    # Step 3a: if location is a bom, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # Step 4: repet steps 2 and 3a/b until there are no more plances to dig -> VICTORY!
    pass