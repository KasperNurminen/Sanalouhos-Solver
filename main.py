from utils import print_with_date
from word_list_importer import initialize_word_list
from selenium_data_importer import SeleniumDataImporter
from valid_paths_finder import ValidPathsFinder
from solver import Solver
from solution_visualizer import visualize_solution


def main():
    print_with_date("Sanalouhos Solver 2000")
    word_list = initialize_word_list()
    print_with_date(f"Initialized word list with {len(word_list)} words")

    data_importer = SeleniumDataImporter()

    html_content = data_importer.import_data()
    data = data_importer.initialize_data_matrix(html_content)
    print_with_date("Initialized Sanalouhos solver with the following matrix:")
    for row in data:
        print(row)

    valid_paths_finder = ValidPathsFinder(data, word_list)
    all_possible_paths = valid_paths_finder.get_all_possible_paths()

    print_with_date(
        f"Found {len(all_possible_paths)} possible words from the matrix")

    print_with_date("Starting solve...")
    solver = Solver(all_possible_paths, word_list)
    solution = solver.find_solution()
    print_with_date(
        f"Solution found ({len(solution.coverage)} coordinates, {len(solution.paths)} words)")
    visualize_solution(data, solution)


if __name__ == '__main__':
    main()
