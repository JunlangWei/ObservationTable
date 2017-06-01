# Initialize S and E to {X}.
# Ask membership queries for X and each a E A.
# Construct the initial observation table (S. E, T)

# Repeat:
# 	While (S, E, T) is not closed or not consistent:
# 		If (S, E, T) is not consistent,
# 			then find s, and s2 in S, a E A, and e E E such that
# 			row(~) = row(sz) and T(sl a. e) =! T(a2. a. e),
# 			add a. e to E,
# 			and extend T to (S U S. A) E using membership queries.
# 		If (S, E, T) is not closed.
# 			then find s1 E S and a E A such that
# 			row(S1. a) is different from row(s) for all s E S,
# 			add s1 a to S1
# 			and extend T to (S U S. A). E using membership queries.

# 	Once (S, E, T) is closed and consistent. let M = M(S, E, T).
# 	Make the conjecture M.
# 	If the Teacher replies with a counter-example t, then
# 		add t and all its prefixes to S
# 		and extend T to (S U S. A) E using membership queries.
# Until the Teacher replies yes to the conjecture M.
# Halt and output M.

from ObservationTable import ObservationTable

import os


def isAcceptable(A, request):
    b = True
    for a in request:
        if a not in A:
            b = False
            break
    return b


Lambda = ''
# A = ['0', '1']
A = ['a', 'b', 'c', 'd']

OT = ObservationTable(Lambda, A)
OT.completeObservationTable()

print("Initialisation\n" + str(OT) + "\nCréation de l'automate :\n")

while True:
    nCC = True
    while nCC:
        nConsistent = OT.makeConsistent()
        if nConsistent:
            OT.completeObservationTable()

        nClosed = OT.makeClosed()
        if nCC:
            OT.completeObservationTable()

        nCC = nClosed or nConsistent

    print(OT)
    AT = OT.makeAutomata()
    print(AT)

    request = "-1"
    while (request != "0" and request != "1"):
        request = input("This is the automate that you want ? (Yes: 1 / No: 0)\n")

    OT.f.write(request + "\n")
    if request == "0":
        b = False
        while not b:
            request = input("What is the counter-example ? (A : " + str(A) + ")\n")
            OT.f.write(request + "\n")
            b = isAcceptable(A, request)
        OT.addCounterExample(request)
        # print(OT)
        OT.completeObservationTable()
    else:
        break

OT.f.close()
AT.drawAutomataGraphviz()

os.system('clear')
print("===== ===== ===== ===== ===== =====\n")
print("Final Observation table :")
print(OT)
print("----- ----- ----- ----- ----- -----\n")
print("Final Automata :")
print(AT)
print("===== ===== ===== ===== ===== =====\n")
