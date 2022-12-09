class hamming:
    def distance(self, first, second):

        if len(first) != len(second):
            raise ValueError(".+")

        if len(first) == 0 and len(second) == 0:
            return 0

        if len(first) == 1 and len(second) == 1:
            if first == second:
                return 0
            else:
                return 1

        result = 0
        for i in range(0, len(first)):
            if first[i] != second[i]:
                result = result + 1

        return result
