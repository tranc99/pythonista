class Set:
    def __init__(self, values=None):
        """This is the constructor"""
        self.dict = {}

        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        """string representation of a Set object"""
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        self.dict[value] =  True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]
