import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move
        if self.parent:
            self.cost = self.parent.cost + 1
        else:
            self.cost = 0

    def __lt__(self, other):
        return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def move_blank(self, direction):
        blank_row, blank_col = self.find_blank()
        if direction == 'up':
            if blank_row > 0:
                new_board = [row[:] for row in self.board]
                new_board[blank_row][blank_col], new_board[blank_row - 1][blank_col] = new_board[blank_row - 1][blank_col], new_board[blank_row][blank_col]
                return PuzzleState(new_board, self, 'Up')
        elif direction == 'down':
            if blank_row < 2:
                new_board = [row[:] for row in self.board]
                new_board[blank_row][blank_col], new_board[blank_row + 1][blank_col] = new_board[blank_row + 1][blank_col], new_board[blank_row][blank_col]
                return PuzzleState(new_board, self, 'Down')
        elif direction == 'left':
            if blank_col > 0:
                new_board = [row[:] for row in self.board]
                new_board[blank_row][blank_col], new_board[blank_row][blank_col - 1] = new_board[blank_row][blank_col - 1], new_board[blank_row][blank_col]
                return PuzzleState(new_board, self, 'Left')
        elif direction == 'right':
            if blank_col < 2:
                new_board = [row[:] for row in self.board]
                new_board[blank_row][blank_col], new_board[blank_row][blank_col + 1] = new_board[blank_row][blank_col + 1], new_board[blank_row][blank_col]
                return PuzzleState(new_board, self, 'Right')
        return None

    def get_neighbors(self):
        neighbors = []
        for direction in ['up', 'down', 'left', 'right']:
            neighbor = self.move_blank(direction)
            if neighbor:
                neighbors.append(neighbor)
        return neighbors

    def heuristic(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != i * 3 + j + 1 and self.board[i][j] != 0:
                    count += 1
        return count

def a_star(start_state):
    open_list = [start_state]
    closed_list = set()

    while open_list:
        current_state = heapq.heappop(open_list)
        if current_state.heuristic() == 0:
            return current_state
        closed_list.add(current_state)
        neighbors = current_state.get_neighbors()
        for neighbor in neighbors:
            if neighbor not in closed_list:
                heapq.heappush(open_list, neighbor)
    return None

def print_path(solution):
    path = []
    current_state = solution
    while current_state:
        path.append(current_state)
        current_state = current_state.parent
    path.reverse()
    for state in path:
        print(state)
        print()

if __name__ == "__main__":
    initial_state = PuzzleState([[1, 2, 3],
                                 [4, 5, 6],
                                 [0, 7, 8]])

    solution = a_star(initial_state)
    print("Solution:")
    print_path(solution)
