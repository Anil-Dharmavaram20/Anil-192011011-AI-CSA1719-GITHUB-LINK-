import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def astar(self, start, goal):
        open_list = [(0, start)]  # (f, node)
        came_from = {}
        g_score = {node: float('inf') for node in self.graph}
        g_score[start] = 0
        f_score = {node: float('inf') for node in self.graph}
        f_score[start] = self.heuristic(start, goal)

        while open_list:
            current_f, current_node = heapq.heappop(open_list)

            if current_node == goal:
                path = self.reconstruct_path(came_from, current_node)
                return path

            for neighbor, weight in self.graph[current_node]:
                tentative_g_score = g_score[current_node] + weight
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current_node
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

        return None

    def heuristic(self, node, goal):
        # Here, we use Manhattan distance as the heuristic
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def reconstruct_path(self, came_from, current_node):
        path = [current_node]
        while current_node in came_from:
            current_node = came_from[current_node]
            path.append(current_node)
        return path[::-1]

# Example usage:
if __name__ == "__main__":
    # Example graph representing distances between nodes
    g = Graph()
    g.add_edge((0, 0), (0, 1), 1)
    g.add_edge((0, 0), (1, 0), 1)
    g.add_edge((0, 1), (1, 1), 1)
    g.add_edge((1, 0), (1, 1), 1)

    start = (0, 0)
    goal = (1, 1)

    path = g.astar(start, goal)
    if path:
        print("Path found:", path)
    else:
        print("No path found")
