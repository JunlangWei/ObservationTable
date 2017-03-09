#Initialize S and E to {X}.
#Ask membership queries for X and each a E A.
#Construct the initial observation table (S. E, T)

#Repeat:
#	While (S, E, T) is not closed or not consistent:
#		If (S, E, T) is not consistent,
#			then find s, and s2 in S, a E A, and e E E such that
#			row(~) = row(sz) and T(sl a. e) =! T(a2. a. e),
#			add a. e to E,
#			and extend T to (S U S. A) E using membership queries.
#		If (S, E, T) is not closed.
#			then find s1 E S and a E A such that
#			row(S1. a) is different from row(s) for all s E S,
#			add s1 a to S1
#			and extend T to (S U S. A). E using membership queries.

#	Once (S, E, T) is closed and consistent. let M = M(S, E, T).
#	Make the conjecture M.
#	If the Teacher replies with a counter-example t, then
#		add t and all its prefixes to S
#		and extend T to (S U S. A) E using membership queries.
#Until the Teacher replies yes to the conjecture M.
#Halt and output M.

from ObsTable import ObsTable

Lambda = ' '
A = ['0', '1']

S = {}
E = {}
T = {}

queries = [Lambda] + A

ObservationTable = ObsTable(Lambda, A)

print(ObservationTable)
