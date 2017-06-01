# Implementation d'une table, donc un ensemble de ligne

from Row import Row


class Table(object):
    """docstring for Table."""
    def __init__(self, key=None, value=None):
        super(Table, self).__init__()
        self.key = []
        self.table = []

        self.lenghtE = 0

        if key is not None and value is not None:
            self.key.append(key)
            self.table.append(Row(key, value))
            self.lenghtE = len(self.table[0])

    def __repr__(self):
        s = ""
        for v in self.table:
            s += repr(v) + "\n"
        return s

    def __iter__(self):
        for v in self.table:
            yield v

    def __len__(self):
        return len(self.key)

    def __contains__(self, item):
        if self.key is None:
            return False
        else:
            return any(res == item for res in self.key)

    def addRow(self, key=None, value=None, row=None):
        if row is None and key is not None and value is not None:
            self.key.append(key)
            self.table.append(Row(key, value))
        elif row is not None and key is None and value is None:
            self.key.append(row.key)
            self.table.append(row)
        else:
            print("Error")

    def addEmptyRow(self, key):
        tmpList = []
        for _ in range(self.lenghtE):
            tmpList.append(None)
        self.addRow(row=Row(key, tmpList))

    def delRow(self, key):
        for v in range(len(self.key)):
            if self.table[v].key == key:
                del self.table[v]
                break

        self.key.remove(key)

    def newColumn(self):
        for row in self.table:
            row.addElement()
        self.lenghtE += 1

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

    OT = Table("a", [0, 1])

    OT.addRow("b", [0, 0])
    OT.addRow("c", [1, 0])

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
