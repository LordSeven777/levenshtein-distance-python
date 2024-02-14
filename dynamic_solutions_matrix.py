class DynamicSolutionsMatrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        matrix = []
        # rows + 1 and cols + 1: because the size of the matrix accounts for the empty characters rows and columns
        # apart from the given number of rows and number of columns
        for i in range(rows + 1):
            row = []
            for j in range(cols + 1):
                value = None
                # The initial values of the first row (which refers to the empty character for the initial word)
                # corresponds to the (column) indices of the characters of the target word
                if i == 0:
                    value = j
                # The initial values of the first column (which refers to the empty character for the target word)
                # corresponds to the (row) indices of the characters of the initial word
                elif j == 0:
                    value = i
                # Otherwise value remains set to None
                row.append(value)
            matrix.append(row)
        self.matrix = matrix

    # Matrix value getter
    def get_value(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    # Matrix value setter
    def set_value(self, row: int, col: int, value: int):
        self.matrix[row][col] = value

    def __str__(self):
        output = ""
        for i in range(self.rows + 1):
            for j in range(self.cols + 1):
                output += " {}".format(self.get_value(i, j))
            output += "\n"
        return output
