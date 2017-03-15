# Implementation d'une table, donc un ensemble de ligne

# addRow
# find
from Row import Row

class Table(object):
    """docstring for Table."""
    def __init__(self, key = None, value = None):
        super(Table, self).__init__()
        self.key = []
        self.table = []

        if key != None and value != None:
            self.key.append(key)
            self.table.append(Row(key, value))

    def __repr__(self):
        s = ""
        for v in self.table:
            s += repr(v) + "\n"
        return s

    def __iter__(self):
        for v in self.table:
            yield v

    def addRow(self, key, value):
        self.key.append(key)
        self.table.append(Row(key, value))

    def delRow(self, key):
        for v in range(len(self.key)):
            if self.table[v].key == key:
                del self.table[v]
                break

        self.key.remove(key)

    def isPresent(self, key):
        return key in self.key

    def getRow(self, key):
        tmp = None
        for v in self.table:
            if v.key == key:
                tmp = v
                break
        return tmp

if __name__ == '__main__':
    # Creation de la table

    OT = Table("a", [0,1])

    OT.addRow("b", [0,0])
    OT.addRow("c", [1,0])

    print(OT)

    print("--------------------")
    # Test de la fonction __iter__

    for v in OT:
        print(v)

    print("--------------------")
    # Test de la presence et recuperation d'une row

    print(OT.isPresent("b"))
    print(OT.isPresent("d"))

    print(OT.getRow("b"))

    print("--------------------")
    # Test de lea suppression d'une row

    OT.delRow("b")

    print(OT)
