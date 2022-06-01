# Create a Board object to represent the minesweeper game
# This is so we can say "create a new board object", or
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs num_bombs


#Play game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    # Step 2: show the user the board and ask where they want to dig
    # Step 3a: if location is a bom, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # Step 4: repet steps 2 and 3a/b until there are no more plances to dig -> VICTORY!
    pass