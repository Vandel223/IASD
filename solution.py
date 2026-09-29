import search
from argparse import ArgumentParser

class GardenerProblem(search.Problem):
    START_POS = (0, 0)  # Starting position of the gardener

    def __init__(self):
        # Initial state
        self.N = 0
        self.M = 0
        self.W0 = 0
        self.grid = []
        self.plant_types = {}

    def load(self, fh):
        """Loads a problem from the opened file object fh."""
        lines = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

        # Grid size and tank capacity
        self.N, self.M, self.W0 = map(int, lines[0].split())

        # Grid
        self.grid = []
        for i in range(1, 1 + self.N):
            row = list(map(int, lines[i].split()))
            self.grid.append(row)

        # Plant types
        for k, line in enumerate(lines[1 + self.N:], start=1):
            wk, dk = map(int, line.split())
            self.plant_types[k] = {"water": wk, "deadline": dk}

    def check_solution(self, plan, verbose=False):
        """Check validity of a candidate solution plan."""
        x, y = self.START_POS
        water = self.W0
        time = 0
        watered = {}  # plants already watered

        for action in plan:

            if action == "U":
                x -= 1
            elif action == "D":
                x += 1
            elif action == "L":
                y -= 1
            elif action == "R":
                y += 1
            elif action == "W":
                plant = self.grid[x][y]
                if plant > 0:
                    need = self.plant_types[plant]["water"]
                    deadline = self.plant_types[plant]["deadline"]
                    if water >= need and time <= deadline and (plant, (x, y)) not in watered:
                        water -= need
                        watered[(plant, (x, y))] = time
                    else:
                        return False  # invalid watering
                else:
                    return False  # watering empty or obstacle
            else:
                return False  # invalid action

            # Boundary & obstacle checks
            if not (0 <= x < self.N and 0 <= y < self.M):
                return False
            if self.grid[x][y] == -1:
                return False

            # Refill if at base
            if (x, y) == self.START_POS:
                water = self.W0

            time += 1

        # Check if all plants watered exactly once
        num_plants = sum(1 for row in self.grid for cell in row if cell > 0)
        if num_plants != len(watered):
            return False

        if verbose:
            print("Watered:", watered)

        return True
    
    def show_grid(self):
        for row in self.grid:
            print(" ".join(f"{cell:2}" for cell in row))
    
def main():
    parser = ArgumentParser(description="Gardener Problem Solver")
    parser.add_argument("input_file", help="Input file with problem definition")
    parser.add_argument("--plan", help="Candidate solution plan as a string")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    problem = GardenerProblem()
    with open(args.input_file) as fh:
        problem.load(fh)

    if args.plan:
        plan = ""
        with open(args.plan) as fplan_file:
            plan = fplan_file.read().strip()
            is_valid = problem.check_solution(plan, verbose=args.verbose)
            print("Plan is valid." if is_valid else "Plan is invalid.")
    else:
        print("No plan provided to check.")

if __name__ == "__main__":
    main()