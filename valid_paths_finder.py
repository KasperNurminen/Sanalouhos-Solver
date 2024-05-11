from itertools import chain
from models import ValidPath


class ValidPathsFinder():
    def __init__(self, data, word_list) -> None:
        self.data = data
        self.data_flattened = flatten(data)
        self.word_list = word_list

    def get_all_possible_paths(self) -> list[ValidPath]:
        possible_paths = set()
        for word in self.word_list:
            paths = self.__get_possible_paths_for_word(word)
            if len(paths) > 0:
                for path in paths:
                    possible_paths.add(ValidPath(path))
        return list(possible_paths)

    def __get_permutations_starting_from(self, row, col, word):
        visited = set()
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1), (-1, 0),
                      (0, -1), (-1, -1), (1, -1)]  # 8 possible directions
        result = []

        def in_bounds(x, y):
            return 0 <= x < len(self.data) and 0 <= y < len(self.data[0])

        def find_permutations(x, y, path, coord_path):
            path_string = ''.join(path)
            if path_string == word:
                result.append(tuple(coord_path))
                return

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if in_bounds(nx, ny) and (nx, ny) not in visited:
                    new_path_string = path_string + self.data[nx][ny]
                    if (word.startswith(new_path_string)):
                        visited.add((nx, ny))
                        find_permutations(
                            nx, ny, path + [self.data[nx][ny]], coord_path + [(nx, ny)])
                        visited.remove((nx, ny))

        # Start recursion from the initial position if it's in bounds and initialize visited set
        if in_bounds(row, col):
            visited.add((row, col))
            find_permutations(row, col, [self.data[row][col]], [(row, col)])
            visited.remove((row, col))

        return result

    def __get_possible_paths_for_word(self, word, width=5):
        start_char = word[0]
        positions = [i for i, char in enumerate(
            self.data_flattened) if char == start_char]
        all_paths = []

        for pos in positions:
            row = pos // width
            col = pos % width
            words = self.__get_permutations_starting_from(row, col, word)
            all_paths.extend(words)

        return all_paths


def flatten(matrix):
    return tuple(chain.from_iterable(matrix))
