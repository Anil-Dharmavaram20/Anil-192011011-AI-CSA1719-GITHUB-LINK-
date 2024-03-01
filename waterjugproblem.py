from collections import deque

class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"({self.x}, {self.y})"

def water_jug(x, y, z):
    if z > max(x, y):
        return None

    visited = set()
    queue = deque()
    initial_state = State(0, 0)
    queue.append((initial_state, []))

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)

        if current_state.x == z or current_state.y == z:
            return path + [current_state]

        # Filling jugs
        queue.append((State(x, current_state.y), path + [(current_state, "Fill X")]))
        queue.append((State(current_state.x, y), path + [(current_state, "Fill Y")]))

        # Emptying jugs
        queue.append((State(0, current_state.y), path + [(current_state, "Empty X")]))
        queue.append((State(current_state.x, 0), path + [(current_state, "Empty Y")]))

        # Pouring water from one jug to another
        to_x = min(current_state.x + current_state.y, x)
        to_y = min(current_state.x + current_state.y, y)

        queue.append((State(to_x, current_state.y - (to_x - current_state.x)), path + [(current_state, "Pour X to Y")]))
        queue.append((State(current_state.x - (to_y - current_state.y), to_y), path + [(current_state, "Pour Y to X")]))

    return None

def print_solution(solution):
    if solution is None:
        print("No solution exists.")
    else:
        print("Steps to measure the desired quantity:")
        for state, action in solution[1:]:
            print(action)

if __name__ == "__main__":
    x = 4  # Capacity of Jug X
    y = 3  # Capacity of Jug Y
    z = 2  # Desired quantity

    solution = water_jug(x, y, z)
    print_solution(solution)
