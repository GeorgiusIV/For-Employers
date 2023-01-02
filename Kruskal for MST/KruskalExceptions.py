
class SharedVertexError(Exception):
    def __init__(self):
        self.message = "On an edge, both verts are identical."
        super().__init__(self.message)

class LengthError(Exception):
    def __init__(self):
        self.message = "The length of the tuple should be no greater or less than 3."
        super().__init__(self.message)

class SpecificTypeError(Exception):
    def __init__(self, index, currentIs = None, shouldBe = None):
        self.message = "Index: " + str(index) + " should be type: " + str(currentIs) + " but is: " + str(shouldBe)
        super().__init__(self.message)

class RepetitionError(Exception):
    def __init__(self):
        self.message = "The same edge or vertex has been input twice."
        super().__init__(self.message)

class MissingVertexError(Exception):
    def __init__(self):
        self.message = "For an edge, the required vertex is missing on the Graph."
        super().__init__(self.message)

class NotInGraph(Exception):
    def __init__(self):
        self.message = "The deleted Edge or Vertex is not present on the Graph."
        super().__init__(self.message)