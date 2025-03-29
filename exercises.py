# Step 1: Define a Game class and initialize game state

class Game():
    def __init__(self, turn, tie, winner, board):
        # string attribute indicated whose turn it is initialized as X
        self.turn = 'X'
        # a boolean attribute indicating if the game ended in a tie, initialized as False
        self.tie = False
        # attribute to store the game-winner, initialized as None
        self.winner = None
        # a dictionary representing the state of the game board
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
