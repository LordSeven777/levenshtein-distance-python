from dynamic_solutions_matrix import DynamicSolutionsMatrix
from levenshtein_distance_solution import LevenshteinDistanceSolution


class LevenshteinDistanceSolver:
    # The main method that solves the Levenshtein distance between two words
    @staticmethod
    def solve(initial_word: str, target_word: str) -> LevenshteinDistanceSolution:
        # The distance to be calculated
        distance = 0

        # Initializing the matrix
        rows = len(initial_word)
        cols = len(target_word)
        matrix = DynamicSolutionsMatrix(rows, cols)

        # Calculating the distance by recursively filling the matrix
        # The dimension of the matrix is (rows + 1) * (cols + 1) because the 1st row and 1st column are for the empty characters of both words
        # The indices for the rows and columns start at 1 because the 1st row and 1st column's values have already been initialized
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                distance_from_insertion = matrix.get_value(row, col - 1) + 1
                distance_from_subtraction = matrix.get_value(row - 1, col) + 1
                # When grabbing characters at a given position from the words, the position resolves to the current index minus 1
                # because string characters' indices start at 0 but the index of the 1st character in the matrix starts at 1
                distance_from_substitution = matrix.get_value(row - 1, col - 1) + LevenshteinDistanceSolver.get_chars_diff_cost(initial_word[row - 1], target_word[col - 1])
                distance = min(distance_from_insertion, distance_from_subtraction, distance_from_substitution)
                matrix.set_value(row, col, distance)

        # Latest calculated distance is the Levenshtein distance since it is the last calculated item in the matrix
        # according to the order that previously filled the matrix
        return LevenshteinDistanceSolution(initial_word, target_word, distance, matrix)

    # Gets the cost of the difference between 2 words
    @staticmethod
    def get_chars_diff_cost(c1: str, c2: str):
        return 0 if c1 == c2 else 1
