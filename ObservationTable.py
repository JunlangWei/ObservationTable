from Table import Table
from ListKey import ListKey
from Automata import Automata


class ObservationTable(object):
    """docstring for ObservationTable."""
    def __init__(self, Lambda, Alphabet):
        super(ObservationTable, self).__init__()
        self.empty = Lambda
        self.alphabet = Alphabet

        # Label of column - Sufix
        self.E = [Lambda]
        self.allKey = ListKey()
        # Label of row - Prefix
        self.S = Table(Lambda, [None])
        self.allKey.addKey(Lambda, 1)
        # Label of row - Prefix.A
        self.SUSA = Table()

        for a in Alphabet:
            self.SUSA.addRow(a, [None])

        self.S.lenghtE = 1
        self.SUSA.lenghtE = 1

        self.f = open("saveInput.txt", "w")

    def __repr__(self):
        s = ("T -> " + str(self.E) + "\n ----- \n" + repr(self.S) +
             " ----- \n" + repr(self.SUSA))
        return s

    def addCounterExample(self, request):
        # On fait une recheche pour rajouter le contre-example, ainsi que tous les mots qui le compose
        # mot : abb -> ajout de a, puis ab et enfin abb
        for i in range(1, len(request) + 1):
            if request[:i] in self.allKey:
                if request[:i] in self.SUSA:
                    temp = self.SUSA.getRow(request[:i])
                    self.SUSA.delRow(temp.key)
                    self.S.addRow(row=temp)
            else:
                self.S.addEmptyRow(request[:i])
                self.allKey.addKey(request[:i], None)

            # Pour chaque mot ajouter, on rajoute aussi le mot suivi de l'alphabet
            for a in self.alphabet:
                if (request[:i] + a) not in self.SUSA:
                    self.SUSA.addEmptyRow(request[:i] + a)
                    if (request[:i] + a) not in self.allKey:
                        self.allKey.addKey(request[:i] + a, None)

    def completeObservationTable(self):
        # Pour chaque élèment des tables, on vérifie si il est à None (Pas rempli)
        # Si il l'est, on vérifie d'abord dans l'ensemble des clés si le mot n'est pas déjà présent et remplis
        # Si non, on fait une membership queries, qui est ajouté dans la liste des clés
        for i in range(len(self.E)):
            for j in range(len(self.S)):
                if self.S.table[j].value[i] is None:
                    k = self.S.table[j].key + self.E[i]
                    if k in self.allKey and self.allKey.getValue(k) is not None:
                        self.S.table[j].value[i] = self.allKey.getValue(k)
                    elif k in self.allKey and self.allKey.getValue(k) is None:
                        self.allKey.setValue(k, self.membershipQueriesWithRow(self.S.table[j], i))
                    else:
                        self.membershipQueriesWithRow(self.S.table[j], i)
                        self.allKey.addKey((self.S.table[j].key + self.E[i]),
                                           self.S.table[j].value[i])
            for j in range(len(self.SUSA)):
                if self.SUSA.table[j].value[i] is None:
                    k = self.SUSA.table[j].key + self.E[i]
                    if k in self.allKey and self.allKey.getValue(k) is not None:
                        self.SUSA.table[j].value[i] = self.allKey.getValue(k)
                    elif k in self.allKey and self.allKey.getValue(k) is None:
                        self.allKey.setValue(k, self.membershipQueriesWithRow(self.SUSA.table[j], i))
                    else:
                        self.membershipQueriesWithRow(self.SUSA.table[j], i)
                        self.allKey.addKey((self.SUSA.table[j].key + self.E[i]),
                                           self.SUSA.table[j].value[i])

    def membershipQueriesWithRow(self, row, pos_symbol):
        evaluation = "-1"
        while (evaluation != "0" and evaluation != "1"):
            evaluation = input("Symbol " + row.key + self.E[pos_symbol] +
                               " is present in this automate? (Yes:1 / No: 0)\n")
        self.f.write(evaluation + "\n")
        evaluation = int(evaluation)

        row.value[pos_symbol] = evaluation
        return evaluation

    def makeClosed(self):
        sStr = []
        for row in self.S:
                sStr.append(str(row.value))

        b = False
        temp = None
        # On teste d'abord si la table est fermée
        for row in self.SUSA:
            if str(row.value) not in sStr:
                temp = row
                b = True
                break

        # Si elle ne l'est pas, on fait les modifications nécessaires
        if b:
            self.SUSA.delRow(temp.key)
            self.S.addRow(row=temp)

            for a in self.alphabet:
                self.SUSA.addEmptyRow(temp.key + a)
                self.allKey.addKey(temp.key + a, None)

        return b

    def addNewColumn(self, key):
        self.E.append(key)
        self.S.newColumn()
        self.SUSA.newColumn()

    def makeConsistent(self):
        b = False
        # On tese si la table est consitente
        for i in range(0, len(self.S) - 1):
            for j in range(i + 1, len(self.S)):
                if self.S.table[i] == self.S.table[j]:
                    b = True
                    s1 = self.S.table[i]
                    s2 = self.S.table[j]
                    break

        # Si elle ne l'est pas, on la rend consistente
        if b:
            ae = None
            for a in self.alphabet:
                for e in self.E:
                    s1ae = s1.key + a + e
                    s2ae = s2.key + a + e
                    if self.allKey.getValue(s1ae) != self.allKey.getValue(s2ae):
                        if e == self.empty:
                            ae = a
                        else:
                            ae = a + e
                        break
                if ae is not None:
                    break

            if ae is not None:
                self.addNewColumn(ae)
            else:
                b = False

        return b

    def getRow(self, key):
        tmp = self.S.getRow(key)
        if tmp is None:
            tmp = self.SUSA.getRow(key)
        return tmp

    # Input: closed and complete observatio table (STA, EXP, OT)
    # Output: DFA (A, Q, q0, Fa, Fr, Delta)
    # Q <- { qu : u E Red ^ v < u OT[v] != OT[u] }
    # Fa <- { qu E Q :  OT[u][lambda] == 1 }
    # Fr <- { qu E Q :  OT[u][lambda] == 0 }
    # for qu E Q do:
    #     for a E A do:
    #         Delta(qu, a) <- qw E Q : OT[ua] == OT[w]
    #     end
    # end
    # return (A, Q, q0, Fa, Fr, Delta)

    def makeAutomata(self):
        Q = [self.empty]

        # On remplit d'abord Q
        for i in range(0, len(self.S)):
            b = False
            for j in range(0, i):
                if i != j and self.S.table[i] == self.S.table[j]:
                    b = False
                    break
                if self.S.key[i] not in Q and self.S.table[i] != self.S.table[j]:
                    b = True
            if b:
                Q.append(self.S.key[i])

        automata = Automata(self.alphabet, Q)

        # Ensuite, on peut remplir les tables Fa et Fr
        for qu in range(len(Q)):
            if self.allKey.getValue(Q[qu] + self.empty) == 1:
                automata.Fa.append(qu)
            else:
                automata.Fr.append(qu)

        # Enfin, on peut créer la table contenant les états et les transitions
        for qu in range(len(Q)):
            for a in self.alphabet:
                for qw in range(len(Q)):
                    if self.getRow(Q[qu] + a) == self.getRow(Q[qw]):
                        automata.setValue(qw, qu, a)
                        break

        print("\n-- Q  ------------------------------")
        print(automata.Q)
        print("\n-- Fa ------------------------------")
        print(automata.Fa)
        print("\n-- Fr ------------------------------")
        print(automata.Fr)

        return automata


if __name__ == '__main__':
    print("Début des tests")

    A = ['a', 'b']
    Lambda = ''

    OT = ObservationTable(Lambda, A)

    print(OT)

    OT.completeObservationTable()
    print(OT)

    print("\n-- Closed ----------------------")

    OT.makeClosed()
    # OT.completeObservationTable()
    print(OT)

    print("\n-- Consistent ------------------")

    temp = OT.SUSA.getRow("b")
    OT.SUSA.delRow(temp.key)
    OT.S.addRow(row=temp)
    print(temp)

    for a in OT.alphabet:
        OT.SUSA.addEmptyRow(temp.key + a)
    OT.completeObservationTable()
    print("1 --- " + str(OT))

    OT.makeConsistent()
    OT.completeObservationTable()
    print(OT)

    print("\n--------------------------------")

    print(OT)

    OT.makeAutomata()

    # # Creation de la table
    # OT = Table("a", [0, 1])
    # OT.addRow("b", [0, 0])
    # OT.addRow("c", [1, 0])
    # print(OT)
    # print("--------------------")
    # queries = Queries(OT.getRow("b"), "a", 1)
    # queries.get_evaluation()
    # print("--------------------")*
    # print(OT)

    print("Fin des tests")
