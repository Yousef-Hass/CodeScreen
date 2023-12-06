# DropYacht Checkers Assessment


This project requires you to implement the rules of a Checkers game in Python. You are required to implement all the functions in the [board.py](src/board.py) file. **Please read the entire Readme before getting started!** Note: If you don't know the basic rules of checkers, please read the appendix or watch this [video explanation](https://www.youtube.com/watch?v=GnHQJ-PSBB0&ab_channel=TripleSGames).

The unit tests in the [test/test_checkers.py](test/test_checkers.py) file should pass if the functions in [board.py](src/board.py) are implemented correctly.

## Requirements

The [test/test_checkers.py](test/test_checkers.py) file should not be modified. If you would like to add your own unit tests, you can add these in a separate file in the `test` directory.

The [requirements.txt](requirements.txt) file should only be modified in order to add any third-party dependencies required for your solution. Please note that all third-party dependencies required for your solution **MUST** be added to the [requirements.txt](requirements.txt) file, otherwise our GitHub Actions workflow that validates your solution will not pass.

The `pytest` version should not be changed.

Your solution must use/be compatible with `Python version 3.11`.

## What We'll Be Checking For

We're not expecting a time/space efficient solution, but we want candidates to show senior engineer level thinking. Given that, the code has been left intentionally sparse. We're looking for:

1. Proper abstractions
2. Code Readability, including code comments
3. If you have time, additional testing that captures edge cases

## Board Setup
The board is a 2D list of size 8x8. The black pieces are positioned at the odd-indexed positions on the even-indexed rows and at the even-indexed positions on the odd-indexed rows for the first three rows (row indexes 0, 1 and 2).

Here are the positions for black pieces:

Row 0: (0,0), (0,2), (0,4), (0,6)

Row 1: (1,1), (1,3), (1,5), (1,7)

Row 2: (2,0), (2,2), (2,4), (2,6)

The white pieces are positioned similarly but start at row index 5.

Here are the positions for white pieces:

Row 5: (5,1), (5,3), (5,5), (5,7)

Row 6: (6,0), (6,2), (6,4), (6,6)

Row 7: (7,1), (7,3), (7,5), (7,7)

## King Movements

The only difference between a regular piece ('b' or 'w') and a king piece ('bK' or 'wK') is that the king pieces can move and capture both forwards and backwards (diagonally), while regular pieces can only move and capture forwards. Note that kings cannot skip spaces, and they cannot move in all 8 directions; they are still restricted to moving diagonally. **Be sure to check for backwards captures for kings.**

## Turns

Track which player's turn it is. **Black starts the game in checkers, unlike chess.** If someone takes a move out of turn, raise a `ValueError`. If you have extra time, for bonus points, implement a **get_winner** to check for the winner.

## Forced Moves/Jumps

If a player can jump, they must jump. This includes backwards jumps for kings, and double (or triple, etc.) jumps. *Hint: a commonly made mistake in this coding assessment is that a checkers player can "double jump" with two separate pieces.*

## Double/Multiple Jumps

Each call to `move()` should be a single jump. In the case of double jumps, the `move()` method will be called twice, once for each jump. If there is a double jump available, do not change your internal tracking of the turn to the next player - the player with the double jump available must take it. If a player becomes king through a jump, he/she can (and must) continue the turn through a backwards jump if available.

## Appendix: Rules of Checkers

Checkers is played on an 8x8 chess board. The game starts with each player having 12 pieces, black and white, arranged on the dark squares of the board. The pieces can only move diagonally.

1. Regular pieces can only move diagonally forward one space. (In the case of black, from row 2 to row 3, for example).
2. If an opponent's piece is diagonally in front of your piece and the space behind the opponent's piece is free, your piece can jump over the opponent's piece, capturing it.
3. If a piece reaches the last row on the opponent's side, it becomes a King. Kings can move and capture diagonally forwards and backwards.

Good luck!
## License

At CodeScreen, we strongly value the integrity and privacy of our assessments. As a result, this repository is under exclusive copyright, which means you **do not** have permission to share your solution to this test publicly (i.e., inside a public GitHub/GitLab repo, on Reddit, etc.). <br>

## Submitting your solution

Please push your changes to the `main branch` of this repository. You can push one or more commits. <br>

Once you are finished with the task, please click the `Submit Solution` link on <a href="https://app.codescreen.com/candidate/030e0052-924c-4dde-867b-412555b4a4fc" target="_blank">this screen</a>.