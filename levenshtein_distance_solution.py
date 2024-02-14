from typing import List
from dynamic_solutions_matrix import DynamicSolutionsMatrix
from transformation_snapshot import TransformationSnapshot
from transformation_operation import TransformationOperation


class LevenshteinDistanceSolution:
    def __init__(self, initial_word: str, target_word: str, distance: int, matrix: DynamicSolutionsMatrix):
        self.initial_word = initial_word
        self.target_word = target_word
        self.distance = distance
        self.matrix = matrix

    def describe(self):
        print("The Levenshtein distance from '{}' to '{}' is {}".format(self.initial_word, self.target_word, self.distance))
        print("Initial word: {}".format(self.initial_word))
        print("The followings are the {} transformation(s) that occurred:".format(self.distance))
        i = 1
        for snapshot in self.backtrack_transformations():
            print("{}-".format(i))
            i += 1
            snapshot.describe()

    # Returns a list of the transformations snapshots that occurred from initial word to the target word
    def backtrack_transformations(self) -> List[TransformationSnapshot]:
        # The list of the transformations snapshots that occurred
        snapshots: List[TransformationSnapshot] = []

        # The current row and column indices as we backtrack the transformations
        # We start at the last matrix value since it represents the final Levenshtein distance
        row = len(self.initial_word)
        col = len(self.target_word)
        # The current distance at a given row and column of the matrix as we backtrack the transformations
        distance = self.matrix.get_value(row, col)
        # The current word snapshot at the given row and column
        word_snapshot = self.target_word
        # The previous transformation operation that led to the current word snapshot
        operation: TransformationOperation
        # The character and the position of the character moving that caused the transformation
        character: str = ""
        position = 0
        # The word snapshot of the current snapshot during the previous transformation
        prev_word_snapshot = ""

        # Note: For most of the subsequent string manipulations, there are going to be a lot of row - 1 and col - 1
        # because strings indices start at 0 but the first character in the matrix start at index 1

        # As long as the current distance is greater than 0, there are still previous transformations that occurred
        while distance > 0:
            transformation_occurred = True

            # If the current distance came from a subtraction operation
            if distance == (self.matrix.get_value(row - 1, col) + 1):
                operation = TransformationOperation.Subtraction
                # The position is col + 1 because since the previous operation was a subtraction,
                # the character at the previous word snapshot position at the current column's next position was removed
                position = col + 1
                # The previously removed character comes from the initial word
                character = self.initial_word[row - 1]
                prev_word_snapshot = word_snapshot[:col] + character + word_snapshot[col:]
                # Backtracking to the previous row
                row -= 1
            # Otherwise, If the current distance came from an insertion operation
            elif distance == (self.matrix.get_value(row, col - 1) + 1):
                operation = TransformationOperation.Insertion
                # The position is col because since the previous operation was an Insertion,
                # the character at the col position was the one being inserted during the previous operation
                position = col
                # The previously removed character comes from the initial word
                character = word_snapshot[col - 1]
                prev_word_snapshot = word_snapshot[:col - 1] + word_snapshot[col:]
                # Backtracking to the previous column
                col -= 1
            # Otherwise, the transformation didn't result from neither an insertion nor a subtraction
            # In that case, the current distance came from the sum of the distance at [row - 1][col - 1]
            # and the cost of the difference between the character at [row] and at [col]
            else:
                # If the character at [row] and the character at [col] are different, then the previous operation was a substitution
                # since the characters difference cost is 1
                if self.initial_word[row - 1] != self.target_word[col - 1]:
                    operation = TransformationOperation.Substitution
                    # The position of the character being previously replaced is at the col position of the target word
                    position = col
                    character = word_snapshot[col - 1]
                    prev_word_snapshot = word_snapshot[:col - 1] + self.initial_word[row - 1] + word_snapshot[col:]
                # Otherwise, no transformation previously occurred since the characters difference cost is 0
                else:
                    transformation_occurred = False
                # Either way, we backtrack to the both the previous row and previous column
                # since it's the distance at those indices that led to the current distance
                row -= 1
                col -= 1

            # A transformation previously occurred
            if transformation_occurred:
                # Stacking the transformation that previously occurred
                snapshot = TransformationSnapshot(operation, position, character, word_snapshot)
                snapshots.insert(0, snapshot)
                # Setting the current word to backtrack from for the next iterations
                word_snapshot = prev_word_snapshot

            # Setting the current word snapshot and current distance to backtrack from for the next iterations
            distance = self.matrix.get_value(row, col)

        return snapshots
