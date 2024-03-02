class VacuumCleaner:
    def __init__(self, initial_position, environment):
        self.position = initial_position
        self.environment = environment

    def move(self):
        if self.environment[self.position] == 'Dirty':
            print(f"Current position: {self.position}, Dirty! Cleaning...")
            self.environment[self.position] = 'Clean'
        else:
            print(f"Current position: {self.position}, Clean")

        # Move to the next position
        if self.position == 0:
            self.position = 1
        else:
            self.position = 0

    def clean_environment(self):
        while 'Dirty' in self.environment:
            self.move()
        print("Environment is clean!")


# Example usage:
if __name__ == "__main__":
    # Define the environment as a list, where 'Dirty' represents a dirty location
    environment = ['Dirty', 'Clean']

    # Create a VacuumCleaner object starting at position 0
    vacuum = VacuumCleaner(initial_position=0, environment=environment)

    # Clean the environment
    vacuum.clean_environment()
