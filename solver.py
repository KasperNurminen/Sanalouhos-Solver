from models import ValidPath, Solution
import random


class Solver():
    def __init__(self, paths: list[ValidPath], word_list: list[str]):
        self.paths = paths
        self.word_list = word_list

    def find_solution(self, max_iterations=100000) -> Solution:
        best_solution = []
        best_coverage = set()

        for _ in range(max_iterations):
            current_solution = []
            used_coordinates = set()

            # Shuffle tuples to start with a random sequence each iteration
            shuffled_tuples = self.weighted_shuffle(self.paths)
            # print("shuffled_tuples", shuffled_tuples)

            for tup in shuffled_tuples:
                if not any(coord in used_coordinates for coord in tup):
                    current_solution.append(tup)
                    used_coordinates.update(tup)

            # Check if this solution is better
            if len(used_coordinates) > len(best_coverage) or (len(used_coordinates) == len(best_coverage) and len(current_solution) < len(best_solution)):
                best_solution = current_solution
                best_coverage = used_coordinates

                # Early stopping if all coordinates are covered
                if len(best_coverage) == 30:
                    break

        return Solution(best_solution, best_coverage)

    def weighted_shuffle(self, paths_list: list[ValidPath]) -> list[tuple[int, int]]:
        # Create a list of tuples with their weights based on their length
        weighted_tuples = [(tuple(valid_path.path), len(valid_path.path))
                           for valid_path in paths_list]
        # Sort tuples by a random weight influenced by their actual length
        sorted_tuples = sorted(
            weighted_tuples, key=lambda x: x[1] * random.random(), reverse=True)
        # Extract just the tuples in their new biased order
        return [tup for tup, _ in sorted_tuples]
