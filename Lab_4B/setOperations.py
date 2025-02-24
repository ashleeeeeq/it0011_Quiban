# Define sets based on the given Venn Diagram
set_A = {'a', 'b', 'c', 'd', 'f', 'g'}
set_B = {'b', 'c', 'h', 'l', 'm', 'o'}
set_C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

print("\na. Number of elements in set A and B: ", len(set_A | set_B))
print(set_A | set_B)
print("\n")

print("b. Elements in set B but not in set A and C: ", len(set_B - (set_A | set_C)))
print(set_B - (set_A | set_C))
print("\n")

print("c. i. Elements in set C but not in set A: ", set_C - set_A)

print("c. ii. Common elements in set A and C: ", set_A & set_C)

print("c. iii. Common elements in set A and B, set B and C, and set A and C: ", (set_A & set_B) | (set_B & set_C))

print("c. iv. Common elements in set A and C but not necessarily in B: ", (set_A & set_C) - set_B)

print("c. v. Element common in all three sets: ", set_A & set_B & set_C)

print("c. vi. Elements unique to set B: ", set_B - (set_A | set_C))