from transformation_operation import TransformationOperation


class TransformationSnapshot:
    def __init__(self, operation: TransformationOperation, position: int, character: str, word: str):
        self.operation = operation
        self.word = word
        # The character that was move or replaced
        self.character = character
        # The position of the character. The position is intended to be displayed to the user therefore it starts with 1 instead of 0.
        self.position = position

    def describe(self):
        output = ""
        if self.operation == TransformationOperation.Insertion:
            output += "Inserted the character '{}' at position {}".format(self.character, self.position)
        elif self.operation == TransformationOperation.Subtraction:
            output += "Removed the character '{}' at position {}".format(self.character, self.position)
        else:
            output += "Replaced the character at position {} with '{}'".format(self.position, self.character)
        output += "\nSnapshot of the word: " + self.word
        print(output)
