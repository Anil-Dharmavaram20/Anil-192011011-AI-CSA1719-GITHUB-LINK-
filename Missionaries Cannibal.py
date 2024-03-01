from collections import deque

# State representation: (M, C, B)
# M: Number of missionaries on the left bank
# C: Number of cannibals on the left bank
# B: 1 if boat is on the left bank, 0 if boat is on the right bank

def is_valid(state):
    m, c, b = state
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m < c and m > 0:
        return False
    if 3 - m < 3 - c and 3 - m > 0:
        return False
    return True

def successors(state):
    m, c, b = state
    if b == 1:
        return [(m - 1, c, 0), (m, c - 1, 0), (m - 1, c - 1, 0), (m - 2, c, 0), (m, c - 2, 0)]
    else:
        return [(m + 1, c, 1), (m, c + 1, 1), (m + 1, c + 1, 1), (m + 2, c, 1), (m, c + 2, 1)]

def solve():
    initial_state = (3, 3, 1)
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()
        if state == (0, 0, 0):
            return path + [state]

        if state not in visited:
            visited.add(state)
            for succ in successors(state):
                if is_valid(succ):
                    queue.append((succ, path + [state]))

    return None

def print_solution(solution):
    if solution is None:
        print("No solution exists.")
    else:
        print("Steps to reach the goal:")
        for idx, state in enumerate(solution):
            print(f"Step {idx + 1}: {state}")

if __name__ == "__main__":
    solution = solve()
    print_solution(solution)
