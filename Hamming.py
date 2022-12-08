class hamming:
    def distance(self, first, second):

        if len(first) == 0 and len(second) == 0:
            return 0

        if len(first) == 1 and len(second) == 1 and first == second:
            return 0