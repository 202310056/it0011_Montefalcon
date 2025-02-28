A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

elements_in_A_and_B = A | B
print("Elements in A and B:", elements_in_A_and_B, "Count:", len(elements_in_A_and_B))

elements_only_in_B = B - (A | C)
print("Elements in B but not in A and C:", elements_only_in_B, "Count:", len(elements_only_in_B))

print("i.", C - {'c', 'd', 'f'})
print("ii.", A & C)
print("iii.", B & C)
print("iv.", A & C - {'c'})
print("v.", A & B & C)
print("vi.", B - A - C)
