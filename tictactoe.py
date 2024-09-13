class Board:
    #Creates an empty board, 9 empty spaces.
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    #Creates a display of the board, of 3 rows and 3 columns, separated by ---+---+--- and |
    def display(self):
        for i, row in enumerate([self.board[i*3:(i+1)*3] for i in range(3)]):
            print(' ' + ' | '.join(row))
            if i < 2:
                print('---+---+---')

    #Checks if board space is empty and updates the board.
    def update(self, position, symbol):
        if self.board[position] == ' ':
            self.board[position] = symbol
            return True
        return False

    #Checks it the board is full.
    def is_full(self):
        return ' ' not in self.board

    #checks if there is a winner by comparing with win conditions
    def check_winner(self, symbol):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                          (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if all(self.board[i] == symbol for i in condition):
                return True
        return False

class Player:
    #Sets player name and symbol
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Game:
    #Initializes the game
    def __init__(self):
        self.board = Board()
        self.players = [Player(self.get_player_name(1), "X"), 
                        Player(self.get_player_name(2), "O")]
        self.current_player = 0

    #Define player "name"
    def get_player_name(self, player_number):
        name = input(f"Enter name for Player {player_number} (or press Enter for default): ")
        return name if name else f"Player {player_number}"

    #Switches players
    def switch_player(self):
        self.current_player = 1 - self.current_player

    """
    Play the game.

    This method will keep looping until either player wins or the board is full.

    It will display the current state of the board, ask the current player for their move,
    update the board with their move, check for a winner or a tie, and switch the current player.
    If the move is invalid, it will print an error message and ask again.
    """
    def play(self):
        while True:
            self.board.display()
            player = self.players[self.current_player]
            try:
                move = int(input(f"{player.name} ({player.symbol}), enter your move (1-9): ")) - 1
                if self.board.update(move, player.symbol):
                    if self.board.check_winner(player.symbol):
                        self.board.display()
                        print(f"{player.name} wins!")
                        break
                    elif self.board.is_full():
                        self.board.display()
                        print("It's a tie!")
                        break
                    else:
                        self.switch_player()
                else:
                    print("Invalid move. Try again.")
            except:
                print("Invalid input. Enter a number between 1-9")

if __name__ == "__main__":
    game = Game()
    game.play()
