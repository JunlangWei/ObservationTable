# Implementation d'une ligne de l'observation table
# key
# value
#
# find

class Row(object):
    """docstring for Row."""
    def __init__(self, key, value):
        super(Row, self).__init__()
        self.key = key
        self.value = value

    def __repr__(self):
        return str(self.key) + " : " + str(self.value)

    def addElement(self, element):
        self.value.append(element)
