class ObsTable(object):
    """docstring for ObsTable."""
    def __init__(self, Lambda, Alphabet):
        super(ObsTable, self).__init__()
        # Label of column - Sufix
        self.E = [Lambda]
        # Label of row - Prefix
        self.S = {Lambda:[1]}
        # Label of row - Prefix.A
        self.SUSA = {}
        # Label for membership queries
        self.MQ = []

        self.addSUSA(Alphabet)

        self.addNewQueries(Alphabet)

    def __repr__(self):
        s = "T -> " + str(self.E) + "\n"
        for key, item in sorted(self.S.items(), key = lambda d: d[0]):
            s += key + " -> " + str(item) + "\n"
        for key, item in sorted(self.SUSA.items(), key = lambda d: d[0]):
            s += key + " -> " + str(item) + "\n"
        return s

    def addNewQueries(self, queries):
        self.MQ += queries
        # Test si une liste est vide :
        # if not self.MQ:

    def addS(self):
        pass

    def addSUSA(self, element):
        for e in element:
            self.SUSA[e] = [0] * len(self.E)

    def isClosed(self):
        sStr = []
        for key, item in self.S.items():
                sStr.append(str(item))

        b = True
        for key, item in self.SUSA.items():
            if str(item) not in sStr:
                b = False
                print(key)
                break
        return b

    def isConsistent(self):
        pass

    def makeClosed(self):
        pass

    def makeConsistent(self):
        pass

if __name__ == '__main__':
    print("Début des tests")
    Lambda = ' '
    A = ['0', '1']

    OT = ObsTable(Lambda, A)

    # print(OT.E)
    # print(OT.S)
    # print(str(OT.SUSA) + "\n")

    print(OT)

    print(OT.isClosed())

    print("Fin des tests")
