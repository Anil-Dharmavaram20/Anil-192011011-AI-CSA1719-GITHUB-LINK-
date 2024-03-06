import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Representing 3x3 board
        self.current_winner = None  # Keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Left diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Right diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


def minimax(game, maximizing_player):
    if game.current_winner:
        if game.current_winner == 'X':
            return -1
        else:
            return 1
    elif not game.empty_squares():
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for move in game.available_moves():
            game.make_move(move, 'O')
            eval = minimax(game, False)
            game.board[move] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in game.available_moves():
            game.make_move(move, 'X')
            eval = minimax(game, True)
            game.board[move] = ' '
            min_eval = min(min_eval, eval)
        return min_eval


if __name__ == '__main__':
    game = TicTacToe()
    game.print_board_nums()
    while game.empty_squares():
        if game.num_empty_squares() % 2 == 1:
            square = int(input("Enter your move (0-8): "))
            game.make_move(square, 'X')
        else:
            best_move = None
            best_eval = -math.inf
            for move in game.available_moves():
                game.make_move(move, 'O')
                eval = minimax(game, False)
                game.board[move] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = move
            game.make_move(best_move, 'O')
        game.print_board()
        if game.current_winner:
            print(f"{game.current_winner} wins!")
            break
        print()
