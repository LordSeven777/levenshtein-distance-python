from levenshtein_distance_solver import LevenshteinDistanceSolver


def main():
    print("Welcome to the Levenshtein distance calculator!")
    initial_word = input("Initial word: ")
    target_word = input("Target word: ")
    solution = LevenshteinDistanceSolver.solve(initial_word, target_word)
    solution.describe()


main()
