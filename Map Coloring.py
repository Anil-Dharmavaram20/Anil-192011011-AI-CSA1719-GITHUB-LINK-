class MapColoring:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, variable, assignment, value):
        for neighbor in self.constraints[variable]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment

        unassigned = [var for var in self.variables if var not in assignment]
        var = unassigned[0]

        for value in self.domains[var]:
            if self.is_consistent(var, assignment, value):
                assignment[var] = value
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None

# Example usage:
if __name__ == "__main__":
    # Variables represent regions, domains represent possible colors
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {var: ['red', 'green', 'blue'] for var in variables}

    # Constraints represent adjacency of regions
    constraints = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    map_coloring = MapColoring(variables, domains, constraints)
    solution = map_coloring.backtracking_search()

    if solution:
        print("Solution found:")
        for region, color in solution.items():
            print(region, "->", color)
    else:
        print("No solution found")
