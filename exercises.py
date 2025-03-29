# Define a Game class and initialize game state
class Game():
    def __init__(self):
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

    # define a play_game method 
    def play_game(self):
        # confirm the method is accessible on an instance of the Game class
        print("Welcome to Tic-Tac-Toe! Let's start.")
    # method to print the current state of the board
    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    # method to print the current game status
    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

     # consolidated render method
    def render(self):
        self.print_board()
        self.print_message()

game_instance = Game()
game_instance.play_game()