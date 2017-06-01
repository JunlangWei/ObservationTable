# Implementation d'une ligne de l'observation table
# key
# value


class Row(object):
    """docstring for Row."""
    def __init__(self, key, value):
        super(Row, self).__init__()
        self.key = key
        self.value = value

    def __repr__(self):
        return str(self.key) + " : " + str(self.value)

    # Implique que len(self.value) == len(other.value)
    def __eq__(self, other):
        b = True
        i = 0
        while b and i < len(self.value):
            if self.value[i] != other.value[i]:
                b = False
            i += 1
        return b

    def __len__(self):
        return len(self.value)

    def addElement(self, val=None):
        self.value.append(val)

if __name__ == '__main__':
    row1 = Row('a', [0, 1])
    row2 = Row('b', [0, 1])
    row3 = Row('c', [1, 1])

    print(row1 == row2)
    print(row1 == row3)
