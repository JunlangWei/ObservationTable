from Table import Table


class Automata(object):
    """docstring for Automata."""
    def __init__(self, alphabet, Q):
        super(Automata, self).__init__()
        # Transition table
        self.key = alphabet
        self.table = Table()
        self.table.lenghtE = len(self.key)

        self.q0 = 0

        self.Q = Q
        self.Fa = []
        self.Fr = []

        self.createTable()

    def __repr__(self):
        s = ("    " + str(self.key) + "\n ----- \n" + repr(self.table) + " ----- \n")
        s += (" * q0 = " + str(self.q0) + "\n")
        s += (" * Final state : \n" + str(self.Fa) + "\n")
        return s

    def createTable(self):
        for qu in range(len(self.Q)):
            self.table.addEmptyRow(qu)

    def setValue(self, value, state, symbol):
        row = self.table.getRow(state)
        for k in range(len(self.key)):
            if self.key[k] == symbol:
                break
        row.value[k] = value

    # dot -Tpng automata.gv -o DFA.png
    def drawAutomataGraphviz(self):
        f = open("automata.gv", "w")

        f.write("digraph finite_state_machine {\n")
        f.write("   rankdir=LR\n")
        f.write("   size=\"8,5\"\n")
        f.write("\n")

        for s in self.Fa:
            f.write("   node [shape = doublecircle, label=\"q" + str(s) + "\", fontsize=12] " + str(s) + ";\n")
        f.write("\n")

        for s in self.Fr:
            f.write("   node [shape = circle, label=\"q" + str(s) + "\", fontsize=12] " + str(s) + ";\n")
        f.write("\n")

        f.write("   node [shape = point] qi;\n")
        f.write("   qi -> 0;\n")

        f.write("\n")
        for row in self.table:
            for a in range(len(self.key)):
                f.write("   " + str(row.key) + " -> " + str(row.value[a]) + " [label = \"" + self.key[a] + "\"];\n")
            f.write("\n")

        f.write("}\n")

        f.close()
