import csv

filename = "nykysuomensanalista2024.csv"


def initialize_word_list() -> list[str]:
    def read_first_column(filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            first_column = [row[0] for row in reader if row and len(
                row[0]) >= 3]
        return first_column

    return set([word for word in read_first_column(filename)])
