class ListKey(object):
    """docstring for ListKey."""
    def __init__(self):
        super(ListKey, self).__init__()
        # Contient toutes les clés de la table d'observation
        #  Dict : Key : mot, Value : pointeur vers Row correspondant à Key
        self.key = []

    def __contains__(self, item):
        if self.key is None:
            return False
        else:
            return any(res[0] == item for res in self.key)

    def __repr__(self):
        s = []
        for v in self.key:
            s.append(v[0])
        return str(s)

    def addKey(self, key, value):
        self.key.append((key, value))

    def setValue(self, key, val):
        self.key.remove((key, None))
        self.key.append((key, val))

    def getValue(self, key):
        res = None
        for k in self.key:
            if k[0] == key:
                res = k[1]
        return res
