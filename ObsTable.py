class ObsTable(object):
    """docstring for ObsTable."""
    def __init__(self, Lambda, Alphabet):
        super(ObsTable, self).__init__()
        # Label of column - Sufix
        self.E = [Lambda]
        # Label of row - Prefix
        self.S = [Lambda]
        self.SUSA = [Lambda]
        # Element of the observation table
        T = [[1] * 1 for _ in range(1)]

    def __repr__(arg):
        s = "|   | "
        for v in self.E:
            s = v + " | "
