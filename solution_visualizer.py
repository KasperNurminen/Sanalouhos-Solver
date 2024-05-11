from models import Solution
# Constants to control the layout
WORDS_PER_ROW = 3


def visualize_solution(data, solution: Solution):
    # Iterate over words in chunks of WORDS_PER_ROW
    for i in range(0, len(solution.paths), WORDS_PER_ROW):
        word_group = solution.paths[i:i + WORDS_PER_ROW]

        # Print the words in the current group
        for word in word_group:
            # Space between words in the same row
            constructed_word = ''.join(data[row][col] for (row, col) in word)
            to_pad = 13 - len(constructed_word)
            print(constructed_word, end=' ' * to_pad)
        print("\n" + "________")

        # Determine the number of rows in the grid
        num_rows = len(data)
        num_cols = len(data[0]) if data else 0

        # Print the grids corresponding to each word
        for row in range(num_rows):
            for word in word_group:
                for col in range(num_cols):
                    if (row, col) in word:
                        print(data[row][col], end=" ")
                    else:
                        print(".", end=" ")
                print(" " * 3, end="")  # Space between grids in the same row
            print("")  # Newline at the end of each grid row
        print("________")
