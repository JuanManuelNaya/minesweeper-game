# Minesweeper Game

The Minesweeper game is a Python terminal game, wich runs in the Code institue mock terminal on Heroku.

User wins by diggin in different possitions on the board evoiding mines.

Heroku link project. [Heroku](https://minesweeper-game2022.herokuapp.com/)

GitHub link project. [GitHub](https://github.com/JuanManuelNaya/minesweeper-game)

![Responsive](/images/Deployment.JPG)

## How to Play

The Minesweeper game is based on the classic video game creted by Curt Johnson for IBM's OS/2. You can read more on [wikipedia](https://en.wikipedia.org/wiki/Microsoft_Minesweeper)

* A board is randomly generated.

* The player can see a board with positions 0 to 9 for rows and columns.

* Mines are marked as *

* The player will input a number for a row followed by a coma and a number for a column. Example 1,6.

* Squares contain numbers (from 0 to 2), with each number being the number of mines adjacent to the uncovered square.

* If a mine is found is Game Over, if not continue digging.

* If a  dig at location has no neighboring mine it will keep dig recursively to neighbors. 

* Player will win when there are no more places to dig and no mine its found.

## Existing Features

* Random board generation
- Mines are randomly placed on the board

![initial](/images/boardInitial.JPG)

- Accepts user input
- Maintain information in dug positions.
- Shows squares containing numbers from 0 to 2, with each number being the number of mines adjacent to the uncovered square.

![input](/images/result.JPG)

* Input validation and error checking
- You cannot enter coordinates outside the size of the board.
- You cannot enter the same guess twice

![errorCeck](/images/Invalid%20location.JPG)

-Data maintained in class instances

## Future Features
- Allow player to select the board size.
- Allow player to mark positions as not safe.
- Allow player select the number of mines position on the board.

## Data Model

I decided to use a Board class as my model. The game create an instance of a Board class.

The Board class stores the board size, the mines planted, the number of neighboring mines, showing the board, where to dig, showing the board.

The class also has methods to help play the game, such as `create_new_board` wich creates the board, `allocate_values_to_board` to places the mines on the board,  `obtain_num_neighboring_mines` to show how close you are to mines from the position dug,  `dig` to keep playing in case of successfull dig or Game over in case mine found and also if a  dig at location has no neighboring mine it will keep dig recursively to neighbors, `__str__` It will return a string that shows the board to the player.

## Testing

I have manually tested this project by doing the following:

- Tested in my local terminal and the Code institue Heroku terminal.

- Passed the code through a PEP8 linter and confirmed there are no major issues.

- Giving invalid inputs: Same input twice, out of bounds.

## Bugs

* Unsolved Bug

When the user inputs a string the game it will end.

![bugerror](/images/InvalidinputCat.JPG)

* Solved Bug

Fixed error regarding not adding the number of neighonroing mines, check the code and i go t`board[r][c] == '*':num_neighboring_mines += 1` fixed by adding `self.` like this `self.board[r][c] == '*':num_neighboring_mines += 1`

## Validator Testing

* PEP8

- No major error found in PEP8online.com

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:
- Frok or clone this repository
- Create a bew Heroku app
- Set the buildbacks to Python and NodeJS in that order
- Click on Deploy

## Credits

- Code Institute for the deployment terminal
- Wikipedia for the details of the Minesweeper game.


