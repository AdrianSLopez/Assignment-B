# Assignment-B
Consider the game of tic-tac-toe. 
(75pt)
Using the provided file, minimax.py, as a starting point, we are going to be implementing the Minimax algorithm for tic-tac-toe.

Several functions, including the main game loop are already implemented for you. The main loop does an X move, checks for a winner, does an O move, checks for a winner, until a winner is found or the board is full.

Presently, the O_move function simply returns the first available space (starting from the top left). You do not have to implement something else for O, but may do so as needed to test your code.

What you will actually be implementing, and what I will be testing, is the X_move function. The X_move function should take in a board state as an argument, run minimax, and return the best move for X at that turn. 

More details are given in the function header.

For the minimax algorithm, you should use +10 for an X win, -10 for an X loss and 0 for a draw. In addition, in order to motivate the agent to end games quickly and not drag them out, subtract the depth of the completed game state from the score. Examples are given in the function header.

I will be testing this by giving running the X_move function with several input board states and expecting the best move

Do not wait until the last minute to start this!

We will go over the starter code in class.


(25 pt)
What is the time and space complexity of your approach?
