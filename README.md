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

* Player will win when there are no more places to dig and no mine its found.

## Existing Features

* Random board generation
- Mines are randomly placed on the board

![initial](/images/boardInitial.JPG)

- Accepts user input
- Maintain information in dug positions.
- Shows squares containing numbers from 0 to 2, with each number being the number of mines adjacent to the uncovered square.

![input](/images/result.JPG)



